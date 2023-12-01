echo "Lancement du Script"
python run_gui.py
rm -rf dossier_extraction
if [ -d docs ]; then
    rm -r docs
fi

read -p "Voulez-vous créer le dossier 'docs' pour déplacer les fichiers .tex? (y/n): " response

# Vérifie la réponse de l'utilisateur
if [ "$response" == "y" ]; then
    # Supprime le dossier 'docs' s'il existe déjà
    if [ -d docs ]; then
        rm -r docs
    fi

    # Crée le dossier 'docs'
    mkdir docs

    # Déplace tous les fichiers .tex dans le dossier 'docs'
    mv *.tex docs/
    echo "Les fichiers .tex ont été déplacés dans le dossier 'docs'."
else
    echo "Aucun dossier 'docs' n'a été créé. Les fichiers .tex n'ont pas été déplacés."
fi

echo "Nettoyage et déplacement terminé. Enjoy!"