import matplotlib.pyplot as plt


class Interface:
    """m : colonne (int), n : ligne (int) echelle : espacement (int)"""

    def __init__(self, m, n, echelle):
        self.m = m
        self.n = n
        self.echelle = echelle

    """
       Commence à tracer de en haut à gauche
       Haut et droite positif
       Bas et gauche négatif
    """
    def tracer_grille(self):
        fig, ax = plt.subplots()

        # tracer chaque ligne de haut en bas
        for i in range(self.n + 1):
            y = -i * self.echelle
            ax.plot([0, self.m * self.echelle], [y, y], "r-")
        # tracer chaque colonne de gauche droite
        for j in range(self.m + 1):
            x = j * self.echelle
            ax.plot([x, x], [0, -self.n * self.echelle], "b-")
        # Cadrage du grillage
        ax.set_xlim(-1, (self.m * self.echelle) + 1)
        ax.set_ylim(-1 + (-self.n * self.echelle), 1)
        # Supprimer les graduations sur les axes x et y
        ax.set_xticks([])
        ax.set_yticks([])
        # Enlever le contour du graphique
        ax.axis("off")
        plt.show()


# Exemple d'utilisation
if __name__ == "__main__":
    grille = Interface(
        4, 4, 20
    )  # Une grille de 5 colonnes, 4 lignes, avec une échelle de 20 pixels par unité
    grille.tracer_grille()
