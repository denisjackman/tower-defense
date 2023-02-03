''' this is the archer tower class '''
from .tower import Tower
import pygame
import os
import math
import time

class ArcherTowerLong(Tower):
    ''' this is the archer tower class '''
    def __init__(self, x, y):
        super().__init__(x, y)

        self.tower_images = []
        self.archer_images = []
        self.archer_count = 0
        self.range = 150
        self.inRange = False
        self.left = True
        self.timer = time.time()
        self.damage = 1

        for atx in range(4):
            add_str = str(atx + 7)
            asset = f"{os.path.join('game_assets/archer-tower-game-assets/PNG')}/{add_str}.png"
            asset_store = pygame.image.load(asset)
            asset_store = pygame.transform.scale(asset_store, (self.width, self.height))            
            self.tower_images.append(asset_store)

        for aax in range(6):
            add_str = str(aax + 38)
            asset = f"{os.path.join('game_assets/archer-tower-game-assets/PNG')}/{add_str}.png"
            asset_store = pygame.image.load(asset)
            asset_store = pygame.transform.scale(asset_store, (32, 32))            
            self.archer_images.append(asset_store)
    
    def draw(self, win):
        '''This function draws the tower.'''
        circle_surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA,32)
        pygame.draw.circle(circle_surface, (128, 128, 128, 100), (self.range, self.range), self.range)
        win.blit(circle_surface, (self.x - self.range, self.y - self.range))
        
        super().draw(win)
        if self.inRange:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_images) * 10  :
                self.archer_count = 0
        else:
            self.archer_count = 0
                        
        archer = self.archer_images[self.archer_count // 10]
        archerx = (self.x + self.width/2) - (archer.get_width()/2) - 32
        archery = (self.y) - (archer.get_height()/2) - 35
        win.blit(archer, (archerx, archery))


    
    def attack(self, enemies):
        '''This function attacks the enemies.'''
        self.inRange = False
        enemy_closest =[]
        for enemy in enemies:
            enemy_x = enemy.x
            enemy_y = enemy.y
            distance = math.sqrt((enemy_x - self.x)**2 + (enemy_y - self.y)**2)
            if distance < self.range:
                self.inRange = True
                enemy_closest.append(enemy)
        enemy_closest.sort(key=lambda x: x.path_pos, reverse=False)
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if time.time() - self.timer >= 0.5:
               self.timer = time.time()
               if first_enemy.hit():
                   enemies.remove(first_enemy)
            if first_enemy.x > self.x and not self.left:
                self.left = True
                for x, img in enumerate(self.archer_images):
                    self.archer_images[x] = pygame.transform.flip(img, True, False)
            elif first_enemy.x < self.x and self.left:
                self.left = False
                for x, img in enumerate(self.archer_images):
                    self.archer_images[x] = pygame.transform.flip(img, True, False)
            
    def change_range(self, range):
        '''This function gets the range.'''
        self.range = range
    
