import random
from tkinter import *
from tkinterClass.base_canvas import *
from tkinterClass.buttons import *
from tkinterClass.title_label import *
from gameClass.soldat import *
from gameClass.tanks import *
from gameClass.entity import *
from gameClass.protections import *
from gameClass.mur import *
from gameClass.collision_manager import *


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
            "space": False
            }
        
        #liste d'ennemis (quand len = 0 -> fin du jeu)
        self.ennemies = []
     
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
            self.soldat = Soldat(self.game_canvas, pos=[400,625], img="TankInvadersV0/Images/soldier_player.png", hp=2, cooldown = 1)
            
            # ajoute 3 murs
            self.murs = []
            self.posx_murs = []

            # générer la position du premier mur
            self.posx1 = random.randint(20, 640)
            self.posx_murs.append(self.posx1)
            
            # générer la deuxième position avec la condition de ne pas se superposer
            self.posx2 = random.randint(20, 640)
            while abs(self.posx2 - self.posx_murs[0]) < 220:
                self.posx2 = random.randint(20, 640)
            self.posx_murs.append(self.posx2)
            
            for i in range (2):
                self.murs.append(Wall(self.game_canvas,self.posx_murs[i], 500, img="TankInvadersV0/Images/wall.png", hp=12))
                print(i)
            
            # ajoute les textes fixes de scores et vies
            Title_Text(self, canvas = self.game_canvas,text="Vies : ",font = 15, colour="white", xaxis=670, yaxis=740)
            Title_Text(self, canvas = self.game_canvas,text="Score : ",font = 15, colour="white", xaxis=110, yaxis=740)

            # crée les textes variables de scores et vies
            self.vies_txt = self.game_canvas.create_text(710, 740, text=self.soldat.hp, font = ("Arial", 15), fill="white") 
            self.score_txt = self.game_canvas.create_text(160, 740, text=self.score, font = ("Arial", 15), fill="white")
            
            self.easy_tank_count = 0
            self.medium_tank_count = 0
            
            # ajoute les tanks
            self.add_ennemies()
            # self.add_medium_tank()                                   A MODIF !!!!!
            #initialisation de la partie
            self.init_gameplay()
                    
        else:
            print(self.is_playing)
    
    def add_ennemies(self):
        self.add_easy_tank()
        
    
    def add_easy_tank(self):
        self.start_x = 759
        self.start_y = 25
        if self.easy_tank_count < 8:
            # Ajouter un easy_tank
            self.easy_tank = Tank(self.game_canvas, pos=(self.start_x, self.start_y), img="TankInvadersV0/Images/tank.png", hp=3, canshoot=False)
            self.ennemies.append(self.easy_tank)
            self.easy_tank.show()
            
            self.easy_tank_count += 1
            print(f"Easy Tanks: {self.easy_tank_count}")
            
            self.easy_tank.animate()
            # mise à jour des vies et score pour démo (à ajuster)
            self.soldat.hp -= 1  # À MODIFIER ÉVIDEMMENT
            self.score += 1
            self.update_vies()
            self.update_score()
            
            # Planifie le prochain tank ou passe aux medium_tanks
            if self.easy_tank_count != 8:
                self.game_canvas.after(1000, self.add_easy_tank)
            else:
                self.game_canvas.after(1000, self.add_medium_tank)

        
    def add_medium_tank(self):
        self.start_x = 759
        self.start_y = 21
        if self.medium_tank_count < 9:
            # Ajouter un medium_tank
            self.medium_tank = Tank(self.game_canvas, pos=(self.start_x, self.start_y), img="TankInvadersV0/Images/med_tank.png", hp=3, canshoot=True)
            self.ennemies.append(self.medium_tank)
            self.easy_tank.show()
            
            
            self.medium_tank_count += 1
            print(f"Medium Tanks: {self.medium_tank_count}")
            
            self.medium_tank.animate()
            
            # Planifie le prochain medium_tank
            if self.medium_tank_count < 8:
                self.game_canvas.after(1000, self.add_medium_tank)
             
             
    def init_gameplay(self):
          
        # Binding keys (jsuis bilingue)
        self.keyBind()
        
        # Update des touches 
        self.update()
            
            
    def keyBind(self):
        
        # sépare les touches pressées et relachées afin d'avoir un mouvement final du soldat plus fluide
        self.bind("<KeyPress>", self.on_key_press)
        self.bind("<KeyRelease>", self.on_key_release)  
        self.bind("<space>", self.spaceBar)
     
     
    def spaceBar(self, event=None):
        self.soldat.shoot()  
        # for ennemies in self.ennemies :
        #     ennemies.shoot() 

    def tank_shooting(self):
        random_shooter = random.randint(0,len(self.ennemies)-1)
        if self.ennemies[random_shooter].canshoot == True :
            self.ennemies[random_shooter].shoot()
    
    def checkAllCOlisions(self):
        ## on fais les boucles sur toutes les entitées et verivfier les collsiiosn 
        ## ezt on applique les collisisons  
        pass
    
    
    def update(self):
        
        # Déplacer le soldat horizontalement
        if self.pressed_keys["Left"] and not self.pressed_keys["Right"]:
            self.soldat.move(-10)
        if self.pressed_keys["Right"] and not self.pressed_keys["Left"]:
            self.soldat.move(+10)
        
        # pas encore utile
        # self.checkAllCOlisions()

        # déplace les tanks horizontalement puis vers le bas en séquence
        for ennemi in self.ennemies:
            ennemi.move() 
        
        #fais tirer un tank a un temps random  
        random_time = random.randint(0,50)
        if random_time >= 45:
            self.tank_shooting()
        
        # self.collisions = CollisionManager.handle_collisions(self.projectiles, self.protections)
        
        # for projectile in self.projectiles:
        #     projectile.animate()

        # for protection in self.protections:
        #     protection.show()
        
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
            
                 
    def checkAllCollisions(self):
        # on fait les boucles sur toutes les entitées et on vérifie les collisions 
        # on applique les collisisons  
        pass

    def tank_shooting(self):
        random_shooter = random.randint(0,len(self.ennemies)-1)
        if self.ennemies[random_shooter].canshoot == True :
            self.ennemies[random_shooter].shoot()
    
        self.projectiles = []  # Liste des projectiles actifs
        self.protections = []  # Liste des protections

        # Ajout d'entités (par exemple, au début du jeu)
        # self.projectiles.append(Projectile(self.game_canvas, (100, 200), img="TankInvadersV0/Images/bullet_soldier.png", speed=5, direction=-1))
        # self.protections.append(Protections(self.game_canvas, (200, 300), img="TankInvadersV0/Images/wall.png", hp=3))

