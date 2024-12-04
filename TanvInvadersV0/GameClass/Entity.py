from tkinter import *


class Entities:
    
    def __init__(self, canvas, pos, img, hp, ):
        
        self.pos = pos
        self.img = PhotoImage(file = img)
        self.image_id = None
        self.canvas = canvas

        self.hp = hp
        
    def show(self):
        if self.image_id is None:
            self.image_id = self.canvas.create_image(self.pos[0], self.pos[1], image=self.img)