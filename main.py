import pygame
import sys

from setttings import *
from maze import *

pygame.init()

class Game:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Mon labyrinthe")

        self.running = True

    def run(self):
        pass

    def menu(self):
        pass

    def game(self):
        pass

    def end(self):
        self.running = False
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()