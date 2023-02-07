'''This is the main game file.'''
import os
import time
import random
import pygame
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard
from tower.archerTower import ArcherTowerLong, ArcherTowerShort
from tower.supportTower import RangeTower, DamageTower
pygame.font.init()

CAPTION = "Tim-Tower"
ICON_FILE = 'y:/Resources/jackmanimation.png'
BACKGROUND = "Y:/tower-defense/tim-tower/game_assets/td-tilesets1-2/tower-defense-game-tilesets/PNG/game_background_2/game_background_2.png"
class Game:
    '''This is the main game class.'''
    def __init__(self) -> None:
        '''This is the init function.'''
        self.width = 1350
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Wizard()]

        self.attack_towers = [ArcherTowerLong(811, 159), 
                       ArcherTowerShort(1044, 381),
                       ArcherTowerLong(696, 381),
                       ArcherTowerShort(231, 458),
                       ArcherTowerLong(493, 630),
                       ArcherTowerShort(900, 584),
                       ArcherTowerLong(119, 130)]
        self.support_towers = [RangeTower(539, 184), DamageTower(1085, 176)]
        self.lives = 10
        self.money = 100
        self.timer = time.time()
        self.background = pygame.image.load(BACKGROUND)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.life_font = pygame.font.SysFont("comicsans", 70)
    
    def run(self):
        '''This is the main game loop.'''
        run = True
        clock = pygame.time.Clock()
        pygame_icon = pygame.image.load(ICON_FILE)
        pygame.display.set_icon(pygame_icon)
        enemycheck = 0 
        while run:
            clock.tick(100)
            if time.time() - self.timer >= random.randrange(1, 5)/2:
                self.timer = time.time()
                self.enemies.append(random.choice([Wizard(), Club(), Scorpion()]))
            if len(self.enemies) == 0:
                pygame.display.set_caption(f"{CAPTION}")
                if enemycheck == 0:
                    self.enemies.append(Wizard())
                    enemycheck = 1
                elif enemycheck == 1:
                    self.enemies.append(Club())
                    enemycheck = 2
                elif enemycheck == 2:
                    self.enemies.append(Scorpion())
                    enemycheck = 0
            else:    
                pygame.display.set_caption(f"{CAPTION} path:{int(self.enemies[0].path_pos)} ")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            enemies_delete = []
            for enemy in self.enemies:
                if enemy.x < -15:
                    enemies_delete.append(enemy)

            for enemy in enemies_delete:
                self.lives -= 1
                self.enemies.remove(enemy)
            for attack_tower in self.attack_towers:
                attack_tower.attack(self.enemies)

            for support_tower in self.support_towers:
                support_tower.support(self.attack_towers)
                
            if self.lives <= 0:
                print("Game Over - you lose")
                run = False
            self.draw()

        pygame.quit()

    def draw(self):
        '''This function draws the game.'''
        self.win.blit(self.background, (0, 0))

        for attack_tower in self.attack_towers:
            attack_tower.draw(self.win)

        for support_tower in self.support_towers:
            support_tower.draw(self.win)

        for enemy in self.enemies:
            enemy.draw(self.win)
        
        text = self.life_font.render(f"{self.lives}", 1, (255, 255, 255))
        life = LIVES_IMAGE
        text = pygame.transform.scale(text, (50, 50))
        start_x = self.width - life.get_width()
        self.win.blit(text, (start_x - text.get_width() - 10 , 10))
        self.win.blit(LIVES_IMAGE, (start_x, 10))

        pygame.display.update()

    def draw_menu(self):
        '''This function draws the menu.'''

        pass

g = Game()
LIVES_IMAGE = pygame.image.load(os.path.join("game_assets/","heart.png")).convert_alpha()
LIVES_IMAGE = pygame.transform.scale(LIVES_IMAGE, (50, 50))
STAR_IMAGE = pygame.image.load(os.path.join("game_assets/","star.png")).convert_alpha()
g.run()
