'''This is the main game file.'''
import os
import pygame
from  enemies.scorpion import Scorpion
from  enemies.club import Club
from  enemies.wizard import Wizard

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
        #self.enemies = [Scorpion(), Club(), Wizard()]
        #self.enemies = [Scorpion()]
        self.enemies = [Club()]
        #self.enemies = [Wizard()]
        self.towers = []
        self.lives = 10
        self.money = 100
        self.background = pygame.image.load(BACKGROUND)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
    
    def run(self):
        '''This is the main game loop.'''
        run = True
        clock = pygame.time.Clock()
        pygame_icon = pygame.image.load(ICON_FILE)
        pygame.display.set_icon(pygame_icon)
        while run:
            pygame.display.set_caption(f"{CAPTION} x:{int(self.enemies[0].x)} y:{int(self.enemies[0].y)}")
            #pygame.time.delay(250)
            clock.tick(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            enemies_delete = []
            for enemy in self.enemies:
                pass
                if enemy.x < -15:
                    enemies_delete.append(enemy)
            for enemy in enemies_delete:
                self.enemies.remove(enemy)
            self.draw()
        pygame.quit()

    def draw(self):
        '''This function draws the game.'''
        self.win.blit(self.background, (0, 0))
        for enemy in self.enemies:
            enemy.draw(self.win)

        pygame.display.update()

g = Game()
g.run()
