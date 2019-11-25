# -*-coding:Utf-8 -*

"""Ce module contient la classe labyrinthe"""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = {}
