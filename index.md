### Welcome to SemEval-2025 Task-3 — Mu-SHROOM, the Multilingual Shared-task on Hallucinations and Related Observable Overgeneration Mistakes 

<!-- TM: somehow jrvc elected to add a white-on-white title?
### <span style="color: white;"> Welcome to SemEval-2025 Task-3 — Mu-SHROOM, the Multilingual Shared-task on Hallucinations and Related Observable Overgeneration Mistakes</span> 
-->

<img style="width:45%" src="assets/img/mu-shroom-logo.png" alt="Mu-SHROOM" title="Mu-SHROOM logo" align="right">

Welcome to the official shared task website for Mu-SHROOM, a [SemEval-2025](https://semeval.github.io/SemEval2025/) shared task!

Mu-SHROOM stands for "**Mu**ltilingual **S**hared-task on **H**allucinations and **R**elated **O**bservable **O**vergeneration **M**istakes".
Mu-SHROOM will invite participants to detect hallucination spans in the outputs of instruction-tuned LLMs in a multilingual context. 
This shared task builds upon our previous iteration, SHROOM, with a few key changes: 
- We're looking at 14 languages: Arabic (Modern standard), Basque, Catalan, Chinese (Mandarin), Czech, English, Farsi, Finnish, French, German, Hindi, Italian, Spanish, and Swedish;
- We're now focusing on LLM outputs;
- Participants will have to predict where the hallucination occurs.

_The information on this website is subject to change._ 
We send announcements for any major update on the [Google group mailing list](https://groups.google.com/g/semeval-2025-task-3-mu-shroom) and the [shared task Slack](https://join.slack.com/t/shroom-shared-task/shared_invite/zt-2mmn4i8h2-HvRBdK5f4550YHydj5lpnA).

#### What is Mu-SHROOM?
The task consists in detecting spans of text corresponding to hallucinations. 
Participants are asked to determine which parts of a given text produced by LLMs constitute hallucinations.
The task is held in multi-lingual and multi-model context, i.e., we provide data in multiple languages and produced by a variety of public-weights LLMs.´

In practice, we provide an LLM output (as a string of characters, a list of tokens, and a list of logits), and participants have to compute, for every character in the LLM output string, the probability that it is marked as a hallucination.
Participants are free to use any approach they deem appropriate, including using external resources, and work on any subset of languages they are interested in.

#### How will participants be evaluated?
Participants will be ranked along two (character-level) metrics: 
1. intersection-over-union of characters marked as hallucinations in the gold reference vs. predicted as such
2. how well the probability assigned by the participants' system that a character is part of a hallucination correlates with the empirical probabilities observed in our annotators.

Rankings and submissions will be done separately per language.

Participants can also download the scoring program on its own [here](./scorer.py) for reference and developing their systems.

#### Participant info
Register on [our submission website](https://mushroomeval.pythonanywhere.com/). Only submissions made on our website will be considered for official rankings.

Want to be kept in the loop? Join our [Google group mailing list](https://groups.google.com/g/semeval-2025-task-3-mu-shroom) or the [shared task Slack](https://join.slack.com/t/shroom-shared-task/shared_invite/zt-2mmn4i8h2-HvRBdK5f4550YHydj5lpnA)! 
<!-- We also have a [Twitter acount](https://x.com/mushroomtask). -->


#### Data
Below are links to access the data already released, as well as provisional expected release dates for future splits.
Do note that release dates are subject to change.

| Dataset split | Access |
|---|---|
| **Sample set** | <a href="https://a3s.fi/mickusti-2007780-pub/sample.zip" download>download</a> (v1) |
| **Validation set** | <a href="https://a3s.fi/mickusti-2007780-pub/val.zip" download>download</a> (v2) |
| **Unlabeled train set** | <a href="https://a3s.fi/mickusti-2007780-pub/train.zip" download>download</a> (v1) |
| **Unlabeled test set** | <a href="https://a3s.fi/mickusti-2007780-pub/test-unlabeled.zip" download>download</a> (v1) |
| **Labeled test set** | <a href="https://a3s.fi/mickusti-2007780-pub/test_labeled.zip" download>download</a> (v1)  |

Supplementary metadata, including raw annotations before post-processing and the wikipedia URL used as a reference by our annotators, can be downloaded from <a href="https://a3s.fi/mickusti-2007780-pub/mushroom-extra-info.tar.gz" download>this link</a>.

We are releasing a participant kit, which we'll keep building up. It contains the scoring program, a format checker, as well as two baselines: a random baseline and an XLM-R based system. The latter is a very naive system and is mostly meant for demonstration purposes (in particular how to convert character-level labels into wordpiece-level tags and vice-versa).  
You can download the participant kit from <a href="https://a3s.fi/mickusti-2007780-pub/participant_kit.zip" download>here</a>.



#### Important dates

This information is subject to change; also refer to the [SemEval website](https://semeval.github.io/SemEval2025/) for supplementary information on the submission process.
- Sample data available: 15 July 2024
- Validaiton data ready: 2 September 2024
- Evaluation start: 10 January 2025
- Evaluation end: 31 January 2025
- Paper submission due: 28 February 2025
- Notification to authors: 31 March 2025
- Camera ready due: 21 April 2025
- SemEval workshop: Summer 2025 (co-located with ACL 2025)


#### Organizers of the shared task

- [Raúl Vázquez](https://jrvc.github.io/), 
University of Helsinki, Finland
- [Timothee Mickus](https://timotheemickus.github.io/), 
University of Helsinki, Finland
- [Elaine Zosa](https://ezosa.github.io/), 
SILO AI, Finland
- [Teemu Vahtola](https://teemuvh.github.io/), 
University of Helsinki, Finland
- [Jörg Tiedemann](https://blogs.helsinki.fi/tiedeman/), 
University of Helsinki, Finland
- [Aman Sinha](https://amansinha09.github.io/),
Université de Lorraine, France
- [Vincent Segonne](), 
Université Bretagne Sud, France
- [Fernando Sánchez-Vega](),
CIMAT A. C., Mexico
- [Alessandro Raganato](https://raganato.github.io/), 
University of Milano-Bicocca, Italy
- [Jindřich Libovický](https://ufal.mff.cuni.cz/jindrich-libovicky),
Charles University, Czechia
- [Jussi Karlgren](https://www.lingvi.st/),
SILO AI, Finland
- [Shaoxiong Ji](https://shaoxiongji.github.io/),
Technical University of Darmstadt, Germany
- [Jindřich Helcl](https://ufal.mff.cuni.cz/jindrich-helcl),
Charles University, Czechia
- [Liane Guillou](https://sites.google.com/site/lianeguillou/home),
University of Edinburgh, UK
- [Ona de Gibert](),
University of Helsinki, Finland
- [Jaione Bengoetxea](),
HiTZ Basque Center for Language Technology - Ixa, University of the Basque Country UPV/EHU, Spain
- [Joseph Attieh](), 
University of Helsinki, Finland
- [Marianna Apidianaki](https://mariannaapi.github.io/), 
University of Pennsylvania, USA


#### Looking for something else?

The website for the previous iteration of the shared task is available [here](/shroom/2024).

The logo is available [here](/shroom/assets/img/mu-shroom-logo.png) (<a href="/shroom/assets/img/mu-shroom-logo.png" download>download</a>); we encourage participants to use it where relevant (esp. in your posters)! 

#### Still have questions?
We have compiled a [**FAQ**](/shroom/FAQ)! You can also reach out via our communication channels.
