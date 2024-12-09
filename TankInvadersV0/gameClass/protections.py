from tkinter import * 
from gameClass.entity import Entities

class Protections (Entities):
    def __init__(self, canvas, pos, img):
        super().__init__(self, canvas, pos, img, hp=1)
    
    
    def delete(self):
        self.canvas.delete(self.protection)
        
        
    def get_coords(self):
        self.pos = self.canvas.coords(self.brick)
        x1 = self.pos[0] - 18
        y1 = self.pos[1] - 18
        x2 = x1 + 36
        y2 = y1 + 36
        return x1, y1, x2, y2