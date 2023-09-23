## Welcome to the SemEval-2024 Task-6 - SHROOM, a Shared-task on Hallucinations and Related Observable Overgeneration Mistakes

**Task description:** SHROOM participants will need to detect grammatically sound output that contains incorrect semantic information (i.e. unsupported or inconsistent with the source input), with or without having access to the model that produced the output.

**Overview of the task:** The modern NLG landscape is plagued by two interlinked problems:
On the one hand, our current neural models have a propensity to produce inaccurate but fluent outputs; on the other hand, our metrics are most apt at describing fluency, rather than correctness. This leads neural networks to “hallucinate”, i.e., produce fluent but incorrect outputs that we currently struggle to detect automatically. For many NLG applications, the correctness of an output is however mission critical. For instance, producing a plausible-sounding translation that is inconsistent with the source text puts in jeopardy the usefulness of a machine translation pipeline. With our shared task, we hope to foster the growing interest in this topic in the community.     

With SHROOM we adopt a post hoc setting, where models have already been trained and outputs already produced: participants will be asked to perform binary classification to identify cases of fluent overgeneration hallucinations in two different setups: model-aware and model-agnostic tracks. That is, participants must detect grammatically sound outputs which contain incorrect or unsupported semantic information, inconsistent with the source input, with or without having access to the model that produced the output. To that end, we will provide participants with a collection of checkpoints, inputs, references and outputs of systems covering three different NLG tasks: definition modeling (DM), machine translation (MT) and paraphrase generation (PG), trained with varying degrees of accuracy. The development set will provide binary annotations from at least five different annotators and a majority vote gold label.    


**Join the mailing group:** [semeval-2024-task-6-shroom@googlegroups.com](https://groups.google.com/u/1/g/semeval-2024-task-6-shroom)

**[Codalab competition page](https://codalab.lisn.upsaclay.fr/competitions/15726)** 

**[TRAIN unlabeled] Download unlabeled training data - [Google drive link](https://drive.google.com/file/d/1IrVRFPnDPUiWHClooLRIeQpbo9ZD7Kr6/view?usp=sharing)** (Updated September 23, 2023): unlabeled model agnostic and model aware training data.

**[TRIAL] Download trial data - [Google drive link](https://drive.google.com/file/d/12DquaVHbnAAlNzLhiQZOG5Fw1h4JyNIm/view?usp=sharing)** (Updated August 2, 2023): Trial data including README file (in v1.1 only the README file has been updated). 

**[DEV] Download validation data - [Google drive link](https://drive.google.com/file/d/1p57VPdhK_dVjEJ4HAPi1vzEn2q-QGqSa/view?usp=sharing)** (Updated September 11, 2023): Validation data including README file. 

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

