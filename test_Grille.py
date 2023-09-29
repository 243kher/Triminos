""""ce programme contient les tests des méthodes contenus dans le fichier "Grille.py""" ""

from Grille import Grille


def test_creer_tableau():
    longueur,hauteur = 5,4
    grillage = Grille(longueur, hauteur)
    grillage.creer_tableau()
    assert grillage.tableau == [[0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def test_est_vide():
    longueur, hauteur = 5, 4
    grillage = Grille(longueur, hauteur)
    grillage.creer_tableau()
    assert grillage.est_vide() == True
    print(grillage.tableau)
    grillage.tableau[hauteur-1][longueur-1] = 1
    assert grillage.est_vide() == False


def test_choisir_trimino():
    longueur, hauteur = 5, 4
    grillage = Grille(longueur, hauteur)
    grillage.creer_tableau()
    
    coordonnees = (0,1)
    type_tuile = 0
    
    assert grillage.choisir_trimino(coordonnees, type_tuile) == [(0,1),(1,1),(0,0)]
    type_tuile = 1
    assert grillage.choisir_trimino(coordonnees, type_tuile) == [
        (0, 1), (1, 1), (0, 2)]
    type_tuile = 2
    assert grillage.choisir_trimino(coordonnees, type_tuile) == [
        (0, 1), (-1, 1), (0, 2)]
    type_tuile = 3
    assert grillage.choisir_trimino(coordonnees, type_tuile) == [
        (0, 1), (-1, 1), (0, 0)]
    

def test_verifier_tableau():
    pass


def test_ajouter_tuile():
    pass


def test_obtenir_tuile():
    pass


def test_enlever_tuile():
    pass
