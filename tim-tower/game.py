'''This is the main game file.'''
import os
import time
import random
import pygame
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard
from tower.archerTower import ArcherTowerLong, ArcherTowerShort
from tower.supportTower import RangeTower, DamageTower
from menu.menu import VerticalMenu, PlayPauseButton

pygame.init()
pygame.font.init()
FRAMERATE = 100
CAPTION = "Tim-Tower"
ICON_FILE = 'y:/Resources/jackmanimation.png'
BACKGROUND = "Y:/tower-defense/tim-tower/game_assets/td-tilesets1-2/tower-defense-game-tilesets/PNG/game_background_2/game_background_2.png"
side_image = pygame.image.load("game_assets/td-gui/PNG/upgrade/window_3.png")
side_image = pygame.transform.scale(side_image, (120, 500))

star = pygame.image.load(os.path.join("game_assets/td-gui/PNG/achievement","star.png"))
star = pygame.transform.scale(star, (50, 50))

buy_damage = pygame.image.load("game_assets/td-gui/PNG/upgrade/ico_2.png")# Damage Upgrade
buy_range = pygame.image.load("game_assets/td-gui/PNG/upgrade/ico_3.png")# Range Upgrade
buy_archer = pygame.image.load("game_assets/td-gui/PNG/upgrade/ico_7.png")# Purchase Archer Tower
buy_archer_2 = pygame.image.load("game_assets/td-gui/PNG/upgrade/ico_8.png")# Purchase Crossbow Tower
buy_damage = pygame.transform.scale(buy_damage, (75, 75))
buy_range = pygame.transform.scale(buy_range, (75, 75))
buy_archer = pygame.transform.scale(buy_archer, (75, 75))
buy_archer_2 = pygame.transform.scale(buy_archer_2, (75, 75))

attack_tower_names = ["Archer", "Crossbow"]
support_tower_names = ["Damage", "Range"]

LIVES_IMAGE = pygame.image.load("game_assets/td-gui/PNG/interface_game/heart.png")
LIVES_IMAGE = pygame.transform.scale(LIVES_IMAGE, (50, 50))
STAR_IMAGE = pygame.image.load("game_assets/td-gui/PNG/interface_game/star.png")

play_button = pygame.image.load("game_assets/td-gui/PNG/interface_game/button_start.png")
pause_button = pygame.image.load("game_assets/td-gui/PNG/interface_game/button_pause.png")
play_button = pygame.transform.scale(play_button, (75, 75))
pause_button = pygame.transform.scale(pause_button, (75, 75))

wave_background = pygame.image.load("game_assets/td-gui/PNG/shop/window_2.png")
wave_background = pygame.transform.scale(wave_background, (230, 80))

waves = [
            [20, 0, 0],
            [50, 0, 0],
            [100, 0, 0],
            [0, 20, 0],
            [0, 50, 0],
            [0, 100, 0],
            [20, 100, 0],
            [50, 100, 0],
            [100, 100, 0],
            [0, 0, 50],
            [20, 0, 100],
            [20, 0, 150],
            [200, 100, 200],
        ]

class Game:
    '''This is the main game class.'''
    def __init__(self) -> None:
        '''This is the init function.'''
        self.width = 1350
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [#Wizard()
                        ]

        self.attack_towers = [#ArcherTowerLong(119, 130),
                              #ArcherTowerShort(231, 458),
                              #ArcherTowerLong(493, 630),
                              #ArcherTowerLong(696, 381),
                              #ArcherTowerLong(900, 584),
                              #ArcherTowerShort(539, 184),
                              #ArcherTowerShort(1085, 176),
                            ]                              
        self.support_towers = [#DamageTower(811, 159), 
                               #DamageTower(900, 584),
                               #RangeTower(1085, 176),
                               #RangeTower(1044, 381),
                               ]
        self.lives = 10
        self.money = 2000
        self.timer = time.time()
        self.background = pygame.image.load(BACKGROUND)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.life_font = pygame.font.SysFont("comicsans", 65)
        self.selected_tower = None
        self.menu = VerticalMenu(self.width -side_image.get_width() + 70, 250 , side_image)
        self.menu.add_button(buy_archer, "Buy_Archer", 500)
        self.menu.add_button(buy_archer_2, "Buy_Crossbow", 750)
        self.menu.add_button(buy_damage, "Buy_Damage", 1000)
        self.menu.add_button(buy_range, "Buy_Support", 1000)
        self.moving_object = False
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.pause = True
        self.playPauseButton = PlayPauseButton(play_button, pause_button, 10, self.height - 85)

    def generate_enemies(self):
        wave_enemy = [
                Scorpion(),
                Wizard(),
                Club(), 
              ]
        if sum(self.current_wave) == 0:
            if len(self.enemies) == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]
                self.pause = True
                self.playPauseButton.paused = True
        else:
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemies.append(wave_enemy[x])
                    self.current_wave[x] -= 1
                    break
    def run(self):
        '''This is the main game loop.'''
        run = True
        clock = pygame.time.Clock()
        pygame_icon = pygame.image.load(ICON_FILE)
        pygame.display.set_icon(pygame_icon)

        while run:
            clock.tick(FRAMERATE)
            position = pygame.mouse.get_pos()
            if self.pause == False:
                if time.time() - self.timer >= random.randrange(1, 6)/3:
                    self.timer = time.time()
                    self.generate_enemies()

            if self.moving_object:
                self.moving_object.move(position[0], position[1])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


                if event.type == pygame.MOUSEBUTTONUP:
                    if self.moving_object:
                        if self.moving_object.name in attack_tower_names:
                            self.attack_towers.append(self.moving_object)
                        elif self.moving_object.name in support_tower_names:
                            self.support_towers.append(self.moving_object)
                        self.moving_object.moving = False
                        self.moving_object = None
                    else:
                        if self.playPauseButton.click(position[0], position[1]):
                            self.pause = not(self.pause)
                            self.playPauseButton.paused = self.pause
                            
                        side_menu_clicked = self.menu.get_clicked(position[0], position[1])
                        button_clicked = None

                        if side_menu_clicked:
                            if self.money >=self.menu.get_item_cost(side_menu_clicked):
                                self.money -= self.menu.get_item_cost(side_menu_clicked)
                                self.add_tower(side_menu_clicked)
                            
                            
                        if self.selected_tower:
                            button_clicked = self.selected_tower.menu.get_clicked(position[0], position[1])
                            if button_clicked:
                                if button_clicked == "Upgrade":
                                    cost = self.selected_tower.get_upgrade_cost()
                                    if self.money >= cost:
                                        self.money -= cost
                                        self.selected_tower.upgrade()
                        if not button_clicked:
                            for tower in self.attack_towers:
                                if tower.click(position[0], position[1]):
                                    tower.selected = True
                                    self.selected_tower = tower
                                else:
                                    tower.selected = False

                            for tower in self.support_towers:
                                if tower.click(position[0], position[1]):
                                    tower.selected = True
                                    self.selected_tower = tower
                                else:
                                    tower.selected = False
            if not(self.pause):
                enemies_delete = []
                for enemy in self.enemies:
                    enemy.move()
                    if enemy.x < -15:
                        enemies_delete.append(enemy)

                for enemy in enemies_delete:
                    self.lives -= 1
                    self.enemies.remove(enemy)
                for attack_tower in self.attack_towers:
                    self.money += attack_tower.attack(self.enemies)

                for support_tower in self.support_towers:
                    support_tower.support(self.attack_towers)
                    
                if self.lives <= 0:
                    print("Game Over - you lose")
                    run = False
            self.draw()

        pygame.quit()

    def draw(self):
        '''This function draws the game.'''
        self.win.blit(self.background, (0, 0))

        for attack_tower in self.attack_towers:
            attack_tower.draw(self.win)

        for support_tower in self.support_towers:
            support_tower.draw(self.win)

        for enemy in self.enemies:
            enemy.draw(self.win)

        if self.moving_object:
            self.moving_object.draw(self.win)
        
        self.menu.draw(self.win)
        self.playPauseButton.draw(self.win)
 
        text = self.life_font.render(f"{self.lives}", 1, (255, 255, 255))
        life = LIVES_IMAGE
        start_x = self.width - life.get_width()
        self.win.blit(text, (start_x - text.get_width() - 10 , 5))
        self.win.blit(LIVES_IMAGE, (start_x, 20))

        text = self.life_font.render(f"{self.money}", 1, (255, 255, 255))
        currency = star
        start_x = self.width - currency.get_width()
        self.win.blit(text, (start_x - text.get_width() - 10 , 55))
        self.win.blit(currency, (start_x, 70))
        
        self.win.blit(wave_background, (10,10))
        text = self.life_font.render(f"Wave #{self.wave}", 1, (255, 255, 255))
        text = pygame.transform.scale(text, (220, 70))
        self.win.blit(text, (10 + (wave_background.get_width()/2 - text.get_width()/2) , 10))
        pygame.display.update()

    def add_tower(self, name):
        '''This function adds a tower to the game.'''
        x, y = pygame.mouse.get_pos()
        name_list = ["Buy_Archer", "Buy_Crossbow", "Buy_Damage", "Buy_Support"]
        object_list = [ArcherTowerLong(x,y), ArcherTowerShort(x,y), DamageTower(x,y), RangeTower(x,y)]
        try:
            object = object_list[name_list.index(name)]
            self.moving_object = object
            object.move(x,y)
            object.moving = True
        except Exception as e:
            print(f"Error: {e}: invalid name")

if __name__ == "__main__":
    g = Game()
    g.run()
