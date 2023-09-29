class Grille:
    def __init__(self, longueur, hauteur, tableau=[]):
        self.longueur = longueur
        self.hauteur = hauteur
        self.tableau = tableau
        self.num_actuel = 0
        self.format_tuile = [
            [(1, 0), (0, -1)], [(1, 0), (0, 1)], [(-1, 0), (0, 1)], [(-1, 0), (0, -1)]]

    def creer_tableau(self):
        """
        Méthode qui créer un tableau (list)
        initialisé selon les attributs longueur(int) et hauteur(int) de l'objet
        """

        self.tableau = [[0 for x in range(self.longueur)]
                        for y in range(self.hauteur)]

    def est_vide(self):
        """
        Méthode qui retourne un booléen si le tableau est vide
        """

        for y in range(self.hauteur):
            for x in range(self.longueur):
                if self.tableau[y][x] != 0:
                    return False
        return True

    def choisir_trimino(self, coordonnees, type_tuile):
        """ 
        Méthode qui retourne une liste de coordonnées tuple d'une tuile selon la coordonné choisie et son type
        Type 0: L ;Type 1: Г ;Type 2: ꓶ ;Type 3: ⅃
        la case de coordonnées (x, y) représente en colonne x et en ligne y.
        premiere coordonée d'après l'angle puis horizontale et vertical
        """
        return [coordonnees, (coordonnees[0]+self.format_tuile[type_tuile][0][0], 
                            coordonnees[1]+self.format_tuile[type_tuile][0][1]), 
                            (coordonnees[0]+self.format_tuile[type_tuile][1][0], 
                            coordonnees[1]+self.format_tuile[type_tuile][1][1])
                            ]

        

    def liste_vide(self):
        liste_vide = []
        for y in range(self.hauteur):
            for x in range(self.longueur):
                if self.tableau[y][x] == 0:
                    liste_vide.append((x, y))
        return liste_vide

    def verifier_tuile_vide(self, liste_vide):
        for t in liste_vide:
            if (t[0], t[1] - 1) in liste_vide and (t[0] - 1, t[1]) in liste_vide:
                return True
            if (t[0] - 1, t[1]) in liste_vide and (t[0] + 1, t[1]) in liste_vide:
                return True
            if (t[0] + 1, t[1]) in liste_vide and (t[0], t[1] + 1) in liste_vide:
                return True
            if (t[0], t[1] + 1) in liste_vide and (t[0], t[1] - 1) in liste_vide:
                return True
        return False

    def verifier_tableau(self):
        """
        Méthode qui verifier si il y a de la place pour ajouter un trimino
        Retourne un booléen
        """
        pass

    def ajouter_tuile(self, tuile):
        """
        Méthode qui ajoute une tuile au tableau d'après ses coordonnées
            tuile : liste de tuple de coordonées (x,y)
        """

        self.num_actuel += 1

        for x_y in tuile:
            self.tableau[x_y[1]][x_y[0]] = self.num_actuel

    def obtenir_tuile(self, num_tuile):
        """
        Méthode qui obtient les coordonées de la tuile 'num_tuile'
        num_tuile : int
        renvoie une liste de tuple de coordonées (x,y) de la tuile 'num_tuile'
        """
        if num_tuile > self.num_actuel:
            return []

        coordonnees = []

        for y in range(self.hauteur):
            for x in range(self.longueur):
                if self.tableau[y][x] == num_tuile:
                    coordonnees.append((x, y))

        return coordonnees

    def enlever_tuile(self):
        """
        Méthode qui enlève la dernière tuile posée
        """

        for y in range(self.hauteur):
            for x in range(self.longueur):
                if self.tableau[y][x] == self.num_actuel:
                    self.tableau[y][x] = 0

        self.num_actuel -= 1

    def __str__(self):
        """
        Affiche une belle matrice
        """

        line = "-" + "-" * 4 * self.longueur + "\n"
        s = line
        for l in self.tableau:
            s += "| "
            for x in l:
                s += str(x) + " | "
            s += "\n" + line
        return s

    def obtenir_l(self):
        return self.longueur

    def obtenir_h(self):
        return self.hauteur


if __name__ == "__main__":
    print(Grille(6,5))