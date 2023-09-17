import pygame

class Maze:
    def __init__(self,  game, size) -> None:
        self.game = game
        self.size = size

        self.maze = self.new_maze(self.size)
        print(self.maze)

    def new_maze(self, size):
        maze = []
        wall = 1
        empty = 0
        for i in range(size[0]):
            if i % 2 == 0:
                line = [wall for i in range(size[1])]
            else:
                line = [wall if i % 2 == 0 else empty for i in range(size[1])]
                if line[-1] == empty:
                    line.append(wall)
            maze.append(line)
        return maze