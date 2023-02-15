''' this is the support tower class '''
import os
import math
import pygame
from .tower import Tower

range_images = []
damage_images = []

for rtx in range(2):
    add_str = str(rtx + 4)
    asset = f"{os.path.join('game_assets/support-tower-game-assets/PNG')}/{add_str}.png"
    asset_store = pygame.image.load(asset)
    asset_store = pygame.transform.scale(asset_store, (64, 64))            
    range_images.append(asset_store)

for dtx in range(2):
    add_str = str(dtx + 8)
    asset = f"{os.path.join('game_assets/support-tower-game-assets/PNG')}/{add_str}.png"
    asset_store = pygame.image.load(asset)
    asset_store = pygame.transform.scale(asset_store, (64, 64))            
    damage_images.append(asset_store)

class RangeTower(Tower):
    ''' this is the range tower class'''
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 300
        self.tower_images = range_images[:]
        self.effect = [0.2, 0.4]
        self.width = 64 
        self.height = 64
        self.name = 'Range'
        
    def draw(self, window):
        ''' this draws the range tower '''
        super().draw_radious(window)
        super().draw(window)
    
    def support(self, towers):
        ''' this function supports the tower '''
        affected = []
        for tower in towers:
            tower_x = tower.x
            tower_y = tower.y
            distance = math.sqrt((tower_x - self.x)**2 + (tower_y - self.y)**2)
            if distance < self.radius + tower.width/2:
                self.inRange = True
                affected.append(tower) 
        for tower in affected:
            tower.range = tower.original_damage + round(tower.range * self.effect[self.level - 1])
        
class DamageTower(RangeTower):
    ''' this is the damage tower class '''
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 300
        self.tower_images = damage_images[:]
        self.effect = [1, 2]
        self.width = 64
        self.height = 64
        self.name = 'Damage'

    def support(self, towers):
        ''' this function supports the tower '''
        affected = []
        for tower in towers:
            tower_x = tower.x
            tower_y = tower.y
            distance = math.sqrt((tower_x - self.x)**2 + (tower_y - self.y)**2)
            if distance < self.radius + tower.width/2:
                self.inRange = True
                affected.append(tower) 
        for tower in affected:
            tower.damage = tower.original_damage + round(tower.original_damage * self.effect[self.level - 1])