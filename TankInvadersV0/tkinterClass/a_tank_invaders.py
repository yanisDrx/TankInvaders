from tkinter import *
from tkinterClass.base_canvas import *
from tkinterClass.buttons import *
from tkinterClass.title_label import *
from gameClass.soldat import *
from gameClass.tanks import *
from gameClass.entity import *


class TankInvaders(Tk):
    def __init__(self):
        super().__init__()
        
        #initialisation de l'app
        self.title("Tank Invaders V0")
        self.iconbitmap("TankInvadersV0/Images/icon.ico")
        self.geometry("800x800")
        
        #fixe la taille de l'app
        self.minsize(800,800)
        self.maxsize(800,800)
        
        #variable de status
        self.is_playing = False

        #Ajout d'un canvas avec image de fond
        self.home_canvas = Base_Canvas(self,"TankInvadersV0/Images/home_bg_image.png")
        
        #Ajout de boutons quitter et jouer
        Buttons(self,text="QUITTER",command=self.quit,xaxis=420,yaxis=600)
        Buttons(self,text="JOUER",command=self.Jouer,xaxis=70,yaxis=600)
        
        #Ajout Titre app
        Title_Text(self, canvas = self.home_canvas,text="TANK INVADERS V0",font = 50, colour="#878787", xaxis=402, yaxis=152)
        Title_Text(self, canvas = self.home_canvas,text="TANK INVADERS V0",font = 50, colour="white", xaxis=400, yaxis=150)

        #touches utilisables
        self.pressed_keys = {
            "Left": False,
            "Right": False,
            "Space": False
            }
        
        #liste d'ennemis (quand len = 0 -> fin du jeu)
        self.ennemies = []
        
        self.ennemies_coords = []
     
        self.score = 10 # ça va pas la

        
    def Jouer(self):
        
        if self.is_playing == False:
            
            # suppression du canvas d'accueil
            self.home_canvas.destroy()
            
            # variable d'état  
            self.is_playing = True
            print("Jeu en cours :",self.is_playing)
            
            # ouvre un nouveau canva du jeu, ajoute le bouton quitter
            self.game_canvas = Base_Canvas(self, "TankInvadersV0/Images/champ_bataille.png")
            Buttons(self,text="QUITTER",command=self.quit,xaxis=250,yaxis=715)
            
            # ajoute le rectangle dans lequel le bouton quitter se positionne, ainsi que le score et les vies
            self.rectangle = self.game_canvas.create_rectangle(0, 680, 800, 800, outline="#494949" ,fill="#494949", width=2)
            
            # ajoute un premier soldat
            self.soldat = Soldat(self.game_canvas, pos=[400,625], img="TankInvadersV0/Images/soldier_player.png", hp=2, size=0, fproj=0)
            
            # ajoute les textes fixes de scores et vies
            Title_Text(self, canvas = self.game_canvas,text="Vies : ",font = 15, colour="white", xaxis=670, yaxis=740)
            Title_Text(self, canvas = self.game_canvas,text="Score : ",font = 15, colour="white", xaxis=110, yaxis=740)

            # crée les textes variables de scores et vies
            self.vies_txt = self.game_canvas.create_text(710, 740, text=self.soldat.hp, font = ("Arial", 15), fill="white") 
            self.score_txt = self.game_canvas.create_text(160, 740, text=self.score, font = ("Arial", 15), fill="white")
            
            # ajoute les tanks
            self.add_ennemi()
            
            #initialisation de la partie
            self.init_gameplay()
                    
        else:
            print(self.is_playing)
    
    def add_ennemi(self):
        
        self.start_x = 759 # position initiale x de l'ennemi
        self.start_y = 25 # position initiale y de l'ennemi
        
        # ajoute un tank puis démarre son mouvement
        self.ennemi = Tank(self.game_canvas, pos=(self.start_x, self.start_y), img="TankInvadersV0/Images/tank.png", hp=3, size=(50, 50), fproj=None,)
        #self.ennemi = ...
        self.ennemi.animate()
        
        # positionne le tank dans la liste d'ennemis vivants
        self.ennemies.append(self.ennemi)
        
        # positionne les coordonnées en temps réel des ennemis dans une autre liste
        self.ennemies_coords.append(self.ennemi.pos)
        
        # mise à jour du canvas (règle un bug de Tcl *merci chatgpt*)
        self.game_canvas.update()
        
        self.soldat.hp -=1 # A MODIF EVIDEMMENT ON EST PAS CONS
        self.score +=1
        
        # mise à jour des vies
        self.update_vies()
        
        # mise à jour du score
        self.update_score()
        
        #limite la boucle à 16 ennemis max
        if len(self.ennemies) < 16: 
            self.game_canvas.after(1000, self.add_ennemi)
             
    def init_gameplay(self):
          
        # Binding keys (jsuis bilingue)
        self.keyBind()
        
        # Update des touches 
        self.update()
            
    def keyBind(self):
        
        # sépare les touches pressées et relachées afin d'avoir un mouvement final du soldat plus fluide
        self.bind("<KeyPress>", self.on_key_press)
        self.bind("<KeyRelease>", self.on_key_release)  
        
            
    def update(self):
        
        # Déplace le soldat horizontalement
        if self.pressed_keys["Left"] and not self.pressed_keys["Right"]:
            self.soldat.move(-10)
        if self.pressed_keys["Right"] and not self.pressed_keys["Left"]:
            self.soldat.move(+10)
        if self.pressed_keys["Space"]:
            self.soldat.shoot()
            
        # déplace les tanks horizontalement puis vers le bas en séquence
        for ennemi in self.ennemies:
            ennemi.move() 
            """pour être tout à fait honnête, cette fonction était utile car le premier mouvement
            défini par la fonction "animate" permettait de déplacer les tank qui apparaissaient
            hors du cadre une premiere fois jusqu'a la bordure gauche, puis cette fonction move
            s'occupait de la séquence de mouvement. Cependant, les conditions de la séquences ont
            fait que l'apparition des tank hors du cadre n'étaient plus possible, et la modification
            de ces méthodes fonctionnelles était trop laborieuse""" 
        
        # affiche les coordonnées de chaque ennemi dans la liste     
        print(self.ennemies_coords)
        
        # Relance la boucle après 16ms (~60 FPS)
        self.after(16, self.update)

    def update_vies(self):
        
        # mets à jour les vies du joueur en temps réél
        self.game_canvas.itemconfig(self.vies_txt, text=f"{self.soldat.hp}")
    
    def update_score(self):
        # pareil pour le score
        self.game_canvas.itemconfig(self.score_txt, text=f"{self.score}")
    
    def on_key_press(self, event):
         
        # mets à jour l'état à true lorsque la touche est pressée
        if event.keysym in self.pressed_keys:
            self.pressed_keys[event.keysym] = True

    def on_key_release(self, event):
        
        # pareil pour false - relachée
        if event.keysym in self.pressed_keys:
            self.pressed_keys[event.keysym] = False