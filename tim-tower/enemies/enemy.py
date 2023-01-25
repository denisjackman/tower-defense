import os
import pygame
class Enemy:
    images = []
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.path = []
        self.image = None

    def draw(self, win):
        '''This function draws the enemy.'''
        self.animation_count += 1
        self.image = self.images[self.animation_count]
        if self.animation_count >= len(self.images):
            self.animation_count = 0
        win.blit(self.image, (self.x, self.y))
        self.move()
        
    def collide(self, collide_x, collide_y):
        '''This function checks if the enemy has collided with the tower.'''
        if collide_x <= self.x + self.width and self.x >= collide_x:
            if collide_y <= self.y + self.height and self.y >= collide_y:
                return True
        return False

    def move(self):
        '''This function moves the enemy.'''
        pass
    
    def hit(self):
        '''This function checks if the enemy has been hit.'''
        self.health -= 1
        if self.health <= 0:
            return True
        return False