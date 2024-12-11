from gameClass.protections import Protections

class Wall:
    def __init__(self, canvas, x, y, img, hp, rows=4, cols=4, block_size=36):
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
                pos_y = self.y + row * self.block_size
                protection = Protections(self.canvas, (pos_x, pos_y), self.img, self.hp)    #Crée une protection et l'ajoute à la liste
                self.blocks.append(protection)

    def check_collision(self, projectile_coords):
        for protection in self.blocks:
            if protection.hp > 0:  #Permet de prendre en compte seulement les protections encore en vie
                protection_coords = protection.get_coords()
                if protection_coords and self._is_colliding(protection_coords, projectile_coords):
                    protection.loss_hp()
                    return True 
        return False
    
    #Non présence de self car utilisation d'une méthode statique (pratique pour les collisions)
    def _is_colliding(coords1, coords2):    #Permet de vérifie si deux rectangles se chevauchent
        x1, y1, x2, y2 = coords1
        px1, py1, px2, py2 = coords2
        return not (x2 < px1 or px2 < x1 or y2 < py1 or py2 < y1)
    
    def remove_destroyed_protections(self): #Retire les protections qui sont détruites de la liste self.blocks
        self.blocks = [p for p in self.blocks if p.hp > 0]

    def is_destroyed(self): #Vérifie si toutes les protections du mur sont détruites (Utile si l'on veut reconstruire les murs à la fin d'un niveau)
        return len(self.blocks) == 0
    
    def rebuild(self):
        self.blocks = []  # Réinitialise la liste des protections
        self.create()