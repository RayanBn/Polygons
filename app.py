#coding: utf-8
# importation des modules
import turtle
from tkinter import *

# creation de la classe principale, elle permet de creer des polygons predefini
class App:
    def __init__(self):
        self.window = Tk()# creation de la fenetre
        self.window.title("Application") # attribut un titre a la fenetre
        self.window.iconbitmap("logo.ico") # attribut un logo a la fenetre
        self.window.geometry('390x520') # definit la longueur et la largeur de la fenetre
        self.window.resizable(width=False, height=True) # impossible de changer la largeur de la fenetre
        self.bg = "#99D6DF" # variable qui va stocker la ouleur de fond de l'appli
        self.window.config(background=self.bg) # definit la couleur de fond de l'application
        self.canvas = Canvas(width=375, height=370) # permet d'implementer la fenetre turtle dans tkinter et de changer sa taille
        self.draw = turtle.RawTurtle(self.canvas) # va permetre l'utilisation des modules turtle

        self.onglet() # appel la fonction onglet qui est un menu repertoriant des onglets permettant de quitter la fenetre et changer de mode
        self.home() # appel de la fonction home ou ce trouve les menus deroulant permettant de choisir le polygon a tracer
        self.canvas.pack() # affiche la fenetre turtle
        self.window.mainloop() # fin du programme

# fonction qui cree un menu repertoriant des onglets permettant de quitter la fenetre et de changer de modes
    def onglet(self):
        self.menu = Frame(self.window) # cree un cadre sur la fenetre qui va permettre de bouger simplement tout les elements de ce cadre
        advanced = Menubutton(self.menu, text="Mode", width='30', bg='#50A7A7', activebackground='#E1F3F3',
                              borderwidth=2) # creation d'un onglet mode
        quit = Menubutton(self.menu, text="Quitter", width='30', bg='#50A7A7', activebackground='#E1F3F3',
                          borderwidth=2) # creation d'un onglet quitter

        advanced.grid(row=0, column=0, sticky=W) # change le positionnement de l'onglet mode
        quit.grid(row=0, column=1, sticky=W) # change le positionnement de l'onglet quitter

        advancedMenu = Menu(advanced, tearoff=0) # cration du menu advanced qui va permettre de changer le mode, la fonction "tearoff=0" permet d'eviter le detachement du menu
        advancedMenu.add_command(label='Normal', command=self.normal) # ajoute un attribut a l'onglet mode, celui ci permet de choisir le mode normal (par defaut)
        advancedMenu.add_command(label='Avancé', command=self.advancedOption) # ajoute un attribut a l'onglet mode, celui-ci permet de choisir le mode avancé
        advanced.configure(menu=advancedMenu) # fin de creation de l'onglet mode, permet de l'afficher

        quitMenu = Menu(quit, tearoff=0) # cration du menu quit qui va permettre de fermer la fenetre, la fonction "tearoff=0" permet d'eviter le detachement du menu
        quitMenu.add_command(label='Quitter', command=self.leave) # ajoute un attribut a l'onglet Quitter, celui ci permet de quitter la fenetre
        quit.configure(menu=quitMenu) # fin de creation de l'onglet mode, permet de l'afficher

        self.menu.pack() # affiche le menu

# creation de fonction ou se trouve tout les menus deroulant pour ameliorer l'IHM
    def home(self):
        self.frame = Frame(self.window, bg=self.bg) # creation d'un cadre pour failiter le deplacement des composants et leurs destruction
        button = Button(self.window, text="valider", command=self.config) # creation d'un bouton qui va permettre de dessiner

        self.c = StringVar() # memorise la chaine de caractere atribué a c
        self.c.set("Cotés") # affiche Cotés sur le menu deroulant
        self.c.trace_add("write", self.name) # permet de relier des menus deroulant a une meme fonction pour qu'ils soient accordé
        self.cote = OptionMenu(self.frame, self.c, "3", "4", "5", "6", "7", "8", "9", "10", "15", "20", "30", "40",
                               "50",
                               "100", "200", "300", "400", "500", "600", "700", "800", "900",
                               "1000") # creation du menu qui stock tout les cotés

        self.l = StringVar() # memorise la chaine de caractere atribué a l
        self.l.set("Taille") # affiche Taille sur le menu deroulant
        self.longueur = OptionMenu(self.frame, self.l, "1", "10", "50", "100", "200", "300", "500",
                                   "1000") # creation du menu qui stock toutes les tailles

        self.f = StringVar() # memorise la chaine de caractere atribué a f
        self.f.set("Figure") # affiche Figure sur le menu deroulant
        self.f.trace_add("write", self.names) # permet de relier des menus deroulant a une meme fonction pour qu'ils soient accordé
        self.figure = OptionMenu(self.frame, self.f, "triangle", "carré", "pentagone", "hexagone", "heptagone", "octogone", "ennéagone", "décagone", "pentadécagone", "icosagone", "triacontagone", "tétracontagone", "pentacontagone", "hectogone", "dihectogone", "trihectogone", "tétrahectogone", "pentahectogone", "hexahectogone", "heptahectogone", "octahectogone", "ennéahectogone", "Chiliogone") # creation du menu qui stock toutes les figures

        self.cote.grid(row=0, column=0, sticky=W) #gere le positionnement du menu
        self.longueur.grid(row=0, column=1, sticky=W) #gere le positionnement du menu
        self.figure.grid(row=0, column=2, sticky=W) #gere le positionnement du menu

        self.frame.pack() # affiche le cadre
        button.pack() # affiche le bouton permettant de tracer la figure

# Fonction qui permet de tracer tout type de polygons
    def polygone(self, longueur, angle, cote):
        if cote > 0: # si le coté demandé est supérieur a 0, on peut commencer la fonction
            self.draw.forward(longueur) # permet d'avancer de longueur
            self.draw.right(angle) # permet de tourner de angle
            self.polygone(longueur, angle, cote - 1) # recommence la fonction avec un nombre de coté inferieur
        self.draw.ht() # leve le stylo

#fonction qui gere les configuration permettant d'ameliorer l'IHM
    def config(self):
        self.draw.penup() # leve le tylo
        self.draw.goto(0, 150) # va en x = -25 et  y = 110
        self.draw.pendown() # baisse le stylo
        self.draw.clear() # efface le dessin
        self.draw.speed(10) # vitesse de la tortue = 10
        # gestion des erreurs, si une entry est vide celle-ci ce mettra en rouge pour indiquer a l'utilisateur d'entrer une valeur
        try:
            l = int(self.l.get()) # recupere la valeur de self.l
            self.longueur.config(bg="#EAEAEA") # change la couleur de fond de la cellule
            try:
                c = int(self.c.get()) # recupere la valeur de self.c
                self.cote.config(bg="#EAEAEA") # change la couleur de fond de la cellule
                self.polygone(l, 360 / c, c) # appel la fonction permettant de tracer un polygon
                self.texte = Label(self.window, text="le " + self.f.get() + " possède " + self.c.get() + " cotées", fg="red",
                                    bg=self.bg) # crée un texte pour informer l'utililsateur de la figure qu'il vient de tracer
                self.texte.pack() # affiche le texte
            except ValueError: # si il y a une erreur avec le cote :
                self.cote.config(bg="#F44141") # change la couleur de fond de a cellule
                texte = Label(self.window, text="Vous devez entrer le nombre de cotés", fg='red', bg=self.bg) # cree un message d'erreur
                texte.pack() # affiche le message d'erreur
        except ValueError: # si il y a une erreur avec la longueur :
            self.longueur.config(bg="#F44141") # change la couleur de fond de la cellule
            texte = Label(self.window, text="Vous devez entrer la taille", fg='red', bg=self.bg) # cree un messaeg d'erreur
            texte.pack() # affiche le message d'erreur

# fonction qui va repertorier le nom de toutes les figures et leurs cotés, elle va aussi permettre de relier des éléments d'un menu entre eux
    def name(self, a, b, c):
        name = {"3":"triangle", "4":"carré", "5":"pentagone", "6":"hexagone", "7":"heptagone", "8":"octogone", "9":"ennéagone", "10":"décagone", "15":"pentadécagone", "20":"icosagone", "30":"triacontagone", "40":"tétracontagone", "50":"pentacontagone", "100":"hectogone", "200":"dihectogone", "300":"trihectogone", "400":"tétrahectogone", "500":"pentahectogone", "600":"hexahectogone", "700":"heptahectogone", "800":"octahectogone", "900":"ennéahectogone", "1000":"Chiliogone"}
        self.f.set(name[self.c.get()])

    def names(self, a, b, c):
        names = {"triangle":"3", "carré":"4", "pentagone":"5", "hexagone":"6", "heptagone":"7", "octogone":"8", "ennéagone":"9", "décagone":"10", "pentadécagone":"15", "icosagone":"20", "triacontagone":"30", "tétracontagone":"40", "pentacontagone":"50", "hectogone":"100", "dihectogone":"200", "trihectogone":"300", "tétrahectogone":"400", "pentahectogone":"500", "hexahectogone":"600", "heptahectogone":"700", "octahectogone":"800", "ennéahectogone":"900", "Chiliogone":"1000"}
        self.c.set(names[self.f.get()])

# fonction qui va permettre d'acceder au mode normal de l'application, mode par defaut
    def normal(self):
        self.window.destroy() # detruit la fenetre principale
        App() # relance l'application

# fonction qui va permettre d'accéder au mode avancé de l'application
    def advancedOption(self):
        self.window.destroy() # detruit la fenetre
        AdvancedOption() # lance la class advancedOption dans laquel se trouve l'application avec possibilité de creer des polygons a sa guise

# fonction qui permet de fermer l'application
    def leave(self):
        self.window.destroy() # detruit la fenetre

# creation d'une classe permettant d'acceder aux parametres avancés de l'application
class AdvancedOption:
    def __init__(self):
        self.window = Tk() # creation de la fenetre
        self.window.title("Application") # initialise le nom de la fenetre
        self.window.iconbitmap("logo.ico") # definit le logo de la fenetre
        self.window.geometry('390x450') # definit la taille de la fenetre
        self.window.resizable(width=False, height=True) # impossible de changer la largeur de la fenetre
        self.bg = "#99D6DF" # variable qui va permettre de definir a chaque fois une couleur de fond
        self.window.config(background=self.bg) # definit la couleur de fond de l'application
        self.canvas = Canvas(width=375, height=300) # defini la taille de la fenetre turtle
        self.draw = turtle.RawTurtle(self.canvas) # permet d'utiliser les fonctions de turtle dans tkinter

        self.onglet() # appel de la fonction onglet dans laquel se trouve le menu permetttant de quitter la fenetre et changer de mode
        self.home() # appel de la fonction home qui affiche tout les composants utile a la creation d'un polygon
        self.canvas.pack() # affiche la fenetre turtle
        self.window.mainloop() # fin du programme

# creation d'une foction onglet qui re appel la fonction de la classe app
    def onglet(self):
        App.onglet(self) # appel de la fonction onglet dans la classe app

# creation de la fonction home qui affiche tout les composants utile a la creation d'un polygon
    def home(self):
        self.frame = Frame(self.window, bg=self.bg) # creation d'un cadre pour faciliter le deplacement des éléments et leurs destruction
        button = Button(self.frame, text="valider", command=self.config) # creation d'un bouton qui renvoie a la fonction config

        text_c = Label(self.frame, text="Nombres de Cotés ?", bg=self.bg) # creation d'un texte qui demande le nombre de cotés
        text_l = Label(self.frame, text="Longeur d'un Coté ?", bg=self.bg) # creation d'un texte qui demande la longueur
        self.entry_c = Entry(self.frame) # creation d'une entry
        self.entry_l = Entry(self.frame) # creation d'une entry

        text_c.grid(row=0, column=0) # ajuste l'emplacement de text_c
        text_l.grid(row=1, column=0) # ajuste l'emplacement de text_l
        self.entry_c.grid(row=0, column=1) # ajuste l'emplacement de self.entry_c
        self.entry_l.grid(row=1, column=1) # ajuste l'emplacement de self.entry_l
        button.grid(row=2, column=1) # ajuste l'emplacement du bouton

        self.frame.pack() # affiche le cadre et ses composants

# fonction qui gere les configuration permettant d'ameliorer l'IHM
    def config(self):
        self.draw.penup() # leve le stylo
        self.draw.goto(-25, 110) # setup les position de turtle
        self.draw.pendown() # baisse le stylo
        self.draw.clear() # efface la urtle
        self.draw.speed(10) # definit la vitesse de turtle a 10
        # essaye une chose et si sa produit une erreur exécute autre chose
        try:
            c = int(self.entry_c.get()) # recupere la valeur de entry_c
            self.entry_c.config(bg="white") # instaure le fond de couleur blanche
            try:
                l = int(self.entry_l.get()) # recupere la valeur de entr_l
                self.entry_l.config(bg="white") # instaure le fond de couleur blanche
                self.polygone(l, 360 / c, c) # appel de la fonction polygon
                self.texte = Label(self.window, text="la figure possède " + self.entry_c.get() + " cotées", fg="red",
                                    bg=self.bg) # cree un texte pour informer l'utilisateur de la figure qu'il a construit
                self.texte.pack() # affiche le texte
            except ValueError:
                self.entry_l.config(bg="#F44141") # definit la couleur de fond comme rouge clair
                texte = Label(self.window, text="Vous devez entrer la longueur", fg='red', bg=self.bg) # cree un message d'erreur
                texte.pack() # affiche le message d'erreur
        except ValueError:
            self.entry_c.config(bg="#F44141") # definit la couleur de fond comme rouge clair
            texte = Label(self.window, text="Vous devez entrer le nombre de cotés", fg='red', bg=self.bg) # cree un message d'erreur
            texte.pack() # affiche le message d'erreur

# creation d'une fonction polygone qui va permettre de dessiner tout type de polygons
    def polygone(self, longueur, angle, cote):
        App.polygone(self, longueur, angle, cote) # appel de la fonction polygone definit dans la classe App

# creation d'une fonction normal qui permet d'acceder au mode par defaut de l'application
    def normal(self):
        self.window.destroy() # detruit la fenetre
        App() # appel la fonction App

# creation d'une fonction qui permet d'aller sur la version avancée de l'application
    def advancedOption(self):
        self.window.destroy() # detruit la fenetre
        AdvancedOption() # appel de la fonction AdvancedOption

# creation d'une fonction permettant de fermer la fenetre
    def leave(self):
        self.window.destroy() # detruit la fenetre


App() # lancement de l'application

