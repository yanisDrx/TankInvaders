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
        Title_Text(self, canvas = self.home_canvas,text="TANK INVADERS V0", colour="#878787", xaxis=402, yaxis=152)
        Title_Text(self, canvas = self.home_canvas,text="TANK INVADERS V0", colour="white", xaxis=400, yaxis=150)

        #touches utilisables
        self.pressed_keys = {
            "Left": False,
            "Right": False,
            "Space": False
            }
     
        
    def Jouer(self):
        """Test de jeu"""
        if self.is_playing == False:
            
            self.is_playing = True
            print("Jeu en cours :",self.is_playing)
            
            self.game_canvas = Base_Canvas(self, "TankInvadersV0/Images/champ_bataille.png")
            self.home_canvas.destroy()
            
            self.soldat = Soldat(canvas = self.game_canvas, pos=[400,725], img="TankInvadersV0/Images/soldier_player.png", hp=3, size=0, proj=0, fproj=0)
            
            self.init_gameplay()
                    
        else:
            print(self.is_playing)
        pass     
    
             
    def init_gameplay(self):
          
        # Binding keys (jsuis binlingue)
        self.keyBind()
        
        # Update des touches 
        self.update()
        
        # ajoute un premier tank
        self.tank = Tank(self.game_canvas, pos=(725,100), img="TankInvadersV0/Images/tank.png", hp = 1, size=0, proj=0, fproj=0)
        
            
    def keyBind(self):
        
        self.bind("<KeyPress>", self.on_key_press)
        self.bind("<KeyRelease>", self.on_key_release)  
            
            
    def update(self):
        
        # Déplacer le soldat horizontalement
        if self.pressed_keys["Left"] and not self.pressed_keys["Right"]:
            self.soldat.move(-10)
        if self.pressed_keys["Right"] and not self.pressed_keys["Left"]:
            self.soldat.move(+10)
            
        # Déplacer le tank horizontalement
        # self.tank.move(self.image_id, self.dx, self.dy)

        # Relance la boucle après 16ms (~60 FPS)
        self.after(16, self.update)
        
    
    def on_key_press(self, event):
         
        if event.keysym in self.pressed_keys:
            self.pressed_keys[event.keysym] = True

    def on_key_release(self, event):
        
        if event.keysym in self.pressed_keys:
            self.pressed_keys[event.keysym] = False