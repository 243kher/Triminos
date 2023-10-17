class Grille:
    def __init__(self, longueur, hauteur, tableau=[]):
        """
        Initialise une instance de la classe Grille avec une longueur, une hauteur et un tableau.

        longueur: La longueur de la grille (nombre de colonnes).
        hauteur: La hauteur de la grille (nombre de lignes).
        tableau: Le tableau représentant la grille (par défaut vide).
        """
        self.longueur = longueur
        self.hauteur = hauteur
        self.tableau = tableau
        self.num_actuel = 1
        self.format_tuile = [
            [(1, 0), (0, -1)],
            [(1, 0), (0, 1)],
            [(-1, 0), (0, 1)],
            [(-1, 0), (0, -1)],
        ]

    def creer_tableau(self):
        """
        Méthode qui créer un tableau (list)
        initialisé selon les attributs longueur(int) et hauteur(int) de l'objet
        """

        self.tableau = [[0 for x in range(self.longueur)] for y in range(self.hauteur)]

    def est_vide(self):
        """
        Méthode qui retourne True si le tableau est vide, False sinon.

        """

        for y in range(self.hauteur):
            for x in range(self.longueur):
                if self.tableau[y][x] != 0:
                    return False
        return True

    def choisir_trimino(self, coordonnees, type_tuile):
        """
        Méthode qui retourne une liste de coordonnées tuple d'une tuile selon la coordonné choisie et son type
        Type 1: L ;Type 2: Г ;Type 3: ꓶ ;Type 4: ⅃
        la case de coordonnées (x, y) représente en colonne x et en ligne y.
        premiere coordonée d'après l'angle puis horizontale et vertical
        """
        return [
            coordonnees,
            (
                coordonnees[0] + self.format_tuile[type_tuile][0][0],
                coordonnees[1] + self.format_tuile[type_tuile][0][1],
            ),
            (
                coordonnees[0] + self.format_tuile[type_tuile][1][0],
                coordonnees[1] + self.format_tuile[type_tuile][1][1],
            ),
        ]

    def cases_vide(self):
        """
        Méthode qui retourne une liste des coordonnées des cases vides dans le tableau.
        """
        liste_vide = []
        for y in range(self.hauteur):
            for x in range(self.longueur):
                if self.tableau[y][x] == 0:
                    liste_vide.append((x, y))
        return liste_vide

    def verifier_tuile_vide(self):
        """
        Méthode qui vérifie si une tuile peut être placée dans des cases vides adjacentes.

        liste_vide: La liste des coordonnées des cases vides.
        return: True si une tuile peut être placée, False sinon.
        """
        liste_vide = self.cases_vide()
        for t in liste_vide:
            for k in range(4):
                if (
                    t[0] + self.format_tuile[k][0][0],
                    t[1] + self.format_tuile[k][0][1],
                ) in liste_vide and (
                    t[0] + self.format_tuile[k][1][0],
                    t[1] + self.format_tuile[k][1][1],
                ) in liste_vide:
                    return True

        return False

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
        et retourne les coordonées de la tuile enlevé
        """
        if self.num_actuel > 1:
            liste_coord_triminos = []

            for y in range(self.hauteur):
                for x in range(self.longueur):
                    if self.tableau[y][x] == self.num_actuel - 1:
                        self.tableau[y][x] = 0
                        liste_coord_triminos.append((x, y))

            self.num_actuel -= 1
            return liste_coord_triminos

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

    def ajouter_tuile(self, x, y, type_tuile):
        """
        Méthode qui tente d'ajouter une tuile au tableau à partir des coordonnées spécifiées et du type de tuile.

        x: La coordonnée x de la case où la tuile sera ajoutée.
        y: La coordonnée y de la case où la tuile sera ajoutée.
        type_tuile: Le type de tuile à ajouter.
        return: True si l'ajout est possible, False sinon.
        """
        if x < 0 or x >= self.longueur or y < 0 or y >= self.hauteur:
            return False
        tuile_coordonnees = self.choisir_trimino((x, y), type_tuile)

        for x, y in tuile_coordonnees:
            if (
                x < 0
                or x >= self.longueur
                or y < 0
                or y >= self.hauteur
                or self.tableau[y][x] != 0
            ):
                return False

        for x, y in tuile_coordonnees:
            self.tableau[y][x] = self.num_actuel

        self.num_actuel += 1
        return True

    def obtenir_l(self):
        """
        Méthode qui retourne la longueur de la grille.
        """
        return self.longueur

    def obtenir_h(self):
        """
        Méthode qui retourne la hauteur de la grille.
        """
        return self.hauteur

    def est_pavable(self):
        """Méthode qui vérifie que la grille est pavable"""
        return (
            (self.longueur * self.hauteur) % 3
        ) == 0  # Comme on pose des figures qui sont composées de 3 pavés il faut vérifier que notre quadrillage peut être recouvert de figures"""
        
    def avoir_num_actuel(self):
        max = 0
        for y in range(self.hauteur):
            for x in range(self.longueur):
                if self.tableau[y][x] > max:
                    max = self.tableau[y][x]
        self.num_actuel = max+1

    def paver_recursif_une_solution(self):
        if self.est_pavable():
            if not self.verifier_tuile_vide():
                if self.cases_vide() == []:
                    return self.tableau

            for x, y in self.cases_vide():
                for type_tuile in range(4):
                    if self.ajouter_tuile(x, y, type_tuile):
                        if self.paver_recursif_une_solution():
                            return True
                        self.enlever_tuile()

            return False

    def paver_recursif_toutes_solutions(self, solutions=[]):
        if self.est_pavable():
            if not self.verifier_tuile_vide():
                if self.cases_vide() == []:
                    tableau = [[elm for elm in ligne] for ligne in self.tableau]
                    grille = Grille(self.longueur, self.hauteur, tableau)
                    solutions.append(grille)
                    return

            for x, y in self.cases_vide():
                for type_tuile in range(4):
                    if self.ajouter_tuile(x, y, type_tuile):
                        self.paver_recursif_toutes_solutions(solutions)
                        self.enlever_tuile()


if __name__ == "__main__":
    grille = Grille(3, 4)
    grille.creer_tableau()
    print(grille)

    print(grille.est_pavable())
