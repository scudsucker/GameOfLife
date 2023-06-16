from random import randint


class Engine(object):

_grid = []

def __init__(self, rows, cols):
    self._rows = rows
    self._cols = cols

def seed(self, grid):
    """ Add a 'seed' grid; this allows adding known patterns
    :param grid: a 2 dimensional list containing only 1 or 0
    :return: null
    """
    self._grid = grid
    return

def generate(self):
    """ Using an existing 'seed' grid, follow the rules to change the
    values in the list
    :return: a 2 dimensional list containing only 1 or 0
    """

    # NB: if the system was not set up with a 'seed' pattern, generate one.
    if len(self._grid) == 0:
        self._grid = [[randint(0, 1) for row in range(self._rows)]
                     for col in range(self._cols)]

    generated = [[0 for row in range(self._rows)]
                 for col in range(self._cols)]

    for y in range(self._cols):
        for x in range(self._rows):

            neighbours = self.__neighbourCount(x, y)

            # Handles
            #  Rule 1 - Any live cell with fewer than two live neighbours
            #  dies, as if caused by under-population (by defaulting to 0)
            #  Rule 2 - Any live cell with two or three live neighbours
            #  lives on to the next generation.
            #  Rule 3 - Any live cell with more than three live neighbours
            #  dies, as if by overcrowding (by defaulting to 0)
            if ((self._grid[y][x] == 1) and
                    (neighbours == 2 or neighbours == 3)):
                generated[y][x] = 1

            # Rule 4 - Any dead cell with exactly three live neighbours
            # becomes a live cell
            if self._grid[y][x] == 0 and neighbours == 3:
                generated[y][x] = 1

    self._grid = generated
    return generated

def __neighbourCount(self, x, y):
    """ Return the sum of the value of neighbours of a cell in the grid
    :param x: the X coordinate index of the cell
    :param y: the Y coordinate index of the cell
    :return:
    """
    count = 0
    for row in [-1, 0, 1]:
        for col in (-1, 0, 1):
            if (not row == col == 0 and
                (0 <= x + row < self._rows and
                 0 <= y + col < self._cols)):
                count += self._grid[(y + col) % self._cols][(x + row) % self._rows]

    return count
