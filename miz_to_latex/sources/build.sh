#!/bin/bash

cp run_gui.py ../build/
pyinstaller --onefile --noconsole run_gui.py
rm build
cp -r dist/run_gui.exe ../build/
pdflatex -interaction=batchmode -halt-on-error -output-directory="../build/" ../docs/doc_release.tex
rm ../build/doc_release.aux
rm ../build/doc_release.log
zip -r kerboul_Miz_To_Latex_1.1.0.zip ../build/
mv kerboul_Miz_To_Latex_1.1.0.zip ../release