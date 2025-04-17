import copy

# Shared databases (same as Exercise 1)
faits = []
regles = []

def initDBs():
    """Reinitialize both fact and rule databases"""
    global faits, regles
    faits = []
    regles = []

# --- RULE MANAGEMENT FUNCTIONS ---

def afficher_regles():
    """1. Display all rules in the rule base"""
    print("\nBase des règles actuelle:")
    if not regles:
        print("(Vide)")
    else:
        for i, regle in enumerate(regles, 1):
            print(f"{i}. Conditions: {regle[0]} → Conséquence: {regle[1]}")

def ajouter_regle(conditions, consequence):
    """2. Add a new rule to the rule base with deep copy"""
    global regles
    new_regle = [copy.deepcopy(conditions), copy.deepcopy(consequence)]
    regles.append(new_regle)
    print(f"Règle ajoutée: {conditions} → {consequence}")

def get_conditions(rule_index):
    """3. Return conditions of a specific rule"""
    if 0 <= rule_index < len(regles):
        return regles[rule_index][0]
    return None

def get_consequence(rule_index):
    """4. Return consequence of a specific rule"""
    if 0 <= rule_index < len(regles):
        return regles[rule_index][1]
    return None

def condition_satisfaite(fait, rule_index):
    """5. Check if a given fact satisfies any condition of a rule"""
    conditions = get_conditions(rule_index)
    if conditions:
        return fait in conditions
    return False

def toutes_conditions_satisfaites(rule_index):
    """6. Check if ALL conditions of a rule are satisfied by the fact base"""
    conditions = get_conditions(rule_index)
    if not conditions:
        return False
    return all(cond in faits for cond in conditions)

# --- INTERACTIVE MENU ---
if __name__ == "__main__":
    initDBs()
    
    # Sample initial data
    ajouter_regle(['fait1', 'fait2'], 'conclusion1')
    ajouter_regle(['fait3', 'fait4'], 'conclusion2')
    faits.extend(['fait1', 'fait3'])  # Add some facts for testing

    while True:
        print("\nMenu Règles:")
        print("1. Afficher la base des règles")
        print("2. Ajouter une règle")
        print("3. Voir les conditions d'une règle")
        print("4. Voir la conséquence d'une règle")
        print("5. Vérifier si un fait satisfait une condition")
        print("6. Vérifier si toutes les conditions sont satisfaites")
        print("7. Quitter")
        
        choix = input("Votre choix (1-7): ")
        
        if choix == "1":
            afficher_regles()
        elif choix == "2":
            conds = input("Entrez les conditions (séparées par des virgules): ").split(',')
            cons = input("Entrez la conséquence: ")
            ajouter_regle([c.strip() for c in conds], cons.strip())
        elif choix == "3":
            idx = int(input("Numéro de la règle: ")) - 1
            print(f"Conditions: {get_conditions(idx)}")
        elif choix == "4":
            idx = int(input("Numéro de la règle: ")) - 1
            print(f"Conséquence: {get_consequence(idx)}")
        elif choix == "5":
            f = input("Entrez le fait à vérifier: ")
            idx = int(input("Numéro de la règle: ")) - 1
            print("Satisfait?" , "Oui" if condition_satisfaite(f, idx) else "Non")
        elif choix == "6":
            idx = int(input("Numéro de la règle: ")) - 1
            print("Toutes satisfaites?" , "Oui" if toutes_conditions_satisfaites(idx) else "Non")
        elif choix == "7":
            print("Au revoir!")
            break
        else:
            print("Choix invalide!")