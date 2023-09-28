# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Grille:
    def __init__(self, longueur, hauteur, tableau):
        self.longueur = longueur
        self.hauteur = hauteur
        self.tableau = tableau
        
    def creer_tableau(self):
        pass
    
    def obtenir_l(self):
        pass
        
    def obtenir_h(self):
        pass
        
    def est_vide(self):
        pass
    
    def choisir_trimino(self, coordonnees):
        """"""
        pass


    def verifier_tableau(self):
        """Verifier si il y a de la place pour ajouter un trimino """
        pass
    
    def ajouter_tuile(self, tuile):
        pass
    
    def renvoyer_tuile(self, i):
        pass



# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Grille:
    def __init__(self, longueur, hauteur, tableau=[]):
        self.longueur = longueur
        self.hauteur = hauteur
        self.tableau = tableau
        
    def creer_tableau(self):
        """
        Methode qui renvoie un tableau (list) 
        initialisé selon les attributs longueur(int) et hauteur(int) de l'objet
        """
        
        
        for t in range(self.hauteur):
            l=[]
            for i in range(self.longueur):
                l.append(0)
            self.tableau.append(l)
                
    def obtenir_l(self):
        return self.longueur
        
    def obtenir_h(self):
        return self.hauteur
        
    def est_vide(self):
        pass
    
    def choisir_trimino(self, coordonnees, type_tuile):
        """
        """
        pass
    
    def liste_vide(self):
        liste_vide = []
        for t in range(self.hauteur):
            for i in range(self.longueur):
                if self.tableau[t][i] == 0:
                    liste_vide.append((t,i))
        return liste_vide
                    
    def verifier_tuile_vide(self, liste_vide):
        for t in liste_vide:
            if (t[0], t[1]-1) in liste_vide and (t[0]-1, t[1]) in liste_vide:
                return True
            if (t[0]-1, t[1]) in liste_vide and (t[0]+1, t[1]) in liste_vide:
                return True
            if (t[0]+1, t[1]) in liste_vide and (t[0], t[1]+1) in liste_vide:
                return True
            if (t[0], t[1]+1) in liste_vide and (t[0], t[1]-1) in liste_vide:
                return True
        return False
            
        
                    
    def verifier_tableau(self):
        """Verifier si il y a de la place pour ajouter un trimino """
        
     
    def ajouter_tuile(self, num_tuile):
        pass
    
    def renvoyer_tuile(self, num_tuile):
        pass
    
    
t=Grille(5,6)
