import os
import pygame
from .enemy import Enemy
images = []
for x in range(20):
    add_str = str(x) 
    if x < 10:
        add_str = '0' + str(x)
    asset = f"{os.path.join('game_assets/2d-monster-sprites/PNG/5')}/5_enemies_1_run_0{add_str}.png"
    asset_store = pygame.image.load(asset)
    asset_store = pygame.transform.scale(asset_store, (64, 64))            
    images.append(asset_store)
class Club(Enemy):

    def __init__(self):
        super().__init__()
        self.images = []
        self.max_health = 5
        self.health = self.max_health
        self.images = images[:]
        self.name = 'club'
        self.money = 5