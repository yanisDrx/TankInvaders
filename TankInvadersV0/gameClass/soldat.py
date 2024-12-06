from tkinter import *
from gameClass.entity import Entities


class Soldat(Entities):
    
    def __init__(self, canvas, pos, img, hp, size, fproj):
        super().__init__(canvas, pos, img, hp, size, fproj=None)
        self.timer = 0  #Mise en place d'un cooldown 
        self.show()

    
    def move(self, dx): #ATTENTION CHANGER NOM DE VARIABLE CAR PAS UTILE AU MOVE MAIS A L'ENCADREMENT 
        self.pos[0] = self.pos[0] + dx 
        if self.pos[0] <= 10:
            self.pos[0] = 10
            dx = 0
        if self.pos[0] >= 790:
            self.pos[0] = 790
            dx = 0
        if self.image_id is not None:  # Vérifier si l'image est bien créée
            self.canvas.move(self.image_id, dx, 0)
            
    def shoot(self):
        
        if self.timer <= 0:
            x1, y1, x2, y2 = self.canvas.bbox(self.image_id)
            projectile_pos = ((x1+x2) / 2, y1)
            
            self.timer = self.fproj
        
    def update_timer(self):
        # if self.timer > 0:
            # self.timer -= delta_prime
            
        pass
