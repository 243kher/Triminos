import matplotlib.pyplot as plt
import random
from Grille import Grille


class Interface(Grille):
    """
    Classe Interface qui hérite des méthodes et attributs de Grille
    Ceci va nous permettre de dessiner des triminos dans des cases plus facilement
    sans dédoubler notre code.
    longueur : colonne (int), hauteur : ligne (int) echelle : espacement (int)
    """

    def __init__(self, longueur, hauteur, echelle):
        super().__init__(self, longueur, hauteur)
        self.longueur = longueur
        self.hauteur = hauteur
        self.echelle = echelle
        self.couleurs = {}

        self.creer_tableau()
        self.fig, self.ax = plt.subplots()
        self.tracer_grille()

    """
       Commence à tracer de en haut à gauche
       Haut et droite positif
       Bas et gauche négatif
    """

    def tracer_grille(self):
        # Tracer chaque ligne de haut en bas
        for i in range(self.hauteur + 1):
            y = -i * self.echelle
            self.ax.plot([0, self.longueur * self.echelle], [y, y], "r-")
        # Tracer chaque colonne de gauche droite
        for j in range(self.longueur + 1):
            x = j * self.echelle
            self.ax.plot([x, x], [0, -self.hauteur * self.echelle], "b-")
        # Cadrage du grillage
        self.ax.set_xlim(-1, (self.longueur * self.echelle) + 1)
        self.ax.set_ylim(-1 + (-self.hauteur * self.echelle), 1)
        # Supprimer les graduations sur les axes x et y
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        # Enlever le contour du graphique
        self.ax.axis("off")
        # Met en ratio égal le graphique
        self.ax.set_aspect("equal")

        # Mets à jours le graphique
        self.fig.canvas.draw()

    def couleur_au_pif(self):
        """Génere une couleur aléatoirement"""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def remplir_tuile(self, x, y):
        """Remplit une tuile de position (x,y) d'une couleur ..."""
        couleur = self.couleur_au_pif()

        self.couleurs[(x, y)] = couleur
        self.update_couleurs()

    def update_couleurs(self):
        """Mets à jours les couleurs de la tuiles"""

        # Remplie chaque tuile d'apres ces quatres coordonnées en haut à gauche , en haut à droite, en bas à gauche, en bas à droite
        for tile, color in self.couleurs.items():
            x, y = tile
            self.ax.fill(
                [
                    x * self.echelle,
                    (x + 1) * self.echelle,
                    (x + 1) * self.echelle,
                    x * self.echelle,
                ],
                [
                    -(y * self.echelle),
                    -(y * self.echelle),
                    -((y + 1) * self.echelle),
                    -((y + 1) * self.echelle),
                ],
                color=color,
            )

        self.fig.canvas.draw()


# Exemple d'utilisation
if __name__ == "__main__":
    grille = Interface(
        5, 4, 20
    )  # Une grille de 5 colonnes, 4 lignes, avec une échelle de 20 pixels par unité

    grille.remplir_tuile(1, 3)
    grille.remplir_tuile(2, 2)

    plt.show()
