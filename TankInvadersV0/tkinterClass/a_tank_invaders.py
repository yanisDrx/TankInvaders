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
            self.easy_tank = Tank(self.game_canvas, pos=(self.start_x, self.start_y), img="TankInvadersV0/Images/tank.png", hp=1, canshoot=False)
            self.ennemies.append(self.easy_tank)
            self.easy_tank.show()
            
            self.easy_tank_count += 1
            print(f"Easy Tanks: {self.easy_tank_count}")
            
            self.easy_tank.animate()

            # mise à jour des vies et score pour démo (à ajuster)
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
    
    
    def check_all_collisions(self):
        for bullet in self.soldat.bullets:
            # Vérifier les collisions des projectiles du joueur avec les ennemis
            for enemy in self.ennemies:
                if self.check_collision(bullet, enemy):
                    # Gérer la collision : réduire les points de vie de l'ennemi et supprimer la balle
                    self.handle_collision(bullet, enemy)
                    
            # Vérifier les collisions des projectiles du joueur avec les protections (murs)
            for wall in self.murs:
                if wall.check_collision(bullet.get_coords()):
                    # Gérer la collision avec le mur (diminuer la vie du mur et supprimer la balle)
                    bullet.delete()

        # Vérifier les collisions des projectiles des ennemis avec le soldat
        for enemy in self.ennemies:
            for bullet in enemy.bullets:
                if self.check_collision(bullet, self.soldat):
                    # Gérer la collision avec le soldat (réduire ses points de vie)
                    self.handle_collision(bullet, self.soldat)


    def handle_collision(self, bullet, target):
        if isinstance(target, Tank):
            target.hp -= 1
            if target.hp <= 0:
                target.to_delete = True  # Marquer pour suppression, pas tout de suite
            bullet.to_delete = True
            self.update_score()  # Met à jour le score si un ennemi est détruit

        elif isinstance(target, Soldat):
            target.hp -= 1
            if target.hp <= 0:
                target.to_delete = True  # Marquer pour suppression, pas tout de suite
            bullet.to_delete = True
            self.update_vies()  # Met à jour les vies du joueur
    
    
    def check_collision(self, bullet, target):
        # Vérifie si les coordonnées du projectile et de l'entité se chevauchent
        bullet_bbox = bullet.get_coords()
        target_bbox = target.get_coords()
        
        if bullet_bbox and target_bbox:
            # Si les deux objets existent, vérifier s'ils se chevauchent
            x1, y1, x2, y2 = bullet_bbox
            tx1, ty1, tx2, ty2 = target_bbox
            return not (x2 < tx1 or tx2 < x1 or y2 < ty1 or ty2 < y1)
        return False
    
    
    def update(self):
        print("Mise à jour en cours...")
        # Déplacer le soldat horizontalement
        if self.pressed_keys["Left"] and not self.pressed_keys["Right"]:
            self.soldat.move(-10)
        if self.pressed_keys["Right"] and not self.pressed_keys["Left"]:
            self.soldat.move(+10)
        
        print("Déplacement effectué")
        # pas encore utile
        # self.checkAllCOlisions()

        # déplace les tanks horizontalement puis vers le bas en séquence
        for ennemi in self.ennemies:
            ennemi.move() 
          
        print(f"Nombre d'ennemis : {len(self.ennemies)}")
        
        # Vérifier les collisions entre les projectiles et les entités
        self.check_all_collisions()
        
        # Supprimer les objets marqués pour suppression
        self.remove_marked_objects()
        
        print("Objets supprimés")
        
        #fais tirer un tank a un temps random  
        random_time = random.randint(0,50)
        if random_time >= 45:
            self.tank_shooting()
        
        
        # Relance la boucle après 16ms (~60 FPS)
        self.after(33, self.update)

    def remove_marked_objects(self):
        # Crée une liste temporaire d'objets à supprimer
        to_remove = []

        # Ajoute les objets marqués pour suppression à la liste
        for obj in self.ennemies + self.soldat.bullets:
            if hasattr(obj, 'to_delete') and obj.to_delete:
                to_remove.append(obj)

        # Supprime les objets dans la liste après la boucle
        for obj in to_remove:
            obj.delete()  # Assurez-vous que la méthode delete est correctement définie
            if isinstance(obj, Tank):
                self.ennemies.remove(obj)
            elif isinstance(obj, Projectile):
                self.soldat.bullets.remove(obj)


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
        pass


    def tank_shooting(self):
        random_shooter = random.randint(0,len(self.ennemies)-1)
        if self.ennemies[random_shooter].canshoot == True :
            self.ennemies[random_shooter].shoot()
