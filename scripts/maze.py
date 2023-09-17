import pygame

class Maze:
    def __init__(self,  game, size) -> None:
        self.game = game
        self.size = size

        self.maze = self.new_maze(self.size)
        print(self.maze)

    def new_maze(self, size):
        maze = []

        # Valeurs choisis arbitrairement
        wall = 1
        empty = 0

        for i in range(size[0]):
            # Alternance lignes complètes, creuses
            if i % 2 == 0:
                line = [wall for i in range(size[1])]
            else:
                line = [wall if i % 2 == 0 else empty for i in range(size[1])]

            # Cas où la ligne finit par 0
            if size[1] % 2 == 0:
                line.append(wall)

            maze.append(line)

        # Si la dernière ligne n'est pas complète
        if size[0] % 2 == 0:
            # Selon si la dimension x est paire ou impaire la ligne ne doit pas faire la même longueur
            if size[1] % 2 == 0:
                maze.append([wall for i in range(size[1] + 1)])
            else:
                maze.append([wall for i in range(size[1])])

        return maze
    
    def draw(self):
        pass