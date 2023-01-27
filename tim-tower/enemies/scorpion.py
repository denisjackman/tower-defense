import os
import pygame
from .enemy import Enemy

class Scorpion(Enemy):
    images = []
    for x in range(20):
        add_str = str(x) 
        if x < 10:
            add_str = '0' + str(x)
            asset = f"{os.path.join('game_assets/2d-monster-sprites/PNG/1')}/1_enemies_1_run_0{add_str}.png"
            images.append(pygame.image.load(asset))

    def __init__(self):
        super().__init__()