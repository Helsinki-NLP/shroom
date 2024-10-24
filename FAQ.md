## Welcome to the SemEval-2024 Task-6 - SHROOM, a Shared-task on Hallucinations and Related Observable Overgeneration Mistakes

# Mu-SHROOM 2025 - FAQ

We would like to thank Malvina Nissim and the students of the "Shared Task" course of the Master Information Science and the Erasmus Mundus Programme Language and Communication Technologies, University of Groningen, whose interest and careful scrutiny inspired the creation of this FAQ.

## TASK

**Q: What is this year’s hallucination detection task?**  
A: The Mu-SHROOM 2025 shared task challenges participants to predict the span(s) of text in LLM outputs that correspond to hallucinations. Outputs are provided in multiple (ten) languages. To fulfill the task, we provide a participant's kit, development sets, and unlabeled training sets [ADD LINKS], with the test set being released on [add date]. The test set will mirror the validation set but without the labels, which participants will need to predict. Participants will be ranked using hard labels, and ties will be broken with soft labels.

**Q: What resources can be used to participate in the task?**  
A: You are free to use any resources at hand. We encourage creative solutions. We also strongly encourage using open (non-commercial) systems that can help enhance the state-of-the-art for the whole community.

**Q: Do we need to participate in all of the ten available languages?**  
A: No. You can participate in a single language or as many as you wish. Each language will have its leaderboard.

**Q: What definition of hallucination are we working with?**  
A: To answer this question, we refer you to the definition provided to the annotators that marked the spans of hallucinations in model outputs:  
**Hallucination**: content that contains or describes facts that are not supported by the provided reference. In other words: hallucinations are cases where the answer text is more specific than it should be, given the information available in the provided context.

**Q: Will the MuSHROOM dataset include any metadata beyond the prompt, given that this year’s dataset lacks an explicit semantic reference from which to infer the points of hallucination in the outputs?**  
A: No. Echoing some comments from last year's edition, we want the task to be reflective of real-world applications around detecting the factuality of LLM outputs. One of these challenges is to find a valid semantic reference or trusted source for the claim — we don't expect such information to be readily available, and thus part and parcel of hallucination detection as a task involves finding out the relevant reference.

**Q: What are the main differences with last year’s iteration of the shared task?**  
A: This shared task builds upon our previous iteration, SHROOM, with a few key changes:
- This year, we are not focusing on English only but on 10 languages: Arabic (Modern standard), Chinese (Mandarin), English, Finnish, French, German, Hindi, Italian, Spanish, and Swedish, along with three surprise test languages.
- Last year, we focused on task-specific language models, whereas now we are focusing on LLM outputs.
- This year, participants will have to predict where the hallucination occurs, as opposed to last year’s binary classification task.

**Q: Last year there were two subtasks (model-aware and model-agnostic), is this the case this year?**  
A: No, instead of focusing on model-agnostic and model-aware tracks, this year’s task focuses on the multilingual aspect. Therefore, all data-points in this year's task are model-aware.

**Q: Could the approach to one language be (somehow) combined with the approach to another language?**  
A: That is up to you. In general, we would invite creative approaches to solve the task. It is clear to us that some of the languages would benefit from the transfer of knowledge across languages.

**Q: What are the advantages and disadvantages of detecting hallucinated spans compared to binary classification for hallucination detection, which was used in last year's task?**  
A: Detecting hallucinated spans allows for a more fine-grained understanding of where hallucinations occur and how severe they are, which last year's binary classification at the utterance level could not provide. While binary classification is simpler to implement and evaluate, its contributions are limited if we aim to develop tools and metrics for detecting hallucinations.

## DATA

**Q: Why do you use soft and hard labels?**  
A: In short, because they are complementary:  
- **Hard labels** ∈ {0,1} (binary): A label of 1 is assigned when the corresponding span contains a hallucination. We determine hard labels using majority voting among the annotators.  
- **Soft labels** ∈ [0,1] (continuous): The confidence-based judgments of the annotators. Calculated as the proportion of annotators who marked the span as part of a hallucination out of the total number of annotators.

**Q: Do all the data entries contain hallucinations?**  
A: The data contains some instances where no hallucinations happen. Our datapoint creation process includes prompting 2-3 models with several sampling configurations. This would increase the chances of having at least one output with hallucinated content per prompt. However, this procedure did not render hallucinations for some of the prompts. In the post-evaluation phase, we will release metadata that includes the clarifications provided by the annotators.

**Q: How many annotators participated in the annotation process?**  
A: A minimum of 3 persons annotated each datapoint. For English and Chinese, we had up to 12 annotators go through the dataset; 4 for German, and 3 in all other languages.

**Q: Will you provide information on which annotator made each annotation?**  
A: Yes, during the post-evaluation phase, we will release anonymized data indicating which annotations were made by each annotator. We anticipate that this will enhance transparency and facilitate detailed analysis of the annotation process, but also serve as a valuable resource for examining annotator consistency, inter-annotator agreement and disagreement, and other relevant factors.

**Q: Why do you provide model ID in the dev/test/train sets?**  
A: The IDs of the models used to produce each output are provided for those interested in replicability and further model analysis (e.g., inspecting logits or activations), though participants can opt for model-agnostic approaches. Any methodology can be used, and creativity in developing novel hallucination mitigation techniques is highly encouraged.

**Q: What were the annotation guidelines for the annotated datasets?**  
A: We will release the full annotations guidelines document in the post-evaluation phase. They roughly read as:
- Carefully read the answer text.
- Highlight each span of text in the answer text that is not supported by the provided context (i.e., contains an overgeneration or hallucination).
- Your annotations should include only the minimum number of characters in the text that should be edited/deleted to provide a correct answer (in the case of Chinese, these will be “character components”).
- You are encouraged to annotate conservatively and focus on content words rather than function words. This is not a strict guideline, and you should rely on your best judgments.
- If the answer text does not contain a hallucination, write “NO HALLUCINATION” in the comment box.
- If you are unsure about how to annotate an example, write “UNSURE” in the comment box. Please only use this option as a last resort.
- Ensure that you double-check your annotations. From the “See previous annotations” link, you can edit or delete previous annotations.

**Q: How do the annotators decide where a hallucination span starts and where it ends?**  
A: The annotators were expressly instructed to select the minimal span so that without it, the output would not contain hallucinations. In other words, if the selected span were omitted, the hallucination would be removed.

**Q: Is the annotation performed in stages? (e.g., (1) there is a hallucination; (2) which part signals it?)**  
A: No. It was done in a single stage.

**Q: Could there be discontinuous portions of a hallucination?**  
A: Yes, there are discontinuous spans in the annotated data.

**Q: Were the prompts for different languages on the same topics?**  
A: Yes, there is some overlap in the topics, though not in the prompts. We decided to have a topic overlap to produce analyses.

## MODELLING & EVALUATION

**Q: What is the expected output format with the provided data?**  
A: You need to submit a JSONL, similar to the input data. To make sure things flow smoothly, we will release a format checking script. In more detail: the test files will have the same structure as the validation files but without the `soft_labels` and `hard_labels` keys. Participants will be expected to fill in at least the `soft_labels` keys and otherwise conserve the format of the input files.

**Q: What approach do you think the unlabeled training data would be the best to use for?**  
A: That is up to you. Last year’s participants made use of it by labeling subsets of that data.

**Q: How are the predicted spans of hallucination going to be evaluated?**  
A: For hard labels, we use intersection-over-union (IoU) and for soft labels, we use the Spearman correlation between predicted and reference soft labels. Take a look at the scorer to see its workings ([https://helsinki-nlp.github.io/shroom/scorer.py](https://helsinki-nlp.github.io/shroom/scorer.py)).  
You can run the scorer with predictions using:
```
python3 scorer.py mushroom.en-val.v1.jsonl my-predictions-for-en.jsonl scores.txt
```


## GENERAL

**Q: Is there something we need to know or particularly pay attention to regarding submission and the submission platform?**  
A: Some general recommendations:
- Follow the deadlines; we cannot make exceptions after the deadline.
- Register to the platform well in advance.
- Try not to make your submissions 5 min before the deadline.
- Follow the discussion on our Google group mailing list or the shared task Slack. We are sure you can profit from other people’s questions.

**Q: Can I change the name of my team after registering on the submission website?**  
A: Yes, we can manually update that information. Please reach out via the Google group mailing list or the shared task Slack to inform us.

**Q: There are two model names listed that rely on GGUF-files (TheBloke/Mistral-7B-Instruct-v0.2-GGUF and TheBloke/SauerkrautLM-7B-v1-GGUF): Which exact gguf model files were used to generate the output?**  
A: We used the llama cpp python bindings to run these models. Here are some relevant code snippets:

```python
# Mistral:
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

model_name_or_path = "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
model_basename = "mistral-7b-instruct-v0.2.Q6_K.gguf"
model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)

lcpp_llm = Llama(
    model_path=model_path,
    # add n_ctx, etc. to fit your specific machine
)

# SauerkrautLM:
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

model_name_or_path = "TheBloke/SauerkrautLM-7B-v1-GGUF"
model_basename = "sauerkrautlm-7b-v1.Q4_K_M.gguf"
model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)

lcpp_llm = Llama(
    model_path=model_path,
    # add n_ctx, etc. to fit your specific machine
)
```
