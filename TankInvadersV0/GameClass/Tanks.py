from tkinter import *
from GameClass.Entity import Entities


class Tank(Entities):
    
    def __init__(self, canvas, pos, img, hp, size, proj, fproj):
        super().__init__(canvas, pos, img, hp, size, proj, fproj)
        
        # pil_img = Image.open(img)
        # pil_img = pil_img.resize((pil_img.width * 2, pil_img.height * 2))
        
        
        self.show()