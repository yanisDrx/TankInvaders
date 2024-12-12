"""Classe Protections
Par : Pirès-Portelada Yanis et Bovet Gauthier
Lieu : Domicile (Lyon)
Date : 7 Décembre 2024
Codé en : Python sur VS code"""

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

    def get_coords(self):
        # On vérifie si l'image existe avant de récupérer les coordonnées
        if self.image_id is not None:
            bbox = self.canvas.bbox(self.image_id)  # Récupère les coordonnées de l'objet, ici la protection
        #     if bbox:
        #         return bbox
        # return None  # Si l'objet n'existe plus, retourne None