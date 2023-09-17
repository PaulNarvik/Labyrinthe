import pygame

pygame.init()

class Game:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode()

    def run(self):
        pass

    def end(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.run()