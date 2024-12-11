from tkinter import *
from gameClass.entity import Entities
from gameClass.projectile import Projectile


class Soldat(Entities):
    
    def __init__(self, canvas, pos, img, hp, size):
        super().__init__(canvas, pos, img, hp, size)
        self.timer = 0  #Mise en place d'un cooldown 
        self.bullets = []
    
    def move(self, dx): 
        self.pos[0] += dx 
        if self.pos[0] <= 10:   #Permet de limiter les déplacements (à gauche) du soldat dans la fenêtre de jeu 
            self.pos[0] = 10
            dx = 0
        if self.pos[0] >= 790:  #Permet de limiter les déplacements (à droite) du soldat dans la fenêtre de jeu 
            self.pos[0] = 10
            self.pos[0] = 790
            dx = 0
        if self.image_id is not None:  # Vérifier si l'image est bien créée
            self.canvas.move(self.image_id, dx, 0)


    



          
    # def shoot(self):
        
    #     x1, y1, x2, y2 = self.updateTir()
            
    #     if len(self.image_id) < 4 :
    #         bullet = Projectile (self.canvas, (x1+x2) / 2, y1)
    #         self.bullets.append(bullet)
        
