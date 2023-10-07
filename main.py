from Grille import *


grille = Grille(4, 4)
grille.creer_tableau()
t = grille.cases_vide()
grille.ajouter_tuile(1, 1, 0)
n = grille.cases_vide()
print(t)
print(n)
