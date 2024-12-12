"""Classe Projectile
Par : Pirès-Portelada Yanis et Bovet Gauthier
Lieu : CPE Lyon
Date : 7 Décembre 2024
Codé en : Python sur VS code"""

from tkinter import *
from gameClass.entity import Entities


class Projectile (Entities):
    def __init__(self, canvas, pos, img, speed, direction):
        super().__init__(canvas, pos, img, hp=1)
        self.speed = speed  #Vitesse verticale (négative pour monter et positive pour descendre)
        self.direction = direction
        self.step_y = 10
        self.is_active = True
        self.to_delete = False
        

    def move(self):
        # canvas_height = self.canvas.winfo_height()

        if self.pos[1] > self.canvas.winfo_height()  or self.pos[1] < 0:
            self.canvas.delete(self.image_id)
            self.is_active = False
            return
        
        self.pos = (self.pos[0], self.pos[1] + self.direction * self.step_y)
        self.canvas.coords(self.image_id, self.pos[0], self.pos[1]) 
    
    
    def animate(self):
        if self.is_active:
            self.show()
            self.move()
            self.canvas.after(16, self.animate)
    
        
    def check_collision(self, target_bbox):
        if not self.bounding_box or not target_bbox:    #Sert à vérifier s'il existe un tir ou une cible sinon le fait de vérifier une collision est inutile
            return False
        x1, y1, x2, y2 = self.bounding_box  #Coordonnées du projectile
        tx1, ty1, tx2, ty2 = target_bbox    #Coordonnées de la cible espérée du projectile   
        return not (x2 < tx1 or tx2 < x1 or y2 < ty1 or ty2 < y1)
    
    
    def get_coords(self):   #Fonction qui permet de récupérer les coordonnées du l'objet
        # if self.tir is None:
        #     return None
        return self.canvas.bbox(self.image_id)
    
    
    def update_position(self):
        self.canvas.move(self.tir, 0, self.speed)  #Déplacement vertical 
        self.pos = self.canvas.coords(self.tir)    #Met à jour la position du tir       
        self.bounding_box = self.get_coords()

        if self.pos[1] <= 0 or self.pos[1] >= self.canvas.winfo_height():   #Quand le projectile sort de notre fenêtre de jeu, il est supprimé (en haut ou en bas de la fenêtre)
            self.canvas.destroy(self.tir)  #Permet la suppression du projectile 


    def delete(self):   #Fonction qui permet de supprimer le tir 
        if hasattr(self, 'tir') and self.tir is not None:
            self.tir.destroy()  # ou toute autre méthode de suppression
        else:
            print(f"Projectile {self} n'a pas de tir.")
        # autres actions pour supprimer le projectile


