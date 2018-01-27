# AuB 17-18

Mitschriften zur Vorlesung *AuB17/18* der Uni Stuttgart. Kein Anspruch auf Korrektheit.


|Vorlesung      | Datum der VL |PDF                                    |Thema
|---------------|--------------|---------------------------------------|----------------------------------
|01             |17.10.2017    |[klick](lectures-pdf/lecture01.pdf)    |Closest Pair
|02             |20.10.2017    |[klick](lectures-pdf/lecture02.pdf)    |Min Cut
|03             |24.10.2017    |[klick](lectures-pdf/lecture03.pdf)    |Monte-Carlo, Las Vegas
|04             |27.10.2017    |[klick](lectures-pdf/lecture04.pdf)    |Quicksort, Zero-Knowledge-Proof
|05             |07.11.2017    |[klick](lectures-pdf/lecture05.pdf)    |Quickselect
|06             |10.11.2017    |[klick](lectures-pdf/lecture06.pdf)    |Skiplisten
|07             |14.11.2017    |[klick](lectures-pdf/lecture07.pdf)    |Hashing
|08             |21.11.2017    |[klick](lectures-pdf/lecture08.pdf)    |Perfektes Hashing
|09             |24.11.2017    |[klick](lectures-pdf/lecture09.pdf)    |Perfektes Hashing, Cuckoo-Hashing
|10             |28.11.2017    |[klick](lectures-pdf/lecture10.pdf)    |Contraction Hierarchies
|11             |05.12.2017    |[klick](lectures-pdf/lecture11.pdf)    |Berechenbarkeit/TMs
|12             |08.12.2017    |[klick](lectures-pdf/lecture12.pdf)    |Mehrband TMs
|13             |12.12.2017    |[klick](lectures-pdf/lecture13.pdf)    |Universelle TM
|14             |19.12.2017    |[klick](lectures-pdf/lecture14.pdf)    |Halteproblem
|15             |09.01.2018    |[klick](lectures-pdf/lecture15.pdf)    |Rice, Semi-Entscheidbarkeit, Aufzählbarkeit, Reduktion
|16             |12.01.2018    |[klick](lectures-pdf/lecture16.pdf)    |Allgemeine Halteproblem, weitere unent. Probleme
|17             |16.01.2018    |[klick](lectures-pdf/lecture17.pdf)    |NP, Rucksackproblem
|18             |19.01.2018    |[klick](lectures-pdf/lecture18.pdf)    |NP & P, Bin-Packing, TSP
|19             |23.01.2018    |[klick](lectures-pdf/lecture19.pdf)    |NP vs. P
|20             |26.01.2018    |-                                      |
|21             |              |                                       |
|22             |              |                                       |
|23             |              |                                       |
|24             |              |                                       |


## Mitmachen
Hilfe ist gern gesehen. Ob Grafiken, Mitschriften der Vorlesung in Text- oder Texform oder einfach nur Korrektur.

## Installation
- Latex installieren: (z.B.: Tex-Live, Miktex)
- Latex-Editor der Wahl installieren (z.B.: IntelliJ + TeXiFy-Plugin)

## PDF erzeugen
* *IntelliJ + TeXiFy-Plugin*: Rechtsklick auf die Tex-Datei, dann auf "Run" klicken. Eine PDF-Datei sollte im *out*-Verzeichnis erscheinen.
Die gerenderte PDF bitte ins `lectures-pdf`-Verzeichnis kopieren, und in der Readme eintragen.

* *Falls `pdflatex` und **Python 3.6** installiert:*

    **Alte Methode**:
    ```
    cd scripts
    python updater.py 1 # Erzeugt die erste Vorlesungseinheit-PDF neu
    python updater.py all # Erzeugt alle PDFs neu
    ```

    oder

    **Neue Methode**:
    ```
    cd scripts
    python ud.py 1 # Erzeugt die erste Vorlesungseinheit-PDF neu
    ```

    Die Scripte generieren die PDFs und verschieben sie ins `lectures-pdf` - Verzeichnis.

## Links
- Inspiration: https://github.com/dipdi/aub-skript
- Vorlage: https://komascript.de/node/1692


