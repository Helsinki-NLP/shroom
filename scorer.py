import pandas as pd
from scipy.stats import spearmanr
import numpy as np

import argparse as ap

def recompute_hard_labels(soft_labels):
    """optionally, infer hard labels from the soft labels provided"""
    hard_labels = [] 
    prev_end = -1
    for start, end in (
        (lbl['start'], lbl['end']) 
        for lbl in sorted(soft_labels, key=lambda span: (span['start'], span['end']))
        if lbl['prob'] > 0.5
    ):
        if start == prev_end:
            hard_labels[-1][-1] = end
        else:
            hard_labels.append([start, end])
        prev_end = end
    return hard_labels

def load_jsonl_file_to_records(filename):
    """read data from a JSONL file and format that as a `pandas.DataFrame`. 
    Performs minor format checks (ensures that soft_labels are present, optionally compute hard_labels on the fly)."""
    df = pd.read_json(filename, lines=True)
    if 'hard_labels' not in df.columns:
        df['hard_labels'] = df.soft_labels.apply(recompute_hard_labels)
    # adding an extra column for convenience
    df['text_len'] = df.model_output_text.apply(len)
    df = df[['id', 'soft_labels', 'hard_labels', 'text_len']]
    return df.sort_values('id').to_dict(orient='records')

def score_iou(ref_dict, pred_dict):
    """computes intersection-over-union between reference and predicted hard labels, for a single datapoint.
    inputs:
    - ref_dict: a gold reference datapoint,
    - pred_dict: a model's prediction
    returns:
    the IoU, or 1.0 if neither the reference nor the prediction contain hallucinations
    """
    # ensure the prediction is correctly matched to its reference
    assert ref_dict['id'] == pred_dict['id']
    # convert annotations to sets of indices
    ref_indices = {idx for span in ref_dict['hard_labels'] for idx in range(*span)}
    pred_indices = {idx for span in pred_dict['hard_labels'] for idx in range(*span)}
    # avoid division by zero
    if not pred_indices and not ref_indices: return 1.
    # otherwise compute & return IoU
    return len(ref_indices & pred_indices) / len(ref_indices | pred_indices)

def score_cor(ref_dict, pred_dict):
    """computes Spearman correlation between predicted and reference soft labels, for a single datapoint.
    inputs:
    - ref_dict: a gold reference datapoint,
    - pred_dict: a model's prediction
    returns:
    the Spearman correlation, or a binarized exact match (0.0 or 1.0) if the reference or prediction contains no variation
    """
    # ensure the prediction is correctly matched to its reference
    assert ref_dict['id'] == pred_dict['id']
    # convert annotations to vectors of observations
    ref_vec = [0.] * ref_dict['text_len']
    pred_vec = [0.] * ref_dict['text_len']
    for span in ref_dict['soft_labels']:
        for idx in range(span['start'], span['end']):
            ref_vec[idx] = span['prob']
    for span in pred_dict['soft_labels']:
        for idx in range(span['start'], span['end']):
            pred_vec[idx] = span['prob']
    # constant series (i.e., no hallucination) => cor is undef
    if len({round(flt, 8) for flt in pred_vec}) == 1 or len({round(flt, 8) for flt in ref_vec}) == 1 : 
        return float(len({round(flt, 8) for flt in ref_vec}) == len({round(flt, 8) for flt in pred_vec}))
    # otherwise compute Spearman's rho
    return spearmanr(ref_vec, pred_vec).correlation

def main(ref_dicts, pred_dicts, output_file=None):
    assert len(ref_dicts) == len(pred_dicts)
    ious = np.array([score_iou(r, d) for r, d in zip(ref_dicts, pred_dicts)])
    cors = np.array([score_cor(r, d) for r, d in zip(ref_dicts, pred_dicts)])
    if output_file is not None:
        with open(output_file, 'w') as ostr:
            print(f'IoU: {ious.mean():.8f}', file=ostr)
            print(f'Cor: {cors.mean():.8f}', file=ostr)
    return ious, cors

if __name__ == '__main__':
    p = ap.ArgumentParser()
    p.add_argument('ref_file', type=load_jsonl_file_to_records)
    p.add_argument('pred_file', type=load_jsonl_file_to_records)
    p.add_argument('output_file', type=str)
    a = p.parse_args()
    _ = main(a.ref_file, a.pred_file, a.output_file)

