echo "Lancement du Script"
python script.py
rm -rf dossier_extraction
if [ -d doc ]; then
    rm -r doc
fi
mkdir doc
mv *.tex doc/
echo "Nettoyage et déplacement terminé. Enjoy!"