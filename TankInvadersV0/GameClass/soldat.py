from gameClass.entity import Entities
from gameClass.projectile import Projectile
from time import time

class Soldat(Entities):

    def __init__(self, canvas, pos, img, hp, size, cooldown):
        super().__init__(canvas, pos, img, hp, size)
        self.last_shot_time = 0 #Temps du dernier tir
        self.bullets = []   #Liste des projectiles présents
        self.cooldown = cooldown  #Temps minimum entre deux tirs (en ms)

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
        # current_time = int(self.canvas.winfo_toplevel().tk.call('after', 'info').split()[0]) if self.canvas else 0
        current_time = int(time.time() * 1000)
        if current_time - self.last_shot_time < self.cooldown:  #Vérifie si le soldat est en capacité de tirer , si cette condition est vraie le soldat n'a pas le possibilité de tirer
            return  

        self.last_shot_time = current_time  # Met à jour le dernier temps de tir

        bullet_x = self.pos[0]  # Position x centrée sur le soldat
        bullet_y = self.pos[1] - (self.size[1] // 2)  # Position y au-dessus du soldat
        bullet = Projectile(canvas=self.canvas,pos=(bullet_x, bullet_y), img="TankInvadersV0/Images/soldier_player.png", size=(5, 10),speed=-5) #Création du projectile
        self.bullets.append(bullet) #Ajoute le projectile à la liste des projectiles
          
