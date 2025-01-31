import random
from config import WALL, EMPTY
import maze

class MazeGenerator:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def generate(self) -> list[list[int]]:
        # on crée une grille vide
        grid = [[EMPTY for _ in range(self.width)] for _ in range(self.height)]
        start, finish = (0, 0), (self.width - 1, self.height - 1)

        # On génére les murs
        for y in range(self.height):
            for x in range(0, self.width):
                grid[y][x] = WALL

        # on vérifie que l'entrée et la sortie sont vides
        grid[start[1]][start[0]] = EMPTY
        grid[finish[1]][finish[0]] = EMPTY

        # Backtracking 
        def drill(grid, x, y) -> None:
            ways = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            random.shuffle(ways)

            for dx, dy in ways:
                ax, ay = x + 2*dx, y + 2*dy
                if 0 <= ax < self.width and 0 <= ay < self.height:
                    if grid[ax][ay] == 1:
                        grid[x + dx][y + dy] = 0
                        grid[ax][ay] = 0
                        if (ax, ay) != finish:
                            drill(grid, ax, ay)
        drill(grid, 0, 0)


        return grid, start, finish