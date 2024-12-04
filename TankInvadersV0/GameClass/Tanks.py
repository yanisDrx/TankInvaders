from tkinter import *
from gameClass.entity import Entities


class Tank(Entities):
    
    def __init__(self, canvas, pos, img, hp, size, proj, fproj):
        super().__init__(canvas, pos, img, hp, size, proj, fproj)
        
        self.show()