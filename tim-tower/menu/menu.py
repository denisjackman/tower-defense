'''This module contains the Menu class.'''
import os
import pygame
pygame.font.init()
star = pygame.image.load(os.path.join("game_assets/td-gui/PNG/achievement","star.png"))
star = pygame.transform.scale(star, (50, 50))
star2 = pygame.transform.scale(star, (20, 20))

class Button:
    def __init__(self, menu, image, name):
        self.menu = menu
        self.x = menu.x - 50
        self.y = menu.y - 90 
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.name = name
        
    def click(self, x, y):
        '''This function checks if the mouse is over a component.'''
        if x <= self.x + self.width and x >= self.x:
            if y <= self.y +self.height and y >= self.y:
                return True
        return False

    def draw(self, win):
        '''This function draws the button.'''
        win.blit(self.image, (self.x, self.y))

    def update(self):
        '''This function updates the button.'''
        self.x = self.menu.x - 50 
        self.y = self.menu.y - 90
class VerticalButton(Button):
    '''This class represents a vertical button.'''
    def __init__(self, x, y, image, name, cost):
        self.x = x
        self.y = y
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.name = name
        self.cost = cost
       
class Menu:
    '''This class represents the menu.'''
    def __init__(self, tower,  x, y, image, item_cost):
        '''This function initializes the menu.'''
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()
        self.item_names = []
        self.item_cost = item_cost
        self.items = 0
        self.buttons = []
        self.background = image
        self.font = pygame.font.SysFont("comicsans", 20)
        self.tower = tower

    def add_button(self, image, name):
        '''This function adds a button to the menu.'''
        self.items += 1
        button_x = self.x - self.background.get_width()/2 + 10
        button_y = self.y - 100 + 10 
        button = Button(self, image, name)
        self.buttons.append(button)
        self.item_names.append(name)
    def get_item_cost(self):
        '''This function returns the cost of the item.'''
        return self.item_cost[self.tower.level -1]

    def click(self, x, y):
        '''This function checks if the mouse is over a component.'''
        if x <= self.x and x >= self.x + self.width:
            if y <= self.y and y >= self.y + self.height:
                return True
        return False
        
    def draw(self, win):
        '''This function draws the menu.'''
        dx = self.x - self.background.get_width()/2
        dy = self.y - 100
        win.blit(self.background, (dx, dy))
        for item in self.buttons:
            item.draw(win)
            win.blit(star, (item.x + item.width + 5, item.y - 10))
            text = self.font.render(f"{self.item_cost[self.tower.level -1]}", 1, (255, 255, 255))
            win.blit(text, (item.x + item.width , item.y + star.get_height() - 20))
    
    def get_clicked(self, x, y):
        '''This function returns the clicked item.'''
        for item in self.buttons:
            if item.click(x, y):
                return item.name
        
        return None
    
    def update (self):
        '''This function updates the menu.'''
        for item in self.buttons:
            item.update()

class VerticalMenu(Menu):
    '''This class represents the vertical menu.'''
    def __init__(self, x, y, image):
        '''This function initializes the menu.'''
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()
        self.item_names = []
        self.items = 0
        self.buttons = []
        self.background = image
        self.font = pygame.font.SysFont("comicsans", 20)

    def add_button(self, image, name, cost):
        '''This function adds a button to the menu.'''
        self.items += 1
        button_x = self.x - 40
        button_y = (self.y - 90  + (self.items -1) * 120)
        button = VerticalButton(button_x, button_y, image, name, cost)
        self.buttons.append(button)
        self.item_names.append(name)
        
    def get_item_cost(self, name):
        '''This function returns the cost of the item.'''
        for item in self.buttons:
            if item.name == name:
                return item.cost
        return Exception(f"{name} does not have item cost")
    
    def draw(self, win):
        '''This function draws the menu.'''
        dx = self.x - self.background.get_width()/2
        dy = self.y - 100
        win.blit(self.background, (dx, dy))
        for item in self.buttons:
            item.draw(win)
            win.blit(star2, (item.x, item.y + item.height))
            text = self.font.render(f"{item.cost}", 1, (255, 255, 255))
            win.blit(text, (item.x +item.width/2 - text.get_width()/2 + 5, item.y + item.height + 2))
            
class PlayPauseButton(Button):
    def __init__(self, play_image, pause_image, x, y):
        self.x = x
        self.y = y
        self.play = play_image
        self.image = play_image
        self.pause = pause_image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.paused = True
        
    def draw(self, window):
        if self.paused: 
            window.blit(self.play, (self.x, self.y))
        else:
            window.blit(self.pause, (self.x, self.y))
