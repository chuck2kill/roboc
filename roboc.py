# -*-coding:Utf-8 -*

"""Dans ce fichier, nous trouverons le code principal
du jeu roboc"""

import os
from fonctions import *
import pickle
from carte import Carte

# On charge les cartes existantes
cartes = []
contenu = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].lower()
        with open(chemin, "r") as fichier:
            contenu.append(fichier.read())
        cartes.append(nom_carte)
            # Création d'une carte, à compléter

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print(" {} - {}".format(i + 1, carte))

# On demande la carte choisie
nb_cartes = len(cartes)
choix = int(input("Quelle carte choisissez-vous : ?\n"))
if choix < nb_cartes + 1:
    print(contenu[choix - 1])

carte_choisie = "cartes/" + cartes[choix - 1] + ".txt"
carte_sauve = "sauvegarde/" + cartes[choix - 1] + ".txt"


touche = input("Si vous voulez afficher les règles du jeu, appuyez sur r\n"
              "Sinon, appuyez sur Entrée\n").lower()

if touche == "r":
    print(regles())
else:
    with open(carte_choisie, 'r') as carte_lue:
        texte = carte_lue.read()
    enregistrement(texte, carte_sauve)
    print(recup(carte_sauve))

continuer = True

while continuer:
    avancement = deplacement(carte_sauve, carte_choisie)
    print(avancement)
    with open(carte_sauve, "wb") as sauvegarde_en_cours:
        sauvegarde_pickler = pickle.Pickler(sauvegarde_en_cours)
        sauvegarde_pickler.dump(avancement)

"""    avancement1 = list(avancement)
    if "U" not in avancement1:
        continuer = False
    avancement = "".join(avancement1)"""

print("Fin de la partie")

os.system("pause")




# Si il y a une partie sauvegardée, on l'affiche, à compléter



# ...