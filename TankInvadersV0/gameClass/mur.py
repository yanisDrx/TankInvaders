"""Classe Mur
Par : Pirès-Portelada Yanis et Bovet Gauthier
Lieu : Domicile (Lyon)
Date : 7 Décembre 2024
Codé en : Python sur VS code"""


from gameClass.protections import Protections

class Wall:
    def __init__(self, canvas, x, y, img, hp, rows=3, cols=4, block_size=36):
        self.canvas = canvas
        self.x = x  #Coordonnée x de départ du mur 
        self.y = y  #Coordonnée y de départ du mur
        self.img = img  #Image associée à la protection
        self.hp = hp    #Point de vie pour chaque protection
        self.rows = rows    #Nombre de ligne dans le mur
        self.cols = cols    #Nombre de colonne dans le mur
        self.block_size = block_size    #Taille d'un mur x par y
        self.blocks = []  #Liste pour stocker toutes les protections
        self.create()
    
    def create(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pos_x = self.x + col * self.block_size
                pos_y = self.y + row * (self.block_size - 20)
                protection = Protections(self.canvas, (pos_x, pos_y), self.img, self.hp)    #Crée une protection et l'ajoute à la liste
                self.blocks.append(protection)

    def get_coords(self):
            # Retourne les coordonnées de l'image sous forme de bbox (bounding box)
            return [block.get_coords() for block in self.blocks]
    
    def check_collision(self, coords):
        """Vérifie les collisions avec un projectile ou un tank"""
        for protection in self.blocks:
            if protection.hp > 0:  # Vérifie si la protection est toujours en vie
                protection_coords = protection.get_coords()
                if protection_coords and self._is_colliding(protection_coords, coords):
                    protection.loss_hp()  # Diminue les HP de la protection
                    return True 
        return False

    def _is_colliding(self, coords1, coords2):    # Vérifie si deux rectangles se chevauchent
        x1, y1, x2, y2 = coords1
        px1, py1, px2, py2 = coords2
        return not (x2 < px1 or px2 < x1 or y2 < py1 or py2 < y1)
    # def check_collision(self, projectile_coords):
    #     for protection in self.blocks:
    #         if protection.hp > 0:  #Permet de prendre en compte seulement les protections encore en vie
    #             protection_coords = protection.get_coords()
    #             if protection_coords and self._is_colliding(protection_coords, projectile_coords):
    #                 protection.loss_hp()
    #                 return True 
    #     return False
    
    # #Non présence de self car utilisation d'une méthode statique (pratique pour les collisions)
    # def _is_colliding(coords1, coords2):    #Permet de vérifie si deux rectangles se chevauchent
    #     x1, y1, x2, y2 = coords1
    #     px1, py1, px2, py2 = coords2
    #     return not (x2 < px1 or px2 < x1 or y2 < py1 or py2 < y1)
    
    def remove_destroyed_protections(self): #Retire les protections qui sont détruites de la liste self.blocks
        self.blocks = [p for p in self.blocks if p.hp > 0]

    def is_destroyed(self): #Vérifie si toutes les protections du mur sont détruites (Utile si l'on veut reconstruire les murs à la fin d'un niveau)
        return len(self.blocks) == 0
    
    def rebuild(self):
        self.blocks = []  # Réinitialise la liste des protections
        self.create()