from tkinter import *


class Entities:
    
    def __init__(self, canvas, pos, img, hp, size, proj, fproj):
        
        self.canvas = canvas
        self.pos = pos
        self.img = PhotoImage(file = img)
        self.image_id = None
        
        self.hp = hp
        self.size = size
        self.proj = proj
        self.fproj = fproj
        
    def show(self):
        
        if self.image_id is None:
            self.image_id = self.canvas.create_image(self.pos[0], self.pos[1], image=self.img)