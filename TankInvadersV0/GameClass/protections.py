from gameClass.entity import Entities

class Protections (Entities):
    def __init__(self, canvas, pos, img, hp):
        super().__init__(canvas, pos, img, hp=hp)
       
        self.show()
        
        
    def loss_hp(self):
        if self.hp > 0: #Permet de vérifier si la protection existe toujours
            self.hp -= 1
            if self.hp <= 0:
                self.delete()
                
            
    def delete(self):
        if self.image_id is not None:   #Permet de vérifier si l'objet existe  
            self.canvas.delete(self.image_id)
            self.image_id = None  #Empêche une double suppresion
