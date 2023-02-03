'''This is the tower class.'''
import pygame

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
        self.menu = None
        self.tower_images = []
        self.damage = 1
    
    def draw(self, win):
        '''This function draws the tower.'''
        image = self.tower_images[self.level-1]
        win.blit(image, (self.x - image.get_width()//2, self.y - image.get_height()//2))
    
    def click(self, x ,y):
        '''This function checks if the tower has been clicked.'''
        if x <= self.x + self.width and self.x >= x:
            if y <= self.y + self.height and self.y >= y:
                return True
        return False

    def sell(self):
        '''This function sells the tower.'''
        return self.sell_price[self.level-1]
    
    def upgrade(self):
        '''This function upgrades the tower.'''
        self.level += 1
        self.damage += 1
    
    def get_upgrade_cost(self):
        '''This function gets the upgrade cost of the tower.'''
        return self.price[self.level]
    
    def move(self, x, y):
        '''This function moves the tower.'''
        self.x = x
        self.y = y
    
    