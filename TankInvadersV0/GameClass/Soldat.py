from tkinter import *
from gameClass.entity import Entities


class Soldat(Entities):
    
    def __init__(self, canvas, pos, img, hp, size, proj, fproj):
        super().__init__(canvas, pos, img, hp, size, proj, fproj)
        
        self.show()

    
    def move(self, dx):
        """Déplace le soldat horizontalement."""
        self.pos[0] = self.pos[0] + dx 
        if self.pos[0] < 10:
            self.pos[0] = 10
            dx = 0
        if self.pos[0] > 790:
            self.pos[0] = 790
            dx = 0
        if self.image_id is not None:  # Vérifier si l'image est bien créée
            self.canvas.move(self.image_id, dx, 0)
            
    def shoot(self, pos):
        pass