# AuB 17-18

Mitschriften zur Vorlesung *AuB17/18* der Uni Stuttgart.

<table>
<tr><td>

|Vorlesung      | Datum der VL |PDF                                    |
|---------------|--------------|---------------------------------------|
|01             | 17.10.2017   |[klick](lectures-pdf/lecture01.pdf)    |
|02             | 20.10.2017   |[klick](lectures-pdf/lecture02.pdf)    |
|03             | 24.10.2017   |[klick](lectures-pdf/lecture03.pdf)    |
|04             | 27.10.2017   |[klick](lectures-pdf/lecture04.pdf)    |
|05             | 07.11.2017   |[klick](lectures-pdf/lecture05.pdf)    |
|06             | 10.11.2017   |[klick](lectures-pdf/lecture06.pdf)    |
|07             | 14.11.2017   |[klick](lectures-pdf/lecture07.pdf)    |
|08             | 21.11.2017   |[klick](lectures-pdf/lecture08.pdf)    |
|09             | 24.11.2017   |[klick](lectures-pdf/lecture09.pdf)    |
|10             | 28.11.2017   |[klick](lectures-pdf/lecture10.pdf)    |
</td><td>

|Vorlesung      | Datum der VL |PDF                                    |
|---------------|--------------|---------------------------------------|
| 11            | 05.12.2017   |[klick](lectures-pdf/lecture11.pdf)    |
| 12            | 08.12.2017   |[klick](lectures-pdf/lecture12.pdf)    |
| 13            | 12.12.2017   |[klick](lectures-pdf/lecture13.pdf)    |
| 14            | 19.12.2017   |                                       |
| 15            | 22.12.2017   | Scheinklausur                         |
| 16            |              |                                       |
| 17            |              |                                       |
| 18            |              |                                       |
| 19            |              |                                       |
| 20            |              |                                       |

</td>
<!-- <td>

|Vorlesung      | Datum der VL |PDF                                    |
|---------------|--------------|---------------------------------------|
| 21            |              |                                       |
| 22            |              |                                       |
| 23            |              |                                       |
| 24            |              |                                       |
| 25            |              |                                       |
| 26            |              |                                       |
| 27            |              |                                       |
| 28            |              |                                       |
| 29            |              |                                       |
| 30            |              |                                       |

</td> --></tr> </table>

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


