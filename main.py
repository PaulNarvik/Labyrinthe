import pygame
import sys

from setttings import *

pygame.init()

class Game:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode()

        self.running = True

    def run(self):
        pass

    def end(self):
        self.running = False
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()