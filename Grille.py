class Grille:
    def __init__(self, longueur, hauteur, tableau=[]):
        self.longueur = longueur
        self.hauteur = hauteur
        self.tableau = tableau
        self.num_actuel = 0

    def creer_tableau(self):
        """
        Méthode qui créer un tableau (list)
        initialisé selon les attributs longueur(int) et hauteur(int) de l'objet
        """

        self.tableau = [[0 for j in range(self.longueur)]
                        for i in range(self.hauteur)]

    def est_vide(self):
        """
        Méthode qui retourne un booléen si le tableau est vide
        """

        for i in range(self.hauteur):
            for j in range(self.longueur):
                if self.tableau[i][j] != 0:
                    return False
        return True

    def choisir_trimino(self, coordonnees, type_tuile):
        """ """
        pass

    def liste_vide(self):
        liste_vide = []
        for t in range(self.hauteur):
            for i in range(self.longueur):
                if self.tableau[t][i] == 0:
                    liste_vide.append((t, i))
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
            self.tableau[x_y[0]][x_y[1]] = self.num_actuel

    def obtenir_tuile(self, num_tuile):
        """
        Méthode qui obtient les coordonées de la tuile 'num_tuile'
        num_tuile : int
        renvoie une liste de tuple de coordonées (x,y) de la tuile 'num_tuile'
        """
        if num_tuile > self.num_actuel:
            return []

        coordonnees = []

        for i in range(self.hauteur):
            for j in range(self.longueur):
                if self.tableau[i][j] == num_tuile:
                    coordonnees.append((i, j))

        return coordonnees

    def enlever_tuile(self):
        """
        Méthode qui enlève la dernière tuile posée
        """

        for i in range(self.hauteur):
            for j in range(self.longueur):
                if self.tableau[i][j] == self.num_actuel:
                    self.tableau[i][j] = 0

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


t = Grille(5, 6)

t.creer_tableau()

print(t)
