@echo off
setlocal

REM Récupérer le chemin complet du fichier bat
set "script_path=%~dp0"

REM Lire l'adresse IP depuis le fichier whereiam.txt
set /p local_ip=<"%script_path%whereiam.txt"

REM Lancer le serveur HTTP en arrière-plan
start /B python -m http.server --bind %local_ip% 80

REM Attendre indéfiniment
