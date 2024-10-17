**TL;DR**  
*Mu-SHROOM est une tâche partagée (shared task) multilingue, non-centrée sur l'anglais, et dont le but est de faire progresser l’état de l’art en matière de détection des hallucinations dans les contenus générés par des grands modèles de langue (LLM). Notre jeu de données annotées contient des hallucinations dans 10 langues différentes, produites par des LLM de dernière génération. Participez dans autant de langues que vous le souhaitez: identifiez les passages qui correspondent à des hallucinations dans des textes produits par des LLM. Restez informés en rejoignant notre [groupe Google](https://groups.google.com/g/semeval-2025-task-3-mu-shroom), notre [Slack](https://join.slack.com/t/shroom-shared-task/shared_invite/zt-2mmn4i8h2-HvRBdK5f4550YHydj5lpnA)  et/ou notre compte [Twitter](http://x.com/mushroomtask) \!*

**Invitation complète**  
Nous sommes heureux d'annoncer la tâche partagée Mu-SHROOM sur la détection des hallucinations ([lien vers le site web](https://helsinki-nlp.github.io/shroom/)). Nous invitons les participants à détecter les hallucinations dans les sorties des LLMs dans un contexte multilingue.

**À propos**  
Cette shared task fait suite à une édition précédente, [SHROOM](https://helsinki-nlp.github.io/shroom/2024/), avec trois différences clés: nous nous basons sur des productions de grands modèles de langues (LLM), notre jeu de données est multilingue, et nous nous focalisons sur la détection d’empans correspondant à des hallucinations.

Les LLM produisent fréquemment des « hallucinations », c’est-à-dire des sorties textuelles plausibles mais incorrectes. Les métriques existantes mesure davantage le caractère grammatical que l'exactitude sémantique. Il en résulte un problème d’autant plus préoccupant que ces modèles sont mis à disposition d’un public large.

Avec Mu-SHROOM, nous souhaitons faire progresser l'état de l'art en matière de détection des hallucinations. Cette nouvelle itération de la tâche partagée se déroule dans un contexte multilingue et multimodèle: nous fournissons des données produites par une variété de LLM à paramètres publics (open-weight) dans 10 langues différentes (allemand, anglais, arabe (standard moderne), chinois (mandarin), espagnol, finnois, français, hindi, italien et suédois).

Les participants sont invités à développer des systèmes capables d'identifier les passages correspondant à des hallucinations pour une ou plusieurs des langues disponibles.  
Comme il est d'usage avec les shared task SemEval, les participants seront invités à soumettre des articles décrivant les systèmes implémentés, avec possibilité de présentation format poster lors du prochain atelier SemEval (coïncidant avec une conférence \*ACL à venir). Les participants qui choisissent de rédiger une description système seront invités à réviser les articles soumis par leurs pairs (2 articles maximum par auteur).

**Dates clés :**  
Toutes les dates limites sont « n'importe où sur Terre » (23h59 UTC-12).

* Publication de l’ensemble de validation: 02/09/2024  
* Publication de l’ensemble d’évaluation: 01/01/2025  
* Fin de la phase d'évaluation : 31/01/2025  
* Soumissions des descriptions de systèmes : 28/02/2025 (à confirmer)  
* Notification d'acceptation : 31/03/2025 (à confirmer)  
* Version finale dûe : 21/04/2025 (à confirmer)  
* Atelier SemEval : Eté 2025 (coïncidant avec une conférence \*ACL)

**Métriques d'évaluation :**  
Les participants seront classés selon deux critères (définis au niveau du caractère) :

1. l'intersection sur l'union des caractères annotés comme hallucinations dans la référence et ceux prédits comme tels par le système  
2. la corrélation entre la probabilité attribuée par le système qu'un caractère fasse partie d'une hallucination et la proportion d’annotateurs marquant ce caractère comme tel.

Les classements seront effectués séparément par langue : vous pouvez vous concentrer uniquement sur les langues qui vous intéressent \!

**Comment participer ?**

* Inscriptions : Veuillez enregistrer votre équipe avant d'effectuer une soumission sur https://mushroomeval.pythonanywhere.com.  
* Soumissions : utilisez notre plateforme pour soumettre vos résultats avant le 31/01/2025  
* Description système: à soumettre avant le 28/02/2025 (à confirmer; détails supplémentaires à venir).

**Vous voulez être tenu au courant?**  
Rejoignez nos listes de diffusion: notre [groupe Google](https://groups.google.com/g/semeval-2025-task-3-mu-shroom), notre [Slack](https://join.slack.com/t/shroom-shared-task/shared_invite/zt-2mmn4i8h2-HvRBdK5f4550YHydj5lpnA)  et/ou notre compte [Twitter](http://x.com/mushroomtask)\!

Nous espérons que vous serez nombreux à participer\!

Merci de votre attention,   
Raúl Vázquez et Timothee Mickus  
Au nom de tous les organisateurs de Mu-SHROOM

