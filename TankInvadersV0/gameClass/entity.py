from tkinter import *


class Entities:
    
    def __init__(self, canvas, pos, img, hp):
        self.canvas = canvas
        self.pos = pos  #Position sous forme de coordonnées avec x,y
        self.img = PhotoImage(file = img)   #Image associée à un objet
        self.image_id = None 
        self.hp = hp    #Les points de vie associés à l'objet
        self.bullets = []
        
    def show(self):
        if self.image_id is None:
            self.image_id = self.canvas.create_image(self.pos[0], self.pos[1], image=self.img)

    def get_coords(self):
        if self.image_id is not None:
            return self.canvas.bbox(self.image_id)
        return None
