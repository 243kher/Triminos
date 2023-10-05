""""ce programme contient les tests des méthodes contenus dans le fichier "Grille.py""" ""

from Grille import Grille


def test_creer_tableau():
    longueur,hauteur = 5,4
    grillage = Grille(longueur, hauteur)
    grillage.creer_tableau()
    assert grillage.tableau == [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


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
    assert grillage.choisir_trimino(coordonnees, type_tuile) == [(0, 1), (1, 1), (0, 2)]
    type_tuile = 2
    assert grillage.choisir_trimino(coordonnees, type_tuile) == [(0, 1), (-1, 1), (0, 2)]
    type_tuile = 3
    assert grillage.choisir_trimino(coordonnees, type_tuile) == [(0, 1), (-1, 1), (0, 0)]

def test_ajouter_tuile():
    grille = Grille(4, 4)
    assert grille.ajouter_tuile(0, 0, 0) == True  # Ajoute une tuile de type 0 à la position (0, 0)
    assert grille.ajouter_tuile(5, 5, 0) == False

def test_choisir_trimino():
    grille = Grille(4, 4)
    
    # Teste le choix d'un trimino de type 0 à la position (1, 1)
    coords = grille.choisir_trimino((1, 1), 0)
    expected_coords = [(1, 1), (2, 1), (1, 0)]
    assert coords == expected_coords

    # Teste le choix d'un trimino de type 1 à la position (2, 2)
    coords = grille.choisir_trimino((2, 2), 1)
    expected_coords = [(2, 2), (3, 2), (2, 3)]
    assert coords == expected_coords

    # Teste le choix d'un trimino de type 2 à la position (0, 0)
    coords = grille.choisir_trimino((0, 0), 2)
    expected_coords = [(0, 0), (-1, 0), (0, 1)]
    assert coords == expected_coords

    # Teste le choix d'un trimino de type 3 à la position (3, 3)
    coords = grille.choisir_trimino((3, 3), 3)
    expected_coords = [(3, 3), (2, 3), (3, 2)]
    assert coords == expected_coords
    

def test_cases_vide():
    grille = Grille(4, 4)

    grille.creer_tableau()
    # Teste une grille vide
    assert grille.cases_vide() == [(0, 0), (1, 0), (2, 0), (3, 0), 
                                   (0, 1), (1, 1), (2, 1), (3, 1), 
                                   (0, 2), (1, 2), (2, 2), (3, 2), 
                                   (0, 3), (1, 3), (2, 3), (3, 3)]

    # Ajoute une tuile
    grille.ajouter_tuile(1, 1, 0)  # Ajoute une tuile de type 0 à la position (1, 1)
    
    # Teste la liste des cases vides après avoir ajouté une tuile
    assert grille.cases_vide() == [(0, 0),         (2, 0), (3, 0), 
                                   (0, 1),                  (3, 1), 
                                   (0, 2), (1, 2), (2, 2), (3, 2), 
                                   (0, 3), (1, 3), (2, 3), (3, 3)]

def test_verifier_tuile_vide():
    grille = Grille(4, 4)
    
    # Teste la vérification d'une tuile vide sur une grille vide
    assert grille.verifier_tuile_vide([]) == False

    # Ajoute quelques tuiles
    grille.ajouter_tuile(1, 1, 0)  # Ajoute une tuile de type 0 à la position (1, 1)
    grille.ajouter_tuile(0, 1, 1)  # Ajoute une tuile de type 1 à la position (0, 1)
    grille.ajouter_tuile(2, 1, 2)  # Ajoute une tuile de type 2 à la position (2, 1)
    
    # Teste la vérification d'une tuile vide sur la grille actuelle
    assert grille.verifier_tuile_vide([(1, 0), (2, 0)]) == True  # Les coordonnées (1, 0) et (2, 0) sont vides et forment un trimino valide

def test_verifier_tableau():
    grille = Grille(4, 4)
    
    # Teste la vérification du tableau sur une grille vide
    assert grille.verifier_tableau() == True  # La grille est vide, donc il y a de la place pour un trimino
    
    # Ajoute quelques tuiles
    grille.ajouter_tuile(1, 1, 0)  # Ajoute une tuile de type 0 à la position (1, 1)
    grille.ajouter_tuile(0, 1, 1)  # Ajoute une tuile de type 1 à la position (0, 1)
    grille.ajouter_tuile(2, 1, 2)  # Ajoute une tuile de type 2 à la position (2, 1)
    
    # Teste la vérification du tableau sur la grille actuelle
    assert grille.verifier_tableau() == True  # Il y a encore de la place pour un trimino

    # Remplissons la grille pour qu'il n'y ait plus de place pour un trimino
    grille.ajouter_tuile(0, 0, 3)  # Ajoute une tuile de type 3 à la position (0, 0)
    grille.ajouter_tuile(1, 0, 2)  # Ajoute une tuile de type 2 à la position (1, 0)
    grille.ajouter_tuile(2, 0, 1)  # Ajoute une tuile de type 1 à la position (2, 0)
    grille.ajouter_tuile(3, 0, 0)  # Ajoute une tuile de type 0 à la position (3, 0)
    grille.ajouter_tuile(0, 2, 3)  # Ajoute une tuile de type 3 à la position (0, 2)
    grille.ajouter_tuile(1, 2, 2)  # Ajoute une tuile de type 2 à la position (1, 2)
    grille.ajouter_tuile(2, 2, 1)  # Ajoute une tuile de type 1 à la position (2, 2)
    grille.ajouter_tuile(3, 2, 0)  # Ajoute une tuile de type 0 à la position (3, 2)

    # Teste à nouveau la vérification du tableau, qui doit maintenant renvoyer False
    assert grille.verifier_tableau() == False



def test_ajouter_tuile():
    pass


def test_obtenir_tuile():
    pass


def test_enlever_tuile():
    pass
    
if __name__ == "__main__":
    test_creer_tableau()
    test_est_vide()
    test_choisir_trimino()
    test_ajouter_tuile()
    test_choisir_trimino()
    test_cases_vide()
    test_verifier_tuile_vide()
    test_verifier_tableau()

    print("Tous les tests ont réussi.")
