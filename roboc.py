# -*-coding:Utf-8 -*

"""Dans ce fichier, nous trouverons le code principal
du jeu roboc"""

import os
from fonctions import *
import pickle

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

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print(" {} - {}".format(i + 1, carte))

# On demande la carte choisie
nb_cartes = len(cartes)

# On teste pour que la variable entrée soit de type int et qu'elle soit dans le bon intervalle
while True:
    try:
        choix = int(input("Quelle carte choisissez-vous : ?\n"))
        assert choix < nb_cartes + 1
        break
    except ValueError:
        print("Entrez un nombre s'il vous-plaît")
    except AssertionError:
        print("Vous devez choisir un chiffre entre 1 et {}".format(nb_cartes))

carte_choisie = "cartes/" + cartes[choix - 1] + ".txt"
carte_sauve = "sauvegarde/" + cartes[choix - 1] + ".txt"


touche = input("Si vous voulez afficher les règles du jeu, appuyez sur r\n"
              "Sinon, appuyez sur Entrée\n").lower()

if touche == "r":
    print(regles())

# On vérifie si une partie est sauvegardée

if os.path.exists(carte_sauve):
    partie_sauvee = input("Une partie est en cours, voulez-vous la reprendre (o/n)").lower()
    if partie_sauvee == "o":
        print(recup(carte_sauve))  # On charge la sauvegarde
    else:
        with open(carte_choisie, 'r') as carte_lue:
            texte = carte_lue.read()
        enregistrement(texte, carte_sauve)
        print(recup(carte_sauve))
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
    fin = list(avancement)
    if "U" not in fin:
        continuer = False
    fin = "".join(fin)

print("Fin de la partie")
os.remove(carte_sauve)

os.system("pause")