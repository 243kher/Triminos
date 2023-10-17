from Grille import *
from Interface import *

grille = Grille(4, 4)
grille.creer_tableau()
t = grille.cases_vide()
grille.ajouter_tuile(1, 1, 0)
n = grille.cases_vide()
print(t)
print(n)


grille2 = Grille(3, 4)
grille2.creer_tableau()
print(grille)

solutions = []
grille2.paver_recursif_toutes_solutions(solutions)
print(len(solutions),"solution")
"""
for solution in solutions:
    print(solution)
"""
    
    
grille3 = Interface(6, 3, 1)
grille3.creer_tableau()


if grille3.paver_recursif_une_solution():
    print("Solution trouvée:")
    print(grille3)
else:
    print("Aucune solution trouvée.")


grille3.dessiner_triminos_tableau()
grille3.afficher()



