Set objShell = CreateObject("WScript.Shell")

' Chemin vers le fichier batch pour lancer le script Python et le serveur HTTP
batchFile = "launch.bat"

' Exécute le fichier batch en arrière-plan sans afficher la fenêtre de commande
objShell.Run "cmd.exe /c """"" & batchFile & """", 0, False
