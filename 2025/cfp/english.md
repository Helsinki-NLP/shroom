**TL;DR**  
[*Mu-SHROOM*](https://helsinki-nlp.github.io/shroom/) *is a non-English-centric SemEval-2025 shared task to advance the SOTA in hallucination detection for content generated with LLMs. We’ve annotated hallucinated content in 10 different languages from top \-tier LLMs. Participate in as many languages as you’d like by accurately identifying spans of hallucinated content. Stay informed by joining our  [Google group](https://groups.google.com/g/semeval-2025-task-3-mu-shroom) or our [Slack](https://join.slack.com/t/shroom-shared-task/shared_invite/zt-2mmn4i8h2-HvRBdK5f4550YHydj5lpnA) or follow our [Twitter account](https://x.com/mushroomtask)\!*

**Full Invitation**  
We are excited to announce the Mu-SHROOM shared task on hallucination detection (link to [website](https://helsinki-nlp.github.io/shroom/)). We invite participants to detect hallucination spans in the outputs of instruction-tuned LLMs in a multilingual context. 

**About**  
This shared task builds upon our previous iteration, [SHROOM](https://helsinki-nlp.github.io/shroom/2024), with three key improvements: LLM-centered, multilingual annotations & hallucination-span prediction.

LLMs frequently produce "hallucinations," where models generate plausible but incorrect outputs, while the existing metrics prioritize fluency over correctness. This results in an issue of growing concern as these models are increasingly adopted by the public. 

With Mu-SHROOM, we want to advance the state-of-the-art in detecting hallucinated content. This new iteration of the shared task is held in a multilingual and multimodel context: we provide data produced by a variety of open-weights LLMs in 10 different languages (Arabic (modern standard), Chinese (Mandarin), English, Finnish, French, German, Hindi, Italian, Spanish, and Swedish).

Participants are invited to participate in any of the languages available and are expected to develop systems that can accurately identify and mitigate hallucinations in generated content.   
As is usual with SemEval shared tasks, participants will be invited to submit system description papers, with the option to present them in poster format during the next SemEval workshop (collocated with an upcoming \*ACL conference). Participants that elect to write a system description paper will be asked to review their peers’ submissions (max 2 papers per author)

**Key Dates:**  
All deadlines are “anywhere on Earth” (23:59 UTC-12).

* Dev set available by: 02.09.2024  
* Test set available by: 01.01.2025  
* Evaluation phase ends: 31.01.2025  
* System description papers due: 28.02.2025 (TBC)  
* Notification of acceptance: 31.03.2025 (TBC)  
* Camera-ready due: 21.04.2025 (TBC)  
* SemEval workshop: Summer 2025 (co-located with an upcoming \*ACL conference)

**Evaluation Metrics:**   
Participants will be ranked along two (character-level) metrics:  
1\. intersection-over-union of characters marked as hallucinations in the gold reference vs. predicted as such  
2\. how well the probability assigned by the participants' system that a character is part of a hallucination correlates with the empirical probabilities observed in our annotations.

Rankings and submissions will be done separately per language: you are welcome to focus only on the languages you are interested in\!

**How to Participate:**

* Register: Please register your team before making a submission on https://mushroomeval.pythonanywhere.com  
* Submit results: use our platform to submit your results before 31.01.2025  
* Submit your system description: system description papers should be submitted by 28.02.2025 (TBC, further details will be announced at a later date).

**Want to be kept in the loop?**  
Join our [Google group mailing list](https://groups.google.com/g/semeval-2025-task-3-mu-shroom) or the [shared task Slack](https://join.slack.com/t/shroom-shared-task/shared_invite/zt-2mmn4i8h2-HvRBdK5f4550YHydj5lpnA)\! You can also follow us on [Twitter](https://x.com/mushroomtask). We look forward to your participation and to the exciting research that will emerge from this task.

Best regards,  
Raúl Vázquez and Timothee Mickus   
On behalf of all the Mu-SHROOM organizers

