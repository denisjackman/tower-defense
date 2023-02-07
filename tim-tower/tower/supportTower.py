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
        self.radius = 150
        self.tower_images = range_images[:]
        self.effect = [0.2, 0.4]
        
    def draw(self, window):
        ''' this draws the range tower '''
        super().draw_radious(window)
        super().draw(window)
    
    def support(self, towers):
        ''' this function supports the tower '''
        pass
        
class DamageTower(RangeTower):
    ''' this is the damage tower class '''
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 150
        self.tower_images = damage_images[:]
        self.effect = [1, 2]

    def support(self, towers):
        ''' this function supports the tower '''
        pass    