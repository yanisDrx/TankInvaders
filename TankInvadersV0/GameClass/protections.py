from gameClass.entity import Entities

class Protections (Entities):
    # def __init__(self, canvas, pos, img):
    #     super().__init__(self, canvas, pos, img, hp=1)
    
    def __init__(self, canvas, pos, img, hp):
        super().__init__(canvas, pos, img, hp=hp, size=None)
        self.protection = self.image_id
        self.protection = self.canvas.create_image(self.pos[0], self.pos[1], image=self.img)

    def loss_hp(self):
        if self.hp > 0: #Permet de vérifier si la protection existe toujours
            self.hp -= 1
            if self.hp <= 0:
                self.delete()
    def delete(self):
        # self.canvas.delete(self.protection)
        
        if self.image_id is not None:   #Permet de vérifier si l'objet existe  
            self.canvas.delete(self.protection)
            # self.protection = None  #Empêche une double suppresion

    def get_coords(self):
        # self.pos = self.canvas.coords(self.brick)
        # x1 = self.pos[0] - 18
        # y1 = self.pos[1] - 18
        # x2 = x1 + 36
        # y2 = y1 + 36
        # return x1, y1, x2, y2
        bbox = self.canvas.bbox(self.protection)    #Récupère les coordonnées de l'objet, ici la protection
        if bbox is not None:
            return bbox
        else:
            return None #Si jamais l'objet n'existe pas 