"""Classe Soldat
Par : Pirès-Portelada Yanis et Bovet Gauthier
Lieu : CPE Lyon
Date : 18 Novembre 2024
Codé en : Python sur VS code"""


from gameClass.entity import Entities
from gameClass.projectile import Projectile

class Soldat(Entities):

    def __init__(self, canvas, pos, img, hp, cooldown):
        super().__init__(canvas, pos, img, hp)
        self.dx = 30
        self.show()

    def move(self, dx): 
        self.pos[0] += dx 
        if self.pos[0] <= 10:   #Permet de limiter les déplacements (à gauche) du soldat dans la fenêtre de jeu 
            self.pos[0] = 10
            dx = 0

        if self.pos[0] >= 790:  #Permet de limiter les déplacements (à droite) du soldat dans la fenêtre de jeu
            self.pos[0] = 790
            dx = 0
        if self.image_id is not None:  # Vérifier si l'image est bien créée
            self.canvas.move(self.image_id, dx, 0)
            
    def shoot(self):

        self.bullet = Projectile(canvas=self.canvas,pos=(self.pos[0] + 7, self.pos[1] - 35), img="TankInvadersV0/Images/bullet_soldier.png",speed=-5, direction=-1) #Création du projectile
        self.bullets.append(self.bullet) #Ajoute le projectile à la liste des projectiles
        
        for bullets in self.bullets :
            bullets.animate()
            
    def checkdeath(self):
        if self.hp <= 0:
            self.canvas.delete()