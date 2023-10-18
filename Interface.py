from Grille import Grille

import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Button
from random import choice


class Interface(Grille):
    """
    Classe Interface qui hérite des méthodes et attributs de Grille
    Ceci va nous permettre de dessiner des triminos dans des cases plus facilement
    sans dédoubler notre code.
    longueur : colonne (int), hauteur : ligne (int) echelle : espacement (int)
    couleurs : matrices de couleurs (Liste[List(str)]), buttons : différents boutons selon l'index (dict)
    choix_de_couleurs : 8 possibilitées de couleurs au maximum pour un trimino (list)
    """

    def __init__(self, longueur, hauteur, echelle):
        super().__init__(self, longueur, hauteur)
        self.longueur = longueur
        self.hauteur = hauteur
        self.echelle = echelle
        self.couleurs = [
            ["white" for x in range(self.longueur)] for y in range(self.hauteur)
        ]
        self.buttons = {"Type 1: L": 0, "Type 2: Г": 1,
                        "Type 3: ꓶ": 2, "Type 4: ⅃": 3}
        self.choix_de_couleurs = [
            "red",
            "green",
            "yellow",
            "orange",
            "blue",
            "pink",
            "brown",
            "gray",
        ]

        self.creer_tableau()
        self.fig, self.ax = plt.subplots()
        self.tracer_grille()

        # Utilitaires qui se connectes aux méthodes dés l'utilisation des entrés utilisateur (aux touches de souris,au touchex de clavier, au défilement de souris)
        self.fig.canvas.mpl_connect(
            "button_press_event", self.on_clique_grille)
        self.fig.canvas.mpl_connect("key_press_event", self.on_retire)
        self.fig.canvas.mpl_connect("scroll_event", self.on_defile)

        # Créer les radio buttons des types de trimino
        self.radio_boutons_ax = self.fig.add_axes([0.03, 0.3, 0.15, 0.2])
        self.radio_boutons = RadioButtons(
            self.radio_boutons_ax,
            [cle for cle, valeur in self.buttons.items()],
            active=0,
        )
        # Suit le bouton seléctionné
        self.bouton_active = self.radio_boutons.value_selected
        # Connecte le boutton cliqué à sa méthode
        self.radio_boutons.on_clicked(self.on_clique_bouton_radio)

        # Créer le bouton annuler
        self.annuler_bouton_ax = self.fig.add_axes([0.03, 0.03, 0.1, 0.05])
        self.annuler_bouton = Button(self.annuler_bouton_ax, "Annuler")
        # Connecte le bouton cliqué à sa méthode
        self.annuler_bouton.on_clicked(self.on_annule_bouton_clique)

        # Texte d'action utilisateur
        self.text = self.fig.text(0.5, 0.05, "", ha="center", va="center")

    def tracer_grille(self):
        """
        Méthode qui trace la grille de longueur x hauteur
        Origine en haut à gauche
        Coordonées : Haut et droite positif, Bas et gauche négatif
        """
        # Tracer chaque ligne de haut en bas
        for i in range(self.hauteur + 1):
            y = -i * self.echelle
            self.ax.plot([0, self.longueur * self.echelle], [y, y], "k-")
        # Tracer chaque colonne de gauche droite
        for j in range(self.longueur + 1):
            x = j * self.echelle
            self.ax.plot([x, x], [0, -self.hauteur * self.echelle], "k-")
        # Cadrage du grillage
        self.ax.set_xlim(-1, (self.longueur * self.echelle) + 1)
        self.ax.set_ylim(-1 + (-self.hauteur * self.echelle), 1)
        # Supprimer les graduations sur les axes x et y
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        # Enlever le contour du graphique
        self.ax.axis("off")
        # Met en ratio le graphique
        self.ax.set_aspect("equal")

        # dessine le graphique
        self.fig.canvas.draw()

    def donner_couleur(self, liste_de_couleurs):
        """
        Méthode qui donne une couleur aléatoirement en fonction d'une liste
        retourne la couleur (str)
        """
        return choice(liste_de_couleurs)

    def donner_couleur_adjacent(self, coordonnees, type_tuile):
        """
        Méthode qui donne l'ensemble des couleurs adjacent d'un trimino
        retourne l'ensemble des couleurs (set)
        """

        ensemble_couleur = set()
        # chaque case prend la couleur de la case à gauche à droite en bas en haut
        for x, y in self.choisir_trimino(coordonnees, type_tuile):
            adjacent_coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            # ne la prend pas si hors de la grille
            for x, y in adjacent_coords:
                if self.longueur > x >= 0 and self.hauteur > y >= 0:
                    ensemble_couleur.add(self.couleurs[y][x])

        return ensemble_couleur

    def verifier_couleur_adjacent(self, liste_de_couleurs):
        """
        Methode qui enlève les couleurs déjà pris aux couleurs possibles à mettre sur un trimino
        retourne une liste des couleurs restantes possibles à mettre (list)
        """

        couleurs_restantes = self.choix_de_couleurs.copy()

        for couleur in liste_de_couleurs:
            if couleur != "white":
                couleurs_restantes.remove(couleur)

        return couleurs_restantes

    def dessiner_case(self, coordonnees, couleur="green"):
        """
        Méthode qui déssine une case x,y d'une couleur
        """

        x = coordonnees[0]
        y = coordonnees[1]

        self.couleurs[y][x] = couleur

        # Remplie chaque tuile d'apres ces quatres coordonnées en haut à gauche , en haut à droite, en bas à gauche, en bas à droite
        self.ax.fill(
            [
                x * self.echelle,
                (x + 1) * self.echelle,
                (x + 1) * self.echelle,
                x * self.echelle,
            ],
            [
                -(y * self.echelle),
                -(y * self.echelle),
                -((y + 1) * self.echelle),
                -((y + 1) * self.echelle),
            ],
            color=self.couleurs[y][x],
        )

        self.fig.canvas.draw()

    def dessiner_trimino(self, coordonnees, type_tuile):
        """
        Méthode qui déssine le trimino sur la grille
        vérifie si c'est possible
        choisie une couleur qui n'est pas adjacent à celui ci
        dessine le trimino
        """

        if self.ajouter_tuile(coordonnees[0], coordonnees[1], type_tuile):
            couleurs_adjacent = self.donner_couleur_adjacent(
                coordonnees, type_tuile)
            couleurs = self.verifier_couleur_adjacent(couleurs_adjacent)
            couleur = self.donner_couleur(couleurs)

            liste_coord_triminos = self.choisir_trimino(
                coordonnees, type_tuile)

            for i in range(len(liste_coord_triminos)):
                self.couleurs[liste_coord_triminos[i][1]][
                    liste_coord_triminos[i][0]
                ] = couleur

            for x, y in liste_coord_triminos:
                self.dessiner_case((x, y), couleur)
        else:
            self.text.set_text("Tu ne peux pas posé ce trimino")
            self.fig.canvas.draw()
            
    def dessiner_triminos_tableau(self):
        self.update_num_actuel()
        if self.num_actuel > 1:
            for i in range(1,self.num_actuel):
                coord = self.obtenir_tuile(i)
                
                #duplqué à voir pour simplifier
                
                ensemble_couleur = set()
                # chaque case prend la couleur de la case à gauche à droite en bas en haut
                for x, y in coord:
                    adjacent_coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                    # ne la prend pas si hors de la grille
                    for x, y in adjacent_coords:
                        if self.longueur > x >= 0 and self.hauteur > y >= 0:
                            ensemble_couleur.add(self.couleurs[y][x])
                            
                couleur = self.donner_couleur(self.verifier_couleur_adjacent(ensemble_couleur))
                
                for x, y in coord: 
                    
                    self.dessiner_case((x,y),couleur)
                


    def afficher(self):
        plt.show()

    def on_clique_grille(self, event):
        """
        Méthode lors d'un clique dans le graphique,
        elle récupère les coordonées x,y au rapport de l'échelle
        affiche l'action
        tente de dessiner un trimino
        """

        if event.inaxes == self.ax:
            if event.xdata != None and event.ydata != None:
                x = int((event.xdata) / self.echelle)
                y = int((event.ydata) / self.echelle)

                self.text.set_text(f"Tu as cliqué: ({x}, {y})")
                self.fig.canvas.draw()

                self.dessiner_trimino(
                    (x, -y), self.buttons[self.bouton_active])

    def on_annule_bouton_clique(self, event):
        """
        Méthode qui annule la dernière action,
        le dernier trimino placé
        renvoie une liste des coordonnées du trimino enlevé (Liste[tuple(x,y)])
        """
        liste_coord_triminos = self.enlever_tuile()
        if liste_coord_triminos:
            for x, y in liste_coord_triminos:
                self.dessiner_case((x, y), "white")

    def on_retire(self, event):
        """
        Méthode qui appel on_annule_bouton_clique si la touche retour est appuyé
        """
        if event.key == "backspace":
            self.on_annule_bouton_clique(event)

    def on_clique_bouton_radio(self, bouton):
        """
        Méthode change le bouton actif
        """
        self.bouton_active = bouton

    def on_defile(self, event):
        """
        Méthode qui change le bouton actif en fonction du scroll de de la souris
        """

        if event.button == "up":
            index = self.buttons[self.radio_boutons.value_selected] - 1
            if 0 <= index:
                self.radio_boutons.set_active(index)
        elif event.button == "down":
            index = self.buttons[self.radio_boutons.value_selected] + 1
            if index < len(self.radio_boutons.labels):
                self.radio_boutons.set_active(index)


# Exemple d'utilisation
if __name__ == "__main__":
    grille = Interface(
        6, 6, 20
    )  # Une grille de 5 colonnes, 4 lignes, avec une échelle de 20 pixels par unité

    grille.afficher()
