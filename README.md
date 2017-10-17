# AuB 17-18
Notes of lecture AuB17/18. From students for students. Using Markdown and Latex with Pandoc.

### Installation
1. Latex installieren: (Tex-Live, Miktex)
2. Pandoc installieren: (Debian-Derivate: `sudo apt-get install pandoc`)

### Empfohlene Programme und Plugins
* IntelliJ
* IntelliJ Plugins (TeXiFy Idea, Markdown Navigator)

### PDF aus Markdown erzeugen
Im Root Directory das Terminal öffnen: 

`pandoc -H configuration/preamble.tex configuration/default.yaml lectures-md/lecture01.md -o lectures-pdf/lecture01.pdf`

Pandoc erzeugt mit den beiden Inputparamtern *preamble.tex* und *default.yaml* aus dem **configuration** Verzeichnis aus der Quelldatei *lectures01.md* im **lectures-md** Verzeichnis eine PDF Datei, die im **lectures-pdf** Verzeichnis abegelegt wird.

### Anpassungen
Im Verzeichnis **configuration** befinden sich *preamble.tex* und *default.yaml*.

In *default.yaml* können Paramter eingestellt werden, Latex-Pakete bitte in *preamble.tex* einbinden. Sofern wirs nicht übertreiben, sollte es damit hinhauen.

### Links
* https://www.soimort.org/notes/161117/
* https://daringfireball.net/projects/markdown/syntax (Thx Alex)
* http://kesdev.com/you-got-latex-in-my-markdown/
* https://guides.github.com/features/mastering-markdown/

Inspiration: https://github.com/dipdi/aub-skript

