import copy

# Base des faits (globale)
faits = []
# Base des règles (globale)
regles = []

def initDBs():
    """Réinitialise les bases de faits et règles"""
    global faits, regles
    faits = []
    regles = [] 

def afficher_faits():
    """Affiche le contenu de la base de faits"""
    print("\nBase des faits actuelle:")
    if not faits:
        print("(Vide)")
    else:
        for i, fait in enumerate(faits, 1):
            print(f"{i}. {fait}")

def ajouter_fait(nouveau_fait):
    """Ajoute un fait à la base avec copie profonde"""
    global faits
    # Crée une copie indépendante de l'objet
    copie_fait = copy.deepcopy(nouveau_fait)  
    faits.append(copie_fait)
    print(f"Fait ajouté: {nouveau_fait}")

# Exemple d'utilisation
if __name__ == "__main__":
    initDBs()
    
    while True:
        print("\nMenu:")
        print("1. Afficher la base des faits")
        print("2. Ajouter un fait")
        print("3. Quitter")
        
        choix = input("Votre choix (1-3): ")
        
        if choix == "1":
            afficher_faits()
        elif choix == "2":
            fait = input("Entrez le fait à ajouter: ")
            ajouter_fait(fait)
        elif choix == "3":
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")