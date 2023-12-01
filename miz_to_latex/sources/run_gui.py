import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import zipfile
import os
import re


def extraire_et_creer_latex():
    # Demander à l'utilisateur de sélectionner le fichier .miz
    fichier_miz = filedialog.askopenfilename(filetypes=[("Fichiers .miz", "*.miz")])

    if fichier_miz:
        # Créer un dossier temporaire
        dossier_extraction = 'dossier_extraction'
        with zipfile.ZipFile(fichier_miz, 'r') as zip_ref:
            zip_ref.extractall(dossier_extraction)

        # Trouver le chemin du fichier dictionary à l'intérieur du dossier temporaire
        chemin_fichier_dictionary = os.path.join(dossier_extraction, 'l10n', 'DEFAULT', 'dictionary')

        with open(chemin_fichier_dictionary, 'r', encoding='utf-8') as file:
            contenu = file.read()

        # Utilisation de regex pour extraire les informations spécifiques
        pattern_mission_name = r'\["DictKey_missionName"\]\s*=\s*"([^"]*)"'
        pattern_editor_notes = r'\["DictKey_briefing"\]\s*=\s*"([^"]*)"'

        match_mission_name = re.search(pattern_mission_name, contenu)
        match_editor_notes = re.search(pattern_editor_notes, contenu)

        if match_editor_notes and match_mission_name:
            mission_name = match_mission_name.group(1).replace('\\', '\\\\')
            editor_notes = match_editor_notes.group(1).replace('\\', '\\\\')

            # Demander à l'utilisateur le nom du fichier LaTeX de sortie
            nom_fichier_latex = filedialog.asksaveasfilename(defaultextension=".tex",
                                                             filetypes=[("Fichiers LaTeX", "*.tex")])

            if nom_fichier_latex:
                # Création du contenu LaTeX
                contenu_latex = f"""
                    \\documentclass{{article}}
                    \\title{{{mission_name}}}
                    \\begin{{document}}

                    \\maketitle

                    \\section{{Editor Notes}}
                    {editor_notes}

                    \\end{{document}}
                    """

                # Enregistrement du fichier LaTeX
                with open(nom_fichier_latex, 'w', encoding='utf-8') as latex_file:
                    latex_file.write(contenu_latex)

                messagebox.showinfo("Succès", f"Le fichier LaTeX a été créé avec succès : {nom_fichier_latex}")
            else:
                messagebox.showwarning("Attention", "Aucun nom de fichier LaTeX spécifié.")
        else:
            messagebox.showwarning("Attention",
                                   "Les entrées spécifiées n'ont pas été trouvées dans le fichier dictionary.")
    else:
        messagebox.showwarning("Attention", "Aucun fichier .miz spécifié.")


# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Extraction et création LaTeX")

# Ajouter un bouton pour déclencher le processus
bouton_extraction = tk.Button(fenetre, text="Extraire et créer LaTeX", command=extraire_et_creer_latex)
bouton_extraction.pack(padx=20, pady=20)

# Ajouter un bouton pour quitter
bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(padx=20, pady=20)

# Lancer la boucle principale de l'interface graphique
fenetre.mainloop()