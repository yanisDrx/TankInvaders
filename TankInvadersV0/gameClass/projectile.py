from tkinter import *
from gameClass.entity import Entities


class Projectile (Entities):
    def __init__(self, canvas, pos, img, size, speed):
        super().__init__(canvas, pos, img, hp=1, size=size)
        self.speed = speed  #Vitesse verticale (négative pour monter et positive pour descendre)
        self.tir = self.canvas.create_image(self.pos[0], self.pos[1], image = img)
        self.bounding_box = self.get_coords()
        self.show()

    def get_coords(self):
        if self.tir is None:
            return None
        return self.canvas.bbox(self.tir)
    
    def update_position(self):
        self.canvas.move(self.tir, 0, self.speed)  #Déplacement vertical 
        self.pos = self.canvas.coords(self.tir)    #Met à jour la position du tir       
        self.bounding_box = self.get_coords()

        if self.pos[1] <= 0 or self.pos[1] >= self.canvas.winfo_height():   #Quand le projectile sort de notre fenêtre de jeu, il est supprimé (en haut ou en bas de la fenêtre)
            self.canvas.destroy(self.tir)  #Permet la suppression du projectile 


    def check_collision(self, target_bbox):
        if not self.bounding_box or not target_bbox:    #Sert à vérifier s'il existe un tir ou une cible sinon le fait de vérifier une collision est inutile
            return False
        x1, y1, x2, y2 = self.bounding_box  #Coordonnées du projectile
        tx1, ty1, tx2, ty2 = target_bbox    #Coordonnées de la cible espérée du projectile   
        return not (x2 < tx1 or tx2 < x1 or y2 < ty1 or ty2 < y1)

    def delete(self):   #Permet de supprimer le projectile du canvas
        if self.tir is not None:
            self.canvas.delete(self.tir)
            self.tir = None


