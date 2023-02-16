''' this is the archer tower class '''
import os
import math
import pygame
from .tower import Tower
from menu.menu import Menu

atltower_images = []
atlarcher_images = []

menu_background = pygame.image.load(os.path.join("game_assets/td-gui/PNG/upgrade","table.png"))
menu_background = pygame.transform.scale(menu_background, (120, 70))

upgrade_button = pygame.image.load(os.path.join("game_assets/td-gui/PNG/upgrade","ico_23.png"))
upgrade_button = pygame.transform.scale(upgrade_button, (50, 50))

for atx in range(3):
    add_str = str(atx + 6)
    asset = f"{os.path.join('game_assets/archer-tower-game-assets/PNG')}/{add_str}.png"
    asset_store = pygame.image.load(asset)
    asset_store = pygame.transform.scale(asset_store, (64, 64))            
    atltower_images.append(asset_store)

for aax in range(6):
    add_str = str(aax + 38)
    asset = f"{os.path.join('game_assets/archer-tower-game-assets/PNG')}/{add_str}.png"
    asset_store = pygame.image.load(asset)
    asset_store = pygame.transform.scale(asset_store, (32, 32))            
    atlarcher_images.append(asset_store)

class ArcherTowerLong(Tower):
    ''' this is the archer tower class '''
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_images = atltower_images[:]
        self.archer_images = atlarcher_images[:]
        self.archer_count = 0
        self.range = 150
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 1
        self.original_damage = self.damage
        self.width = 64 
        self.height == 64
        self.menu = Menu(self, self.x, self.y, menu_background, [2000, 5000, 'MAX'])
        self.menu.add_button(upgrade_button, "Upgrade")  
        self.moving = False
        self.name = "Archer"         
    def get_upgrade_cost(self):
        '''This function returns the upgrade cost.'''
        return self.menu.get_item_cost()

    def draw(self, win):
        '''This function draws the tower.'''
        if self.selected:
            circle_surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA,32)
            pygame.draw.circle(circle_surface, (128, 128, 128, 100), (self.range, self.range), self.range)
            win.blit(circle_surface, (self.x - self.range, self.y - self.range))
        super().draw(win)
        if self.inRange and not self.moving:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_images) * 5  :
                self.archer_count = 0
        else:
            self.archer_count = 0
                        
        archer = self.archer_images[self.archer_count // 5]
        archerx = (self.x + self.width/2) - (archer.get_width()/2) - 32
        archery = (self.y) - (archer.get_height()/2) - 35
        win.blit(archer, (archerx, archery))
    
    def attack(self, enemies):
        '''This function attacks the enemies.'''
        self.inRange = False
        money = 0 
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
            if self.archer_count == 6:
               if first_enemy.hit(self.damage):
                   enemies.remove(first_enemy)
                   money = first_enemy.money * 2
            if first_enemy.x > self.x and not self.left:
                self.left = True
                for x, img in enumerate(self.archer_images):
                    self.archer_images[x] = pygame.transform.flip(img, True, False)
            elif first_enemy.x < self.x and self.left:
                self.left = False
                for x, img in enumerate(self.archer_images):
                    self.archer_images[x] = pygame.transform.flip(img, True, False)
        return money
    def change_range(self, range):
        '''This function gets the range.'''
        self.range = range

atstower_images = []
atsarcher_images = []

for atx in range(3):
    add_str = str(atx + 10)
    asset = f"{os.path.join('game_assets/archer-tower-game-assets/PNG')}/{add_str}.png"
    asset_store = pygame.image.load(asset)
    asset_store = pygame.transform.scale(asset_store, (64, 64))            
    atstower_images.append(asset_store)

for aax in range(6):
    add_str = str(aax + 64)
    asset = f"{os.path.join('game_assets/archer-tower-game-assets/PNG')}/{add_str}.png"
    asset_store = pygame.image.load(asset)
    asset_store = pygame.transform.scale(asset_store, (32, 32))            
    atsarcher_images.append(asset_store)    
class ArcherTowerShort(ArcherTowerLong):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.archer_count = 0
        self.range = 100
        self.inRange = False
        self.left = True
        self.damage = 2
        self.tower_images = atstower_images[:]
        self.archer_images = atsarcher_images[:]
        self.menu = Menu(self, self.x, self.y, menu_background, [2500, 5500, 'MAX'])
        self.menu.add_button(upgrade_button, "Upgrade")
        self.name="Crossbow"
