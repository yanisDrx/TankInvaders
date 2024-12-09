from gameClass.protections import Protections

class Wall:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.proctections = []
        self.x = x
        self.y = y
        self.create()
    
    def create(self):
        for i in range(4):
            for j in range(4):
                mur = Protections(self.canvas, self.x + i * 36, self.y + j * 36)
                self.protections.append(mur)