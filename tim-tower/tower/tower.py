'''This is the tower class.'''
import os
import pygame
from menu.menu import Menu

menu_background = pygame.image.load(os.path.join("game_assets/td-gui/PNG/upgrade","table.png"))
menu_background = pygame.transform.scale(menu_background, (120, 70))

upgrade_button = pygame.image.load(os.path.join("game_assets/td-gui/PNG/upgrade","ico_23.png"))
upgrade_button = pygame.transform.scale(upgrade_button, (50, 50))

class Tower():
    '''This is the tower class.'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        self.tower_images = []
        self.damage = 1
        self.menu = Menu(self, self.x, self.y, menu_background, [2000, 'MAX'])
        self.menu.add_button(upgrade_button, "Upgrade")        
    
    def draw(self, win):
        '''This function draws the tower.'''
        image = self.tower_images[self.level-1]
        win.blit(image, (self.x - image.get_width()//2, self.y - image.get_height()//2))
        if self.selected:
            self.menu.draw(win)
    
    def draw_radious(self, window):
        '''This function draws the range of the tower.'''
        if self.selected:
            circle_surface = pygame.Surface((self.radius*4, self.radius*4), pygame.SRCALPHA,32)
            pygame.draw.circle(circle_surface, (128, 128, 128, 100), (self.radius, self.radius), self.radius)
            window.blit(circle_surface, (self.x - self.radius, self.y - self.radius))        
    
    def old_click(self, x ,y):
        '''This function checks if the tower has been clicked.'''
        if x <= self.x + self.width and self.x >= x:
            if y <= self.y + self.height and self.y >= y:
                return True
        return False

    def click(self, X, Y):
        """
        returns if tower has been clicked on
        and selects tower if it was clicked
        :param X: int
        :param Y: int
        :return: bool
        """
        img = self.tower_images[self.level - 1]
        dx =  self.x - img.get_width()//2 + self.width
        dx1 = self.x - img.get_width()//2
        dy = self.y + self.height - img.get_height()//2
        dy1 = self.y - img.get_height()//2
        if X <= dx and X >= dx1:
            if Y <= dy and Y >= dy1:
                return True            
        return False

    def sell(self):
        '''This function sells the tower.'''
        return self.sell_price[self.level-1]
    
    def upgrade(self):
        '''This function upgrades the tower.'''
        if self.level < len(self.tower_images):
            self.level += 1
            self.damage += 1
    
    def get_upgrade_cost(self):
        '''This function gets the upgrade cost of the tower.'''
        return self.price[self.level]
    
    def move(self, x, y):
        '''This function moves the tower.'''
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()
    