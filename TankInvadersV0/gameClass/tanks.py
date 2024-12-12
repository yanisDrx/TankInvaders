from tkinter import *
from gameClass.entity import Entities
from gameClass.projectile import Projectile



class Tank(Entities):
    
    def __init__(self, canvas, pos, img, hp, canshoot):
        super().__init__(canvas, pos, img, hp)
        
        self.canshoot = canshoot
        self.direction = 1
        self.step_x = 2
        self.step_y = 85
        self.show()
        print(f"Tank created at position: {self.pos}")
        
        
    def move(self):
        canvas_width = self.canvas.winfo_width()

    # Vérifier s'il touche le bord droit
        if self.pos[0] >= canvas_width - 40:
            if self.direction == 1:  # Si le tank va à droite
                self.direction = -1  # Change la direction
                self.pos = (self.pos[0], self.pos[1] + self.step_y)  # Descend de 85px

        # Vérifier s'il touche le bord gauche
        elif self.pos[0] <= 40:
            if self.direction == -1:  # Si le tank va à gauche
                self.direction = 1  # Change la direction
                self.pos = (self.pos[0], self.pos[1] + self.step_y)  # Descend de 85px

        # Déplace horizontalement en fonction de la direction
        self.pos = (self.pos[0] + self.direction * self.step_x, self.pos[1])

        # Met à jour la position sur le canvas
        self.canvas.coords(self.image_id, self.pos[0], self.pos[1])
       
                    
    def animate(self):  
        self.move()
        self.canvas.after(50, self.animate)
        
        
    def shoot(self):
        self.bullet = Projectile(canvas=self.canvas,pos=(self.pos[0], self.pos[1]), img="TankInvadersV0/Images/bullet_tank.png",speed=-5, direction=1) #Création du projectile
        self.bullets.append(self.bullet) #Ajoute le projectile à la liste des projectiles
        
        for bullets in self.bullets :
            bullets.animate()
          
            
    def checkdeath(self, ennemies_list):
        if self.hp <= 0:
            print(f"{self} est détruit !")
            self.canvas.delete(self.image_id)  # Supprime le tank du canvas
            if self in ennemies_list:
                ennemies_list.remove(self)