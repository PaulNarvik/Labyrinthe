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
        self.maze = Maze(game, (40, 30))

        self.game() # Remplacer par menu plus tard :-)

    def menu(self):
        pass

    def game(self):
        def handle_events():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end()
                    
        def draw():
            self.screen.fill((0, 0, 0))
            self.maze.draw()

        while self.running:
            handle_events()
            draw()

            pygame.display.flip()

    def end(self):
        self.running = False
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()