from gameClass.entity import Entities
class Soldat(Entities):

    # def __init__(self, canvas, pos, img, hp, size, fproj):
    #     super().__init__(canvas, pos, img, hp, size, fproj=fproj)
    def __init__(self, canvas, pos, img, hp):
        super().__init__(canvas, pos, img, hp)
        # self.timer = 0  #Mise en place d'un cooldown 
        self.show()
        self.bullets = []
        self.dx = 30

    # def move(self, dx): #ATTENTION CHANGER NOM DE VARIABLE CAR PAS UTILE AU MOVE MAIS A L'ENCADREMENT 
    #     self.pos[0] = self.pos[0] + dx 
    #     if self.pos[0] <= 10:
    def move(self, dx): 
        self.pos[0] += dx 
        if self.pos[0] <= 10:   #Permet de limiter les déplacements (à gauche) du soldat dans la fenêtre de jeu 
            self.pos[0] = 10
            dx = 0
        # if self.pos[0] >= 790:
        if self.pos[0] >= 790:  #Permet de limiter les déplacements (à droite) du soldat dans la fenêtre de jeu 
            self.pos[0] = 10
            self.pos[0] = 790
            dx = 0
        if self.image_id is not None:  # Vérifier si l'image est bien créée
            self.canvas.move(self.image_id, dx, 0)
            
    # def shoot(self):
    
          
    # def shoot(self):