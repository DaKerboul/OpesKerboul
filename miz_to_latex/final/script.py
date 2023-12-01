import zipfile
import os
import re

fichier_miz= 'mission.miz'
dossier_extraction='dossier_extraction'

with zipfile.ZipFile(fichier_miz, 'r') as zip_ref:
    zip_ref.extractall(dossier_extraction)

chemin_fichier_dictionary = os.path.join(dossier_extraction, 'l10n', 'DEFAULT', 'dictionary')

with open(chemin_fichier_dictionary, 'r', encoding='utf-8') as file:
    contenu = file.read()

# Utilisation de regex pour extraire les informations spécifiques
pattern_mission_name = r'\["DictKey_missionName"\]\s*=\s*"([^"]*)"'
pattern_editor_notes = r'\["DictKey_briefing"\]\s*=\s*"([^"]*)"'

match_mission_name = re.search(pattern_mission_name, contenu)
match_editor_notes = re.search(pattern_editor_notes, contenu)

if match_editor_notes and match_mission_name:
    mission_name = match_mission_name.group(1).replace('\\', '\\\\')  # Remplacer les "\" par "\\"
    editor_notes = match_editor_notes.group(1).replace('\\', '\\\\')

    nom_fichier_latex = input("Entrez le nom du fichier LaTeX de sortie (sans extension): ")

    contenu_latex = f"""
        \\documentclass{{article}}
        \\title{{{mission_name}}}
        \\begin{{document}}
    
        \\maketitle
    
        \\section{{Editor Notes}}
        {editor_notes}
    
        \\end{{document}}
        """
    chemin_fichier_latex = f"{nom_fichier_latex}.tex"
    with open(chemin_fichier_latex, 'w', encoding='utf-8') as latex_file:
        latex_file.write(contenu_latex)
    print(f"Le fichier LaTeX a été créé avec succès : {chemin_fichier_latex}")
else:
    print("Les entrées spécifiées n'ont pas été trouvées dans le fichier dictionary.")