import os
import random
import time
import pyperclip
from pystyle import Colors, Colorate, Center, Box, Write, System

System.Title("BHL-GEN V3 - BY BHL")

# Configuration des couleurs
couleur_principale = Colors.purple_to_blue
couleur_secondaire = Colors.cyan_to_blue

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class GenerateurCartes:
    SERVICES = {
        "Amazon FR": "generer_amazon",
        "Steam": "generer_steam",
        "PlayStation": "generer_playstation",
        "Google Play": "generer_google_play",
        "iTunes": "generer_itunes",
        "Xbox": "generer_xbox",
        "Nintendo": "generer_nintendo",
        "PayPal": "generer_paypal",
        "Spotify": "generer_spotify",
        "Netflix": "generer_netflix"
    }

    @staticmethod
    def generer_amazon():
        # Format: AMZN-XXXX-XXXX (12 caractères)
        return f"AMZN-{GenerateurCartes.random_part(4)}-{GenerateurCartes.random_part(4)}"

    @staticmethod
    def generer_steam():
        # Format: XXXX-XXXX-XXXX (15 caractères)
        return f"{GenerateurCartes.random_part(4)}-{GenerateurCartes.random_part(4)}-{GenerateurCartes.random_part(4)}"

    @staticmethod
    def generer_playstation():
        # Format: XXXX-XXXX-XXXX (12 caractères)
        return f"{GenerateurCartes.random_part(4)}-{GenerateurCartes.random_part(4)}-{GenerateurCartes.random_part(4)}"

    @staticmethod
    def generer_google_play():
        # Format: XXXXXXXXXX (10 caractères)
        return f"{GenerateurCartes.random_part(10)}"

    @staticmethod
    def generer_itunes():
        # Format: XXXX-XXXX (8 caractères)
        return f"{GenerateurCartes.random_part(4)}-{GenerateurCartes.random_part(4)}"

    @staticmethod
    def generer_xbox():
        # Format: XXXX-XXXX-XXXX (12 caractères)
        return f"{GenerateurCartes.random_part(4)}-{GenerateurCartes.random_part(4)}-{GenerateurCartes.random_part(4)}"

    @staticmethod
    def generer_nintendo():
        # Format: XXXXXXXX (8 caractères)
        return f"{GenerateurCartes.random_part(8)}"

    @staticmethod
    def generer_paypal():
        # Format: XXXXXXXX (8 caractères)
        return f"{GenerateurCartes.random_part(8)}"

    @staticmethod
    def generer_spotify():
        # Format: XXXXXXXXXX (10 caractères)
        return f"{GenerateurCartes.random_part(10)}"

    @staticmethod
    def generer_netflix():
        # Format: XXXXXXXXXXXXXX (14 caractères)
        return f"{GenerateurCartes.random_part(14)}"

    @staticmethod
    def random_part(length):
        return ''.join(random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ23456789', k=length))

    @staticmethod
    def generer_code(service):
        if service in GenerateurCartes.SERVICES:
            generateur = getattr(GenerateurCartes, GenerateurCartes.SERVICES[service])
            return generateur()
        return None

def afficher_banniere():
    banniere = """
    ██████╗ ██╗  ██╗██╗      ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██║  ██║██║     ██╔════╝ ██╔════╝████╗  ██║
    ██████╔╝███████║██║     ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔══██╗██╔══██║██║     ██║   ██║██╔══╝  ██║╚██╗██║
    ██████╔╝██║  ██║███████╗╚██████╔╝███████╗██║ ╚████║
    ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
    """
    print(Colorate.Vertical(couleur_principale, Center.XCenter(banniere)))
    print(Box.DoubleCube("BHL-GEN V3 - BY BHL"))

def menu_principal():
    while True:
        clear()
        afficher_banniere()
        
        options = [
            "1. Générer des codes cadeaux",
            "2. Quitter"
        ]
        
        for option in options:
            print(Colorate.Vertical(couleur_secondaire, Center.XCenter(option)))
        
        choix = input(Colorate.Vertical(couleur_principale, "\n>>> ")).strip()
        
        if choix == "1":
            menu_generation()
        elif choix == "2":
            Write.Print(Center.XCenter("\nMerci d'avoir utilisé BHL-GEN!"), couleur_principale, interval=0.02)
            time.sleep(2)
            exit()

def menu_generation():
    clear()
    afficher_banniere()
    
    print(Colorate.Vertical(couleur_principale, Center.XCenter("=== SERVICES DISPONIBLES ===")))
    
    services = list(GenerateurCartes.SERVICES.keys())
    for i, service in enumerate(services, 1):
        print(Colorate.Vertical(couleur_secondaire, Center.XCenter(f"{i}. {service}")))
    
    print(Colorate.Vertical(couleur_principale, Center.XCenter("\n0. Retour")))
    
    while True:
        try:
            choix = int(input(Colorate.Vertical(couleur_principale, "\nService >>> ")))
            if choix == 0:
                return
            elif 1 <= choix <= len(services):
                service_selectionne = services[choix-1]
                generer_et_afficher(service_selectionne)
                break
            else:
                Write.Print(Center.XCenter("Choix invalide!"), Colors.red_to_yellow, interval=0.02)
        except ValueError:
            Write.Print(Center.XCenter("Entrez un nombre!"), Colors.red_to_purple, interval=0.02)

def generer_et_afficher(service):
    clear()
    afficher_banniere()
    
    print(Colorate.Vertical(couleur_principale, Center.XCenter(f"=== GENERATION {service.upper()} ===")))
    
    try:
        quantite = int(input(Colorate.Vertical(couleur_secondaire, "Nombre de codes à générer (1-1000): ")))
        quantite = max(1, min(1000, quantite))
    except:
        quantite = 1
    
    print("\n")
    Write.Print(Center.XCenter(f"Génération de {quantite} codes {service}...\n"), couleur_principale, interval=0.01)
    
    codes = []
    for _ in range(quantite):
        code = GenerateurCartes.generer_code(service)
        codes.append(code)
        print(Colorate.Vertical(Colors.rainbow, Center.XCenter(f"[+] {code}")))
        time.sleep(0.1)
    
    print("\n")
    Write.Print(Center.XCenter("Génération terminée!\n"), Colors.green_to_blue, interval=0.02)
    
    copier = input(Colorate.Vertical(couleur_secondaire, "Copier les codes dans le presse-papiers? (o/n): ")).lower()
    if copier == 'o':
        pyperclip.copy("\n".join(codes))
        Write.Print(Center.XCenter("Codes copiés dans le presse-papiers!"), Colors.green_to_yellow, interval=0.02)
    
    input(Colorate.Vertical(couleur_principale, "\nAppuyez sur Entrée pour continuer..."))

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        Write.Print(Center.XCenter("\nInterruption par l'utilisateur"), Colors.red_to_purple, interval=0.02)
        exit()
