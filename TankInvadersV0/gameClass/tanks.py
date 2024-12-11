from tkinter import *
from gameClass.entity import Entities


class Tank(Entities):
    
    def __init__(self, canvas, pos, img, hp):
        super().__init__(canvas, pos, img, hp)
        
        self.direction = 1
        self.step_x = 2
        self.step_y = 85
        
        
        
    def move(self):
        
        canvas_width = self.canvas.winfo_width()

        if self.pos[0] >= canvas_width - 40:
            self.direction = -1
            self.pos = (self.pos[0], self.pos[1] + self.step_y)
        elif self.pos[0] <= 40:
            self.direction = 1
            self.pos = (self.pos[0], self.pos[1] + self.step_y)

        self.pos = (self.pos[0] + self.direction * self.step_x, self.pos[1])
        self.canvas.coords(self.image_id, self.pos[0], self.pos[1])
                    
    def animate(self):
        
        self.show()
        self.move()
        self.canvas.after(50, self.animate)