# AuB 17-18

**Mithilfe ist erwünscht!** // Mitschriebe zur *Vorlesung AuB17/18*

Mitschriebe bisher:

|Vorlesung      | Datum der VL |PDF                                    |
|---------------|--------------|---------------------------------------|
|01             | 17.10.2017   |[klick](lectures-pdf/lecture01.pdf)    |
|02             | 20.10.2017   |[klick](lectures-pdf/lecture02.pdf)    |
|03             | 24.10.2017   |[klick](lectures-pdf/lecture03.pdf)    |
|04             | 27.10.2017   |[klick](lectures-pdf/lecture04.pdf)    |

## Installation
- Latex installieren: (Tex-Live, Miktex)
- Latex-Editor der Wahl installieren (z.B.: IntelliJ + TeXiFy-Plugin)

## PDF erzeugen
* *IntelliJ + TeXiFy-Plugin*: Rechtsklick auf die Tex-Datei, dann auf "Run" klicken. Eine PDF-Datei sollte im *out*-Verzeichnis erscheinen.
Die gerenderte PDF bitte ins `lectures-pdf`-Verzeichnis kopieren, und in der Readme eintragen.

* *Falls `pdflatex` und **Python 3.6** installiert:* Im Rootverzeichnis dieses Projekts folgende Befehle ausführen:

    ```
    cd scripts
    python updater.py all // Erzeugt alle PDFs erneut
    python updater.py 1 // Erzeugt z.B. nur die erste Vorlesungseinheit-PDF
    ```

    Das Script generiert die PDFs und verschiebt sie ins `lectures-pdf` - Verzeichnis.

## Links
- Vorlage: https://komascript.de/node/1692

Inspiration: https://github.com/dipdi/aub-skript

