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
from menu.menu import VerticalMenu
pygame.font.init()

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

class Game:
    '''This is the main game class.'''
    def __init__(self) -> None:
        '''This is the init function.'''
        self.width = 1350
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Wizard()]

        self.attack_towers = [ArcherTowerLong(119, 130),
                              ArcherTowerShort(231, 458),
                              ArcherTowerLong(493, 630),
                              ArcherTowerLong(696, 381),
                              ArcherTowerLong(900, 584),
                              ArcherTowerShort(539, 184),
                              ArcherTowerShort(1085, 176),
                            ]                              
        self.support_towers = [DamageTower(811, 159), 
                               #DamageTower(900, 584),
                               #RangeTower(1085, 176),
                               RangeTower(1044, 381),
                               ]
        self.lives = 10
        self.money = 2000
        self.timer = time.time()
        self.background = pygame.image.load(BACKGROUND)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.life_font = pygame.font.SysFont("comicsans", 65)
        self.selected_tower = None
        self.menu = VerticalMenu(self.width -side_image.get_width() + 70, 250 , side_image)
        self.menu.add_button(buy_archer, "Buy Archer", 500)
        self.menu.add_button(buy_archer_2, "Buy Crossbow", 750)
        self.menu.add_button(buy_damage, "Buy Damage", 1000)
        self.menu.add_button(buy_range, "Buy Support", 1000)

    def run(self):
        '''This is the main game loop.'''
        run = True
        clock = pygame.time.Clock()
        pygame_icon = pygame.image.load(ICON_FILE)
        pygame.display.set_icon(pygame_icon)
        enemycheck = 0 
        while run:
            clock.tick(100)
            if time.time() - self.timer >= random.randrange(1, 5)/2:
                self.timer = time.time()
                self.enemies.append(random.choice([Wizard(), Club(), Scorpion()]))
            if len(self.enemies) == 0:
                if enemycheck == 0:
                    self.enemies.append(Wizard())
                    enemycheck = 1
                elif enemycheck == 1:
                    self.enemies.append(Club())
                    enemycheck = 2
                elif enemycheck == 2:
                    self.enemies.append(Scorpion())
                    enemycheck = 0


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                position = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_clicked = None
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

            enemies_delete = []
            for enemy in self.enemies:
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
        self.menu.draw(self.win)
 
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
        

        pygame.display.update()

    def draw_menu(self):
        '''This function draws the menu.'''

        pass

g = Game()
LIVES_IMAGE = pygame.image.load("game_assets/td-gui/PNG/interface_game/heart.png").convert_alpha()
LIVES_IMAGE = pygame.transform.scale(LIVES_IMAGE, (50, 50))
STAR_IMAGE = pygame.image.load("game_assets/td-gui/PNG/interface_game/star.png").convert_alpha()
g.run()
