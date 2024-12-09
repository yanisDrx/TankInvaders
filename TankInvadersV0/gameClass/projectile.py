from tkinter import *
from gameClass.entity import Entities


class Projectile (Entities):
    def __init__(self, canvas, pos, img, size, speed):
        super().__init__(self, canvas, pos, "TankInvadersV0/images/bullet.png", hp=1, size=size, fproj=None)
        self.speed = speed
        self.image_id = self.canvas.create_image(self.pos[0], self.pos[1], image = self.img)
        
    def updateTir(self):   #Permet de mettre à jour l'affichage du projectile à chaque frame
        self.canvas.move(self.image_id, self.pos[0], self.pos[1] + self.speed)  #Permet la mise à jour des coordonnées du projectile
        if self.pos[1] <= 0:    #Quand le projectile sort de notre fenêtre de jeu, il est supprimé
            self.canvas.destroy(self.image_id)  #Permet la suppression du projectile 
        self.pos = self.canvas.coords(self.image_id)
        x1 = self.pos[0] - 5
        y1 = self.pos[1] - 12
        x2 = x1 + 10
        y2 = y1 + 24
        return x1,y1,x2,y2
            
    def collision(self):
        
        pass
