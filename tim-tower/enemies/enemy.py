import os
import math
import pygame

class Enemy:
    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.velocity = 3
        #self.path =[(380, 743), (384, 631), (386, 477), (465, 437), (471, 336), (450, 301), (153, 297), (131, 338), (130, 422), (152, 454), (168, 463), (212, 497), (211, 590), (252, 629), (381, 630), (377, 741)]
        #self.path = [(460, 401), (460, 401), (460, 401), (460, 401), (460, 401), (460, 401), (460, 401), (460, 401), (460, 401)]
        self.path = [(698, 417), (122, 419), (117, 286), (682, 287), (698, 417)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.distance = 0 
        self.image = None
        self.path_pos = 0
        self.move_count = 0
        self.move_distance = 0
        self.images = []
        self.flipped = False 

    def draw(self, win):
        '''This function draws the enemy.'''
        self.animation_count += 1
        if self.animation_count >= len(self.images) * 3:
            self.animation_count = 0

        self.image = self.images[self.animation_count // 3]
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
        x1,y1  = self.path[self.path_pos]
        if self.path_pos +1 >= len(self.path):
            self.path_pos = 0
            x2, y2 = self.path[1]
            x1, y1 = self.path[0]
        else:
            x2,y2 = self.path[self.path_pos + 1]
        move_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        direction = (x2 - x1, y2 - y1)
        length = math.sqrt(direction[0] ** 2 + direction[1] ** 2)
        direction = (direction[0] / length, direction[1] / length)
        if direction[0] < 0 and self.flipped == False:
            self.flipped = True
            for image_count, image in enumerate(self.images):
                self.images[image_count] = pygame.transform.flip(image, True, False)
        if direction[0] > 0 and self.flipped == True:
            self.flipped = False
            for image_count, image in enumerate(self.images):
                self.images[image_count] = pygame.transform.flip(image, True, False)
            
        length = math.sqrt(direction[0] ** 2 + direction[1] ** 2)
        if length == 0: 
            length = 1
        direction = (direction[0] / length, direction[1] / length)
        
        move_x, move_y = (self.x + direction[0] ), (self.y + direction[1])        

        self.distance = math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)
        
        if self.distance >= move_distance:
            self.distance = 0 
            self.move_count = 0
            self.path_pos += 1
            if self.path_pos >= len(self.path):
                self.path_pos = 0 

        self.x = move_x
        self.y = move_y

    def hit(self):
        '''This function checks if the enemy has been hit.'''
        self.health -= 1
        if self.health <= 0:
            return True
        return False