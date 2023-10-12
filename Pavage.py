from Grille import Grille
#Ici on crée juste la fonction pavage et ses sous-fonctions, on implémentera de quoi l'appliquer à des grilles ensuite dans main 

def première_case_vide(grille : Grille):
    return grille.liste_vide()[0]

def paver(grille : Grille):
    """Fonction qui pave une grille donnée"""
    

def pavage(grille : Grille) :
    """Fonction qui va lancer le processus de pavage"""
    grille.creer_tableau()
    if grille.est_pavable() != False:   #D'abord on vérifie que la grille est pavable, à faire séparément de paver pour vérifier s'il est possible de résoudre le problème
        case_courante= première_case_vide(grille)
        if grille.hauteur() % 2 == 0 : 
            if grille.ajouter_tuile(case_courante, 1) == True : 
                    while grille.liste_vide != []:
                         if grille.ajouter_tuile(case_courante, 1) == True:
                              case_courante= première_case_vide(grille)
                              grille.ajouter_tuile((case_courante[0], case_courante[1]-1, 3))



g = Grille(4,6)
print(g.est_vide())
pavage(g)
