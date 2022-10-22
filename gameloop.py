import pygame as pg
import numpy as np
import tile
import random


class GameLoop:
    surface = 0
    tiles = []

    # https://stackoverflow.com/questions/9557182/python-shuffle-only-some-elements-of-a-list
    """Maybe implement your own shuffle algorithm that slices a 1d array according to the fixed positions"""

    """"""

    def __init__(self, screen_width, screen_height, difficulty):
        self.surface = pg.display.set_mode((screen_width, screen_height))
        self.draw_grid(difficulty)
        self.create_loop()

    def get_surface(self):
        return self.surface

    def create_loop(self):
        """
        Creates the game loop and checks for mouse clicks
        :return: none
        """

        running = True
        first_click = True
        while running:
            pos = pg.mouse.get_pos()
            for event in pg.event.get():

                if event.type == pg.MOUSEBUTTONDOWN and first_click:
                    row, col = self.check_tile_click(pos)
                    self.random_walk(8, row, col)
                    first_click = False
                if event.type == pg.MOUSEBUTTONDOWN and not first_click:
                    self.check_tile_click(pos)
                if event.type == pg.QUIT:
                    running = False

    def check_tile_click(self, pos):

        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                t = self.tiles[i][j]
                if t.collidepoint(pos):
                    t.change_color('black')
                    if t.is_bomb == 1:
                        t.change_color('red')
                    return i, j



    def reveal_when_no_bombs(self, t):
        """
        Reveals surrounding safe tiles when no bombs are present in immediate vicinity
        :param t:
        :return: none
        """
        pass

    @staticmethod
    def create_mines(n, k):
        """
        Create a 2D array with random mines within each position of the array
        :param n: dimension size of array
        :param k: number of mines on grid
        :return: array
        """
        grid = np.array([1] * k + [0] * (n * n - k))
        np.random.shuffle(grid)
        grid = np.reshape(grid, (-1, n))  # reshaping into 2D array
        return grid

    def shift_row(self, pos_left, pos_top, col, dimension, t, current_row):
        """
        Once column index reaches end of column length, row has to shift
        down one and column has to reset to 0
        :param pos_left: position of tile from left
        :param pos_top: position of tile from top
        :param col: current column
        :param dimension: tile size
        :param t: object Tile
        :param current_row: list of tiles in current row
        :return: pos_left & pos_top
        """
        current_row.append(t)
        pos_left += t.get_width()
        if col == dimension - 1:
            self.tiles.append(current_row)
            pos_left = 0
            pos_top += t.get_width()

        return pos_left, pos_top

    def draw_grid(self, dimension):
        """
        Draws alternating tiles on the grid
        :param dimension: size of grid
        :return: none
        """
        pos_left = 0
        pos_top = 0
        grid = self.create_mines(dimension, 8)
        # grid = self.create_grid(dimension)
        for row in range(dimension):
            current_row = []
            for col in range(dimension):
                if row % 2 == 0:
                    if col % 2 == 0:
                        current_color = 'light green'
                    else:
                        current_color = 'dark green'
                else:
                    if col % 2 == 1:
                        current_color = 'light green'
                    else:
                        current_color = 'dark green'

                t = tile.Tile(self.surface, current_color, dimension, pos_left, pos_top, grid[row][col])
                pos_left, pos_top = self.shift_row(pos_left, pos_top, col, dimension, t, current_row)

    @staticmethod
    def create_grid(n):
        shape = (n, n)
        return np.zeros(shape)

    def dfs_search(self, grid, row, col):
        if col < 0 or row < 0 or col >= len(grid[0]) or row >= len(grid):
            return
        else:
            self.dfs_search(grid, row + 1, col)
            self.dfs_search(grid, row - 1, col)
            self.dfs_search(grid, row, col + 1)
            self.dfs_search(grid, row, col - 1)

    def generate_first_safe_tiles(self, mouse_pos):
        """
        Purpose is to randomly generate safe tiles around where the player clicked at the start of the game
        Sort of like a random walk
        :param mouse_pos: position of mouse
        :return:
        """
        start_row, start_col = 0, 0
        for row in self.tiles:
            for t in row:
                if t.collidepoint(mouse_pos):
                    start_row, start_col = row, t
                    t.change_color('black')

    def random_walk(self, n, row, col):
        directions = ['LEFT', 'RIGHT', 'UP', 'DOWN']
        for i in range(n):
            step = random.choice(directions)

            if step == 'LEFT' and col >= 0:
                self.tiles[row][col - 1].change_color('black')
                col -= 1
            elif step == 'RIGHT' and col < len(self.tiles[0]) - 1:
                self.tiles[row][col + 1].change_color('black')
                a = str(col) + " " + str(len(self.tiles[0]))
                print(a)
                col += 1
            elif step == 'UP' and row >= 0:
                self.tiles[row - 1][col].change_color('black')
                row -= 1
            elif step == 'DOWN' and row < len(self.tiles) - 1:
                a = str(row) + " " + str(len(self.tiles))
                print(a)
                self.tiles[row + 1][col].change_color('black')
                row += 1
