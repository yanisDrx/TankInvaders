# from gameClass.entity import Entities
# from gameClass.projectile import Projectile
# from gameClass.protections import Protections
# from gameClass.soldat import Soldat
# from gameClass.tanks import Tank


# class CollisionManager:

#     @staticmethod
#     def checkCollision(entity1, entity2):   #Vérifie si deux entités sont en collision en comparant leurs bbox

#         bbox1 = entity1.get_coords()
#         bbox2 = entity2.get_coords()

#         if not bbox1 or not bbox2:
#             return False  # Une des entités n'a pas de bounding box (peut-être supprimée)

#         x1, y1, x2, y2 = bbox1
#         tx1, ty1, tx2, ty2 = bbox2

#         return not (x2 < tx1 or x1 > tx2 or y2 < ty1 or y1 > ty2)

#     @staticmethod
#     def checkAllCollisions(entities1, entities2):   # Vérifie les collisions entre deux entités.

#         collisions = []
#         for entity1 in entities1:
#             for entity2 in entities2:
#                 if CollisionManager.checkCollision(entity1, entity2):
#                     collisions.append((entity1, entity2))
#         return collisions



#     def handle_collisions(projectiles, protections):
#         collisions = CollisionManager.checkAllCollisions(projectiles, protections)

#         for projectile, protection in collisions:
#             # Supprime le projectile
#             projectile.delete()
#             if projectile in projectiles:
#                 projectiles.remove(projectile)

#             # Réduit les points de vie de la protection
#             protection.loss_hp()
#             if protection.hp <= 0 and protection in protections:
#                 protections.remove(protection)
