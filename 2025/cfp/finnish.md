**TL;DR**  
[*Mu-SHROOM*](https://helsinki-nlp.github.io/shroom/) *on monikielinen SemEval2025:n yhteydessä järjestettävä kilpailullinen tutkimustehtävä (shared task), jonka tarkoituksena on edistää viimeisintä teknologiaa hallusinaatioiden havaitsemisessa laajojen kielimallien (LLM) avulla tuotetun tekstin osalta. Olemme annotoineet suosittujen LLM:ien tuottamaa ja hallusinaatioita sisältävää tekstiä 10:llä eri kielellä. Tehtävän tarkoituksena on tunnistaa mahdollisimman tarkasti jaksot, joissa laaja kielimalli tuottaa hallusinoitua sisältöä. Voit osallistua tehtävään niin monella kielellä kuin haluat. Pysy ajan tasalla tehtävästä liittymällä [Google](https://groups.google.com/g/semeval-2025-task-3-mu-shroom)\- ja/tai [Slack](https://join.slack.com/t/shroom-shared-task/shared_invite/zt-2mmn4i8h2-HvRBdK5f4550YHydj5lpnA)\-ryhmäämme\!*

**Kutsu**  
Olemme innoissamme saadessamme kutsua teidät osallistumaan Mu-SHROOM-tutkimustehtävään (*shared task*) hallusinaatioiden tunnistamiseksi monikielisessä kontekstissa ([linkki](https://helsinki-nlp.github.io/shroom/) tehtävän verkkosivuille). Kutsumme osallistujia havaitsemaan hallusinoituja jaksoja laajojen kielimallien (LLM) tuottamissa teksteissä.

**Tietoja**  
Tämä tehtävä perustuu edelliseen iteraatioon, [SHROOMiin](https://helsinki-nlp.github.io/shroom/2024), mutta siinä on kolme keskeistä uudistusta: LLM-keskeisyys, aineiston monikielisyys ja keskittyminen hallusinaatiojaksojen ennustamiseen.

Laajat kielimallit tuottavat usein ”hallusinaatioita”, joissa mallit tuottavat tekstiä, joka sisältää uskottavaa mutta virheellistä informaatiota. Yhdeksi ilmiön syyksi voidaan lukea se, että nykyiset mallien laatua testaavat mittarit asettavat kielen sujuvuuden informaation oikeellisuuden edelle. Huoli laajojen kielimallien luotettavuudesta korostuu, kun niitä otetaan yhä laajemmin yleiseen käyttöön.

Mu-SHROOMin avulla haluamme edistää parasta osaamista hallusinoidun sisällön havaitsemisessa. Tämänkertainen, tehtävän toinen toteutus järjestetään edellisestä poiketen monikielisenä. Tarjoamme monikielisen aineiston, joka on tuotettu useilla avoimen käyttöoikeuden laajoilla kielimalleilla. Aineisto sisältää esimerkkejä kymmenellä eri kielellä: arabia (moderni standardi), kiina (mandariini), englanti, suomi, ranska, saksa, hindi, italia, espanja ja ruotsi.

Osallistujia kutsutaan osallistumaan millä tahansa käytettävissä olevista kielistä, ja heidän odotetaan kehittävän järjestelmiä, joilla voidaan tarkasti tunnistaa ja vähentää hallusinaatioita tuotetussa sisällössä.  
Kuten SemEval-tehtävissä on tapana, osallistujia pyydetään toimittamaan tutkimusartikkelimuotoiset järjestelmäraporttinsa ja heillä on mahdollisuus esitellä ne postereina seuraavassa SemEval-työpajassa (joka järjestetään tulevan \*ACL-konferenssin yhteydessä). Osallistujia, jotka päättävät kirjoittaa järjestelmäraportin, pyydetään vertaisarvioimaan muiden osallistujien työt (enintään 2 artikkelia per kirjoittaja).

**Tärkeimmät päivämäärät:**  
Kaikki määräajat ovat ”anywhere on earth” (23:59 UTC-12).  
Arviointijoukko (validation set) saatavilla: 02.09.2024  
Testijoukko (test set) saatavilla: 01.01.2025  
Arviointivaihe päättyy: 31.01.2025  
Järjestelmäraporttien määräaika: 28.02.2025 (TBC).  
Ilmoitus raportin hyväksymisestä: 31.03.2025 (TBC).  
Lopullisten (camera ready) raporttien määräaika: 21.04.2025 (TBC).  
SemEval-työpaja: Kesä 2025 (samaan aikaan ACL-konferenssin kanssa).

**Arviointimittarit:**  
Osallistujat asetetaan paremmuusjärjestykseen kahden mittarin mukaan:  
1\. tunnistettujen hallusinaatioiden päällekkäisyys merkkitasolla (sekä referenssitekstissä merkitty että osallistujien mallin ennustama hallusinaatiojakso)  
2\. kuinka hyvin osallistujien mallin tunnistamien merkkien todennäköisyys korreloi referenssitekstissä annotoitujen merkkien todennäköisyyden välillä.

Paremmuusjärjestykset tehdään kielikohtaisesti, joten osallistujina voitte keskittyä vain niihin kieliin, joista olette kiinnostuneita\!

**Miten osallistua:**  
Rekisteröidy: https://mushroomeval.pythonanywhere.com.  
Tulosten lähettäminen: Käytä alustaa tulosten lähettämiseen ennen 31.01.2025.  
Lähetä järjestelmäraporttisi: raportit on toimitettava 28.02.2025 mennessä (TBC, lisätietoja ilmoitetaan myöhemmin).

**Haluatko pysyä ajan tasalla?**  
Liity [Google-ryhmän postituslistalle](https://groups.google.com/g/semeval-2025-task-3-mu-shroom) tai tehtävän [Slack-kanavalle](https://join.slack.com/t/shroom-shared-task/shared_invite/zt-2mmn4i8h2-HvRBdK5f4550YHydj5lpnA)\! Odotamme innolla osallistumistasi ja jännittävää tutkimusta, jota tämän tehtävän puitteissa syntyy.

Ystävällisin terveisin,  
Raúl Vázquez ja Timothee Mickus.  
Kaikkien Mu-SHROOM-järjestäjien puolesta

