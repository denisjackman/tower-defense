''' This is the main file for tower-defense'''
import pygame
from dataclasses import dataclass

# Replace width and height with the desired size of the game window.
width = 1068
height = 768
SCREENRECT = pygame.Rect(0, 0, width, height)
@dataclass
class TowerGame:

    screen: pygame.Surface
    screen_rect: pygame.Rect
    fullscreen: bool

    @classmethod
    def create(cls, fullscreen=False):
        game = cls(
            screen=None,
            screen_rect=SCREENRECT,
            fullscreen=fullscreen,
        )
        game.init()
        return game

    def loop(self):
        pass

    def quit(self):
        pygame.quit()

    def start_game(self):
        self.loop()

    def init(self):
        pygame.init()
        window_style = pygame.FULLSCREEN if self.fullscreen else 0
        # We want 32 bits of color depth
        bit_depth = pygame.display.mode_ok(self.screen_rect.size, window_style, 32)
        screen = pygame.display.set_mode(self.screen_rect.size, window_style, bit_depth)
        pygame.mixer.pre_init(
            frequency=44100,
            size=32,
            # N.B.: 2 here means stereo, not the number of channels to
            # use in the mixer
            channels=2,
            buffer=512,
        )
        pygame.font.init()
        self.screen = screen

def start_game():
    game = TowerGame.create()
    game.loop()

if __name__ == "__main__":
    start_game()