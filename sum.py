import sys

def additionner(arg1, arg2):
    """ 
    Additionne deux nombres et retourne le résultat.

    :param arg1: Premier nombre à additionner (float)
    :param arg2: Deuxième nombre à additionner (float)
    :return: La somme de arg1 et arg2 (float)
    """
    return arg1 + arg2

def main():
    """
    Script principal pour lire les arguments de la ligne de commande,
    vérifier leur validité et afficher le résultat de la somme.

    :raises ValueError: Si les arguments fournis ne peuvent pas être convertis en float.
    :raises SystemExit: Si le nombre d'arguments est incorrect.
    """
    # Vérifier si deux arguments sont fournis
    if len(sys.argv) != 3:
        print("Erreur : Deux arguments sont nécessaires.")
        sys.exit(1)

    # Interpréter les arguments
    try:
        arg1 = float(sys.argv[1])
        arg2 = float(sys.argv[2])
    except ValueError:
        print("Erreur : Les arguments doivent être des nombres.")
        sys.exit(1)

    # Calculer la somme et afficher le résultat
    resultat = additionner(arg1, arg2)
    print(resultat)

if __name__ == "__main__":
    main()
