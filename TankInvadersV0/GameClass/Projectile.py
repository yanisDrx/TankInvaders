from tkinter import *
from gameClass.entity import Entities


class Projectile (Entities):
    def __init__(self, canvas, pos, img, hp, size, proj, fproj, speed):
        super().__init__(self, canvas, pos, img, hp=1, size=size, proj=None, fproj=None)
        
        self.speed = speed
        self.image_id = self.canvas.create_image(self.pos[0], self.pos[1], image = self.img)
        
    def update(self):   #Permet de mettre à jour l'affichage du projectile à chaque frame
        self.canvas.move(self.image_id, self.pos[0], self.pos[1] + self.speed)  
        self.pos = self.canvas.coords(self.image_id)
        if self.pos[1] <= 0: # Quand le projectile sort de notre fenêtre de jeu, il est supprimé
            self.canvas.destroy(self.image_id) #Permet la suppression du projectile 
            
    def collision(self):
        
        pass