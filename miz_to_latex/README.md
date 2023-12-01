# Miz to Latex
## Outil d'extraction pour briefings DCS World
### Utilisation
* Installer Python (>=3.9)
* Lancer, au choix run.sh (CLI) ou run_gui (Avec interface tkinter)
* Sélectionnez le fichier mission DCS World (.miz) dont il faut extraire le briefing
* Le programme vous demandera ensuite de sauvegarder le fichier .tex (LaTeX) correspondant
* (Facultatif) Le programme pourra vous proposer de trier l'ensemble des fichiers .tex générés dans un dossier "docs" dédié.

### Données extraites
Les deux champs extraits sont :
* Titre de la mission (missionName)
* La description de la mission / Briefing (Briefing Neutre pour l'instant)

### Les codes fonctionnels sont présents dans "final", ou dans les releases.