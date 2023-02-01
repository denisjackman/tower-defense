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
        self.path = [(-10, 224),(19, 224), (177, 235), (282, 283), (526, 277), (607, 217), (641, 105), (717, 57), (796, 83), (855, 222), (973, 284), (1046, 366), (1022, 458), (894, 492), (740, 504), (580, 542), (148, 541), (10, 442), (-20, 335), (-75, 305), (-100, 345)]
        #self.path = [(1, 225), (200, 231), (280, 280), (644, 263), (666, 231), (683, 193), (710, 121), (755, 80), (787, 47), (868, 58), (909, 93), (937, 154), (936, 195), (967, 231), (994, 263), (1013, 273), (1074, 278), (1119, 297), (1154, 331), (1169, 370), (1173, 414), (1141, 452), (1106, 495), (843, 507), (785, 535), (748, 552), (696, 551), (551, 550), (193, 546), (135, 504), (92, 432), (51, 361), (5, 339)] 
        #self.path = [(1, 341), (71, 376), (95, 437), (110, 488), (134, 528), (166, 551), (768, 554), (801, 524), (851, 501), (1090, 498), (1138, 476), (1160, 437), (1170, 398), (1171, 360), (1156, 331), (1125, 304), (1082, 291), (1044, 282), (1007, 266), (975, 246), (950, 220), (927, 165), (914, 117), (875, 71), (819, 48), (770, 69), (735, 97), (716, 137), (705, 190), (674, 230), (646, 262), (239, 263), (191, 236), (145, 234), (9, 233), (2, 236)]
        #self.path =[(380, 743), (384, 631), (386, 477), (465, 437), (471, 336), (450, 301), (153, 297), (131, 338), (130, 422), (152, 454), (168, 463), (212, 497), (211, 590), (252, 629), (381, 630), (377, 741)]
        #self.path = [(460, 401), (460, 401), (460, 401), (460, 401), (460, 401), (460, 401), (460, 401), (460, 401), (460, 401)]
        #self.path = [(698, 417), (122, 419), (117, 286), (682, 287), (698, 417)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.distance = 0 
        self.image = None
        self.path_pos = 0
        self.move_count = 0
        self.move_distance = 0
        self.images = []
        self.flipped = False 
        self.speed_increase = 1.2

    def draw(self, win):
        '''This function draws the enemy.'''
        self.animation_count += 1
        if self.animation_count >= len(self.images) * 3:
            self.animation_count = 0

        self.image = self.images[self.animation_count // 3]
        win.blit(self.image, (self.x - (self.image.get_width()/2), self.y -(self.image.get_height()/2)))
        self.move()
        
    def collide(self, collide_x, collide_y):
        '''This function checks if the enemy has collided with the tower.'''
        if collide_x <= self.x + self.width and self.x >= collide_x:
            if collide_y <= self.y + self.height and self.y >= collide_y:
                return True
        return False

    def other_move(self):
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
    def move(self):
        """
        Move enemy
        :return: None
        """
        self.animation_count += 1
        if self.animation_count >= len(self.images):
            self.animation_count = 0

        x1, y1 = self.path[self.path_pos]
        x1 = x1 + 75
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 355)
        else:
            x2, y2 = self.path[self.path_pos+1]

        x2 = x2+75

        dirn = ((x2-x1)*2, (y2-y1)*2)
        length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
        dirn = (dirn[0]/length * self.speed_increase, dirn[1]/length * self.speed_increase)

        if dirn[0] < 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.images):
                self.images[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))

        self.x = move_x
        self.y = move_y

        # Go to next point
        if dirn[0] >= 0: # moving right
            if dirn[1] >= 0: # moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else: # moving left
            if dirn[1] >= 0:  # moving down
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1

    def hit(self):
        '''This function checks if the enemy has been hit.'''
        self.health -= 1
        if self.health <= 0:
            return True
        return False