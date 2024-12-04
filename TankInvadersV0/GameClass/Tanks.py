from tkinter import *
from gameClass.entity import Entities


class Tank(Entities):
    
    def __init__(self, canvas, pos, img, hp, size, proj, fproj):
        super().__init__(canvas, pos, img, hp, size, proj, fproj)
        
        self.show()
        
    def move(self, dx, dy):
        
        canvas_width = self.canvas.winfo_width()
        self.step_x = dx
        self.step_y = dy

        if self.pos[0] >= canvas_width - 40:
            self.direction = -1
            self.pos = (self.pos[0], self.pos[1] + self.step_y)
        elif self.pos[0] <= 40:
            self.direction = 1
            self.pos = (self.pos[0], self.pos[1] + self.step_y)

        self.pos = (self.pos[0] + self.direction * self.step_x, self.pos[1])
        print(self.pos)
        self.canvas.coords(self.image_id, self.pos[0], self.pos[1])
                    