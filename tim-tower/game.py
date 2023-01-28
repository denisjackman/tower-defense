'''This is the main game file.'''
import os
import pygame
from  enemies.scorpion import Scorpion
from  enemies.club import Club
from  enemies.wizard import Wizard


class Game:
    '''This is the main game class.'''
    def __init__(self) -> None:
        '''This is the init function.'''
        self.width = 930
        self.height = 759
        self.win = pygame.display.set_mode((self.width, self.height))
        #self.enemies = [Scorpion(), Club(), Wizard()]
        #self.enemies = [Scorpion()]
        #self.enemies = [Club()]
        self.enemies = [Wizard()]
        self.towers = []
        self.lives = 10
        self.money = 100
        self.background = pygame.image.load(os.path.join('game_assets', 'background.png'))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
    
    def run(self):
        '''This is the main game loop.'''
        run = True
        clock = pygame.time.Clock()
        while run:
            #pygame.time.delay(250)
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            enemies_delete = []
            for enemy in self.enemies:
                if enemy.x < -5:
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
