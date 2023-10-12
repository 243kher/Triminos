from Grille import Grille
#Ici on crée juste la fonction pavage et ses sous-fonctions, on implémentera de quoi l'appliquer à des grilles ensuite dans main 

def première_case_vide(grille : Grille):
    return grille.liste_vide()[0]

from Grille import Grille
#Ici on crée juste la fonction pavage et ses sous-fonctions, on implémentera de quoi l'appliquer à des grilles ensuite dans main 

def première_case_vide(grille : Grille):
    """Fonction qui détermine la première case vide de la grille"""
    return grille.cases_vide()[0]

    

def pavage(grille : Grille, types : list) :
    """Fonction qui va lancer le processus de pavage"""
    grille.creer_tableau()
    if grille.verifier_tuile_vide() == False:   #test qui vérifie si on a fini
        if grille.cases_vide() == []:   #test qui vérifie si on obtient une grille valable ou non 
            return True
        else:
            return False
    case_courante = première_case_vide(grille)  #case sur laquelle on cherche à placer chaque tuile
    print(grille.cases_vide()[0])
    print(case_courante)
    for tuile in types :
        if grille.ajouter_tuile(case_courante[0], case_courante[1], tuile) == True: #essai pour placer une tuile 
            #test = pavage(grille, types)    #appel récursif
            test = True
            if test == True :   #cas où l'appel récursif renvoie une grille valide
                return grille.tableau
            else:
                """x = types.pop(0)    #on change la liste des types afin de tester les tuiles dans un autres ordre
                types.append(x)
                if x == 3 :
                    return False"""
                grille.enlever_tuile()  #on change la dernière tuile

    return False
            

            



g = Grille(3,3)
g.creer_tableau()
print(g.est_vide())
pavage(g, [0, 1, 2, 3])
print(g)



g = Grille(4,6)
print(g.est_vide())
pavage(g)
