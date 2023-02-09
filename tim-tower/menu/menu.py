'''This module contains the Menu class.''''
import pygame

class Menu:
    '''This class represents the menu.'''
    def __init__(self, x, y)~:
        '''This function initializes the menu.'''
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.item_names = []
        self.images = []
        self.items = 0


    def click(self, x, y):
        '''This function checks if the mouse is over a component.'''
        if x <= self.x and x >= self.x + self.width:
            if y <= self.y and y >= self.y + self.height:
                return True
        return False