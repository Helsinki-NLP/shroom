
**TL; DR**  
[*Mu-SHROOM*](https://helsinki-nlp.github.io/shroom/) *är ett forskningexperiment för att bidra till bättre hallucinationsdetektion i text som är automatiskt genererad av LLM:er (stora språkmodeller). Mu-SHROOM utförs inom ramen för SemEval-2025 och experimentet avser att behandla fler språk än engelska. Vi har handannoterat hallucinerat innehåll på 10 olika språk från ledande LLM:er. Nu bjuder vi in till ett flerspråkigt experiment i att hitta hallucinerade bitar i genererad text. Gå med i vår [Google group](https://groups.google.com/g/semeval-2025-task-3-mu-shroom) eller vår [Slack](https://join.slack.com/t/shroom-shared-task/shared_invite/zt-2mmn4i8h2-HvRBdK5f4550YHydj5lpnA)\!*

**Fullständig inbjudan**  
Vi är glada över att kunna lansera forskningsexperimentet [Mu-SHROOM](https://helsinki-nlp.github.io/shroom/) för att detektera hallucinationer i text som genererats av flerspråkiga och  instruktionstränade LLM:er.

**Om oss**  
Detta forskningsexpeirment bygger på vår tidigare upplaga från 2023: [SHROOM](https://helsinki-nlp.github.io/shroom/2024), med tre viktiga förbättringar: LLM-centrerade, flerspråkiga annoteringar och prediktion av hallucinationer på delsträngsnivå.

LLM producerar ofta ”hallucinationer”, där modeller genererar rimlig men felaktig text, eftersom de befintliga kvalitets- och utvärderingsmåtten prioriterar språklig kvalitet framför innehållslig riktighet. Detta är en allt viktigare utmaning i takt med att system som bygger på LLM:er används av en bredare allmänhet. 

Genom Mu-SHROOM vill vi flytta forksningsfronten i att upptäcka hallucinerad text. Denna nya iteration av forskningsexpeirmentet är flerspråkigt och inbegriper flera olika LLM:er. Vi tillhandahåller data som genereats av en mängd öppna LLM:er på 10 olika språk (arabiska (modern standard), kinesiska (mandarin), engelska, finska, franska, tyska, hindi, italienska, spanska och svenska).

Vi bjuder in att delta i experimentet genom att utveckla system som kan identifiera och mildra hallucinationer i genererat innehåll på alla experimentspråk.  
Som vanligt i SemEval kommer deltagarna att kunna skicka in en systembeskrivning och kommer om den antas att få presentera dem i posterformat under nästa SemEval-workshop (i samband med en kommande \*ACL-konferens). Deltagare som väljer att skicka in en  systembeskrivning kommer att bli ombedda att granska sina kollegors bidrag (max 2 bidrag att granska per författare)

**Viktiga datum:**  
Alla deadlines är ”var som helst på jorden” (23:59 UTC-12).  
- Utvecklingsdataset släpps senast: 2 sept 2024  
- Testudataset släpps senast: 1 jan 2025  
- Utvärderingen avslutas: 31 dec 2025  
- Systembeskrivningar ska vara inlämnade: 28 feb 2025 (TBC)  
- Antagningsbesked: 31 mars 2025 (TBC)  
- Slutgiltigt manus senast: 21 april 2025 (TBC)  
- SemEval-workshop: Sommaren 2025 (samlokaliserad med en ACL-konferens)

**Utvärderingsmått:**  
Deltagarna kommer att rangordnas efter två mått (båda mätta på teckennivå):  
1. överensstämmelse mellan systemets prediktion av vilka teckensträngar är hallucinerade och den av mänskliga bedömare handannoterade rättningsmallen  
2. hur väl den sannolikhet som deltagarnas system tilldelar att ett visst tecken är en del av en hallucination korrelerar med de empiriska sannolikheter som observerats i våra handannoteringarar.

Rankning och inlämningar kommer att göras separat per språk: delta i så många språk du vill, eller fokusera på de språk du är mest intresserad av\!

**Hur man deltar:**  
Registrera ditt team här https://mushroomeval.pythonanywhere.com  
Skicka in resultat: använd vår plattform för att skicka in dina resultat före 31 jan 2025  
Skicka in din systembeskrivning: systembeskrivningsrapport ska skickas in senast 28 feb 2025 (TBC, fler detaljer kommer).

**Håll koll\!**  
Gå med i vår Googlegroups-sändlista eller vår Slack-kanal\! Vi ser fram emot att ta del av all spännande forskning som Mu-SHROOM kommer att ge upphov till\!

Varma hälsningar,  
Mu-SHROOM  
genom  
Raúl Vázquez och Timothee Mickus

