'''This is the main game file.'''
import os
import pygame
class Game:
    '''This is the main game class.'''
    def __init__(self) -> None:
        '''This is the init function.'''
        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 10
        self.money = 100
        self.background = pygame.image.load(os.path.join('game_assets', 'background.png'))
        self.clicks = []
    
    def run(self):
        '''This is the main game loop.'''
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                pos = pygame.mouse.get_pos()
                self.clicks.append(pos)
                print(f"Position : {pos}")
            self.draw()
        pygame.quit()

    def draw(self):
        '''This function draws the game.'''
        self.win.blit(self.background, (0, 0))
        for item in self.clicks:
            pygame.draw.circle(self.win, (255, 0, 0), item, 5, 1)
        pygame.display.update()

g = Game()
g.run()
