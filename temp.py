class Grille:
    def __init__(self, longueur, hauteur, tableau):
        self.longueur = longueur
        self.hauteur = hauteur
        self.tableau = []
        self.num_actuel = 0
        
    def creer_tableau(self):
        pass
    
    def obtenir_l(self):
        pass
        
    def obtenir_h(self):
        pass
        
    def est_vide(self):
        """Vérifie si le tableau est vide 
            Retourne un booléen"""
        
        for i in range(self.hauteur):
            for j in range(self.longueur):
                if self.tableau[i][j] != 0:
                    return False
        return True
    
    def choisir_trimino(self, coordonnees, type_tuile):
        """ """
        pass
    
    def verifier_tableau(self):
        """Verifier si il y a de la place pour ajouter un trimino 
            Retourne un booléen
        """

        
    
    def ajouter_tuile(self, tuile):
        """Ajouter une tuile au tableau d'après ses coordonnées
            tuile : liste de tuple , numero_tuile : int  """
            
        self.num_actuel += 1
        
        for x_y in tuile:
            self.tableau[x_y[0]][x_y[1]] = self.num_actuel
    
    def obtenir_tuile(self, num_tuile):
        """Obtenir les coordonées de la tuile numero_tuile
            num_tuile : int
            renvoie une liste de tuple des coordonées x y de la tuile numero_tuile
        """
        if num_tuile> self.num_actuel:
            return []
        
        coordonnees = []
        
        for i in range(self.hauteur):
            for j in range(self.longueur):
                if self.tableau[i][j] == num_tuile:
                    coordonnees.append((i,j))
                    
        return coordonnees
    
    def enlever_tuile(self):
        
        for i in range(self.hauteur):
            for j in range(self.longueur):
                if self.tableau[i][j] == self.num_actuel:
                    self.tableau[i][j] = 0
                    
        self.num_actuel -= 1
        

                    
        
     