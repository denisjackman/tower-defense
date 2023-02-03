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
        self.path = [(-10, 224),  # 0
                     (19, 224),   # 1 
                     (177, 235),  # 2 
                     (282, 283),  # 3 
                     (526, 277),  # 4 
                     (607, 217),  # 5 
                     (641, 105),  # 6 
                     (717, 57),   # 7 
                     (796, 83),   # 8
                     (855, 222),  # 9
                     (940, 252),  #10
                     (973, 284),  #11
                     (1090, 366), #12 
                     (1100, 448), #13 
                     (894, 448),  #14
                     (740, 484),  #15
                     (580, 525),  #16
                     (148, 535),  #17
                     (10, 486),   #18
                     (3, 335),    #19
                     (-100, 335)] #20
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
        self.max_health = 0

    def draw(self, win):
        '''This function draws the enemy.'''
        self.animation_count += 1
        if self.animation_count >= len(self.images) * 3:
            self.animation_count = 0

        self.image = self.images[self.animation_count // 3]
        dx = self.x - (self.image.get_width() / 2)
        dy = self.y - (self.image.get_height() / 2)
        win.blit(self.image, (dx, dy))
        self.draw_health_bar(win)
        #for path in self.path:
        #    pygame.draw.circle(win, (255, 0, 0), (path[0], path[1]), 5,1 )
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
    
    def draw_health_bar(self, win):
        '''This function draws the health bar.'''
        length = 50 
        move_by = round(length / self.max_health)
        health_bar = move_by * self.health
        hbx = self.x - (self.image.get_width()/2)
        hby = self.y -(self.image.get_height()/2) - 5
        pygame.draw.rect(win, (255, 0, 0), (hbx, hby, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (hbx, hby, health_bar, 10), 0)
