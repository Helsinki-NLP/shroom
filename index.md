## Welcome to the SemEval-2024 Task-6 - SHROOM, a Shared-task on Hallucinations and Related Observable Overgeneration Mistakes

**Task description:** SHROOM participants will need to detect grammatically sound output that contains incorrect semantic information (i.e. unsupported or inconsistent with the source input), with or without having access to the model that produced the output.

**Overview of the task:** The modern NLG landscape is plagued by two interlinked problems:
On the one hand, our current neural models have a propensity to produce inaccurate but fluent outputs; on the other hand, our metrics are most apt at describing fluency, rather than correctness. This leads neural networks to “hallucinate”, i.e., produce fluent but incorrect outputs that we currently struggle to detect automatically. For many NLG applications, the correctness of an output is however mission critical. For instance, producing a plausible-sounding translation that is inconsistent with the source text puts in jeopardy the usefulness of a machine translation pipeline. With our shared task, we hope to foster the growing interest in this topic in the community.     

With SHROOM we adopt a post hoc setting, where models have already been trained and outputs already produced: participants will be asked to perform binary classification to identify cases of fluent overgeneration hallucinations in two different setups: model-aware and model-agnostic tracks. That is, participants must detect grammatically sound outputs which contain incorrect or unsupported semantic information, inconsistent with the source input, with or without having access to the model that produced the output. To that end, we will provide participants with a collection of checkpoints, inputs, references and outputs of systems covering three different NLG tasks: definition modeling (DM), machine translation (MT) and paraphrase generation (PG), trained with varying degrees of accuracy. The development set will provide binary annotations from at least five different annotators and a majority vote gold label.    


**Join the mailing group:** [semeval-2024-task-6-shroom@googlegroups.com](https://groups.google.com/u/1/g/semeval-2024-task-6-shroom)

**[Codalab competition page](https://codalab.lisn.upsaclay.fr/competitions/15726)** 

**[Follow us on Twitter](https://twitter.com/shroom2024)**

**[TRAIN unlabeled] Download unlabeled training data - [Google drive link](https://drive.google.com/file/d/1wlGZL8Sdqu7xZngcUSrDqp3DCSkYWoaE/view?usp=sharing)** (Updated November 8, 2023): unlabeled model agnostic and model aware training data (in v2 only the model-aware file has been updated).    
**NOTE:** No labeled training data is provided, however, feel free to use any existing methods and/or datasets to develop your systems, such as [Friel et al. 2023](https://arxiv.org/pdf/2310.18344.pdf), [Guerreiro et al. 2023](https://aclanthology.org/2023.eacl-main.75.pdf), [Li et al. 2023](https://github.com/RUCAIBox/HaluEval), and the [EdinburghNLP github repository](https://github.com/EdinburghNLP/awesome-hallucination-detection).

**[TRIAL] Download trial data - [Google drive link](https://drive.google.com/file/d/12DquaVHbnAAlNzLhiQZOG5Fw1h4JyNIm/view?usp=sharing)** (Updated August 2, 2023): Trial data including README file (in v1.1 only the README file has been updated). 

**[DEV] Download validation data - [Google drive link](https://drive.google.com/file/d/1gwanWbGl5s6VEDw2ZoRqx5M6WBmvWcGy/view?usp=sharing)** (Updated November 3, 2023): Validation data including README file (in v2 only the README and the model-aware file have been updated). 

**[Baseline Kit] Download baseline participant kit - [Google drive link](https://drive.google.com/file/d/1Iv2jKa5XrNfQjzpFnc1WyNtN7AO59W99/view?usp=sharing)** (Updated December 19, 2023): baseline participant kit including README file. 

**[TEST labeled] Download labeled test data - [Google drive link](https://drive.google.com/file/d/15NLbjDouwRaWt79oYCgXhjzQqilel8i9/view?usp=sharing)** (Updated February 2, 2024): labeled model agnostic and model aware test data.

**[Ranking Submission TEST] - Following the final ranking of all submissions on the test data:**  (Updated February 2, 2024)    

- [all submissions result - ZIP file](https://drive.google.com/file/d/1khfXSZa2-B1dv5YxLpvhq1Og1BIsFWVW/view?usp=sharing)
- [all submissions pre_parsed - CSV file](https://drive.google.com/file/d/1c8hnsTj24GcgFcIJ6M3CXHptz01I-2_6/view?usp=sharing)
- [ranking agnostic - CSV file](https://drive.google.com/file/d/1-4zF8iEWX_GdRxKSfGC0CfAszOhZfv4w/view?usp=sharing)
- [ranking aware - CSV file](https://drive.google.com/file/d/1InbPoXgozM8pijD0hgmmD850WvuHlfRW/view?usp=sharing)

[**Important dates for task participants**](https://semeval.github.io/SemEval2024/)

**Organizers of the shared task:**

- [Elaine Zosa](https://ezosa.github.io/), 
University of Helsinki, Finland
- [Raúl Vázquez](https://jrvc.github.io/), 
University of Helsinki, Finland
- [Jörg Tiedemann](https://blogs.helsinki.fi/tiedeman/), 
University of Helsinki, Finland
- [Vincent Segonne](), 
Universite Grenoble Alpes, France
- [Teemu Vahtola](), 
University of Helsinki, Finland
- [Alessandro Raganato](https://raganato.github.io/), 
University of Milano-Bicocca, Italy
- [Timothee Mickus](https://timotheemickus.github.io/), 
University of Helsinki, Finland
- [Marianna Apidianaki](https://mariannaapi.github.io/), 
University of Pennsylvania, USA

