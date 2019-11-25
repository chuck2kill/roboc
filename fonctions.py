# -*- coding:Utf-8 *-

"""Fichier contenant les différentes fonctions utiles au jeu roboc"""

import os
import pickle

def creer_labyrinthe_depuis_chaine(chaine):
    pass

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
    """Cette fonction sert à enregistrer la carte modifiée"""
    with open(fichier_sauve, 'wb') as save:
        mon_pickler = pickle.Pickler(save)
        mon_pickler.dump(nom_fichier)

def recup(fichier_sauve):
    with open(fichier_sauve, 'rb') as save2:
        mon_depickler = pickle.Unpickler(save2)
        carte_enregistree = mon_depickler.load()
        return carte_enregistree

def deplacement(carte_sauve, carte_depart):
    """Cette fonction va permettre de déplacer le joueur dans le labyrinthe"""
    # On ouvre le fichier
    with open(carte_sauve, "rb") as provisoire:
        le_depickler = pickle.Unpickler(provisoire)
        carte_provisoire = le_depickler.load()

    # On ouvre la carte
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

    lettre = input("Choisissez le déplacement :\n").lower()
    if lettre == "n":
        liste_reference[index_provisoire - index_ligne - 1] = "X"
        liste_reference[liste_reference.index("X")] = " "
        carte_sauve1 = "".join(liste_reference)
        return carte_sauve1
    elif lettre == "s":
        liste_reference[index_provisoire + index_ligne + 1] = "X"
        liste_reference[liste_reference.index("X")] = " "
        carte_sauve1 = "".join(liste_reference)
        return carte_sauve1
    elif lettre == "o":
        liste_reference[index_provisoire - 1] = "X"
        liste_reference[liste_reference.index("X")] = " "
        carte_sauve1 = "".join(liste_reference)
        return carte_sauve1
    elif lettre == "e":
        liste_reference[index_provisoire + 1] = "X"
        liste_reference[liste_reference.index("X")] = " "
        carte_sauve1 = "".join(liste_reference)
        return carte_sauve1
    else:
        print("Choisissez une direction valide (n, s, e, o")
