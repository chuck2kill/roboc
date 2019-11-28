# -*- coding:Utf-8 *-

"""Fichier contenant les différentes fonctions utiles au jeu roboc"""

import pickle

"""fonction affichant les règles du jeu"""
def regles():
    print("Pour vous déplacer, c'est très simple. Voici les touches:\n"
          "n -> se déplacer au nord\n"
          "s -> se déplacer au sud\n"
          "o -> se déplacer à l'ouest\n"
          "e -> se déplacer à l'est\n"
          "n2 -> se déplacer de 2 cases au nord\n"
          "A noter que pour quitter en enregistrant, il faut appuyer sur q\n \n"
          "Vous êtes le 'X' et vous appuyez sur les touches pour\nvous diriger vers la sortie\n"
          "Les '0' sont des murs\n"
          "Les '.' sont des portes\n"
          "Le 'U' est la sortie")

def enregistrement(nom_fichier, fichier_sauve):
    """Cette fonction sert à enregistrer la carte modifiée
    dans le répertoire sauvegarde"""
    with open(fichier_sauve, 'wb') as save:
        mon_pickler = pickle.Pickler(save)
        mon_pickler.dump(nom_fichier)

def recup(fichier_sauve):
    """Cette fonction sert à récupérer la sauvegarde de la carte"""
    with open(fichier_sauve, 'rb') as save2:
        mon_depickler = pickle.Unpickler(save2)
        carte_enregistree = mon_depickler.load()
        return carte_enregistree

def deplacement(carte_sauve, carte_depart):
    """Cette fonction va permettre de déplacer le joueur dans le labyrinthe"""
    # On ouvre le fichier sauvegardé
    with open(carte_sauve, "rb") as provisoire:
        le_depickler = pickle.Unpickler(provisoire)
        carte_provisoire = le_depickler.load()

    # On ouvre la carte de départ
    with open(carte_depart, "r") as depart:
        carte_reference = depart.read()

    # On transforme la variable "carte_provisoire" str en liste
    liste_provisoire = list(carte_provisoire)

    # On transforme la variable "carte_reference" str en liste
    liste_reference = list(carte_reference)

    # On cherche l'index de X
    index_provisoire = liste_provisoire.index("X")

    # On cherche l'index de '\n'
    index_ligne = liste_reference.index("\n")

    # On cherche les indices des 'O' dans la carte de référence
    index_ref = [i for i, e in enumerate(liste_reference) if e == "O"]

    # Déclaration de la variable 'mur' en False (booléen)
    mur = False

    # on récupère la saisie de l'utilisateur pour le déplacement, dans la
    # variable 'lettre'
    lettre = input("Choisissez le déplacement :\n").lower()
    # Si le déplacement choisi tombe sur un mur ('O'), on passe la variable
    # 'mur' à True
    if lettre == "n":
        if (index_provisoire - index_ligne - 1) in index_ref:
            mur = True
    elif lettre == "s":
        if (index_provisoire + index_ligne + 1) in index_ref:
            mur = True
    elif lettre ==  "o":
        if (index_provisoire - 1) in index_ref:
            mur = True
    elif lettre == "e":
        if (index_provisoire + 1) in index_ref:
            mur = True
    else:
        print("Choisissez une direction valide (n, s, e, o)")  # Si le choix de déplacement n'est pas valide

    # Boucle while qui permet le déplacement, si le choix est valide
    while mur is False:
        if lettre == "n":
            liste_reference[liste_reference.index("X")] = " "  # On met l'emplacement de départ de X à vide
            liste_reference[index_provisoire - index_ligne - 1] = "X"  # On inscrit le nouveau X
            carte_sauve1 = "".join(liste_reference)  # On transforme la liste en str
            return carte_sauve1  # On renvoie la valeur à la fonction
        elif lettre == "s":
            liste_reference[liste_reference.index("X")] = " "
            liste_reference[index_provisoire + index_ligne + 1] = "X"
            carte_sauve1 = "".join(liste_reference)
            return carte_sauve1
        elif lettre == "o":
            liste_reference[liste_reference.index("X")] = " "
            liste_reference[index_provisoire - 1] = "X"
            carte_sauve1 = "".join(liste_reference)
            return carte_sauve1
        elif lettre == "e":
            liste_reference[liste_reference.index("X")] = " "
            liste_reference[index_provisoire + 1] = "X"
            carte_sauve1 = "".join(liste_reference)
            return carte_sauve1
    print("Vous ne pouvez pas traverser ce mur !")
    return carte_provisoire  # Si l'utilisteur choisi un mur, on garde la disposition de la dernière sauvegarde

