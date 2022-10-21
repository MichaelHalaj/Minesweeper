import pygame as pg
import numpy as np
import tile
import random as rd


class GameLoop:
    surface = 0
    tiles = []

    def __init__(self, screen_width, screen_height):
        self.surface = pg.display.set_mode((screen_width, screen_height))
        self.draw_grid(8)
        self.create_loop()

    def get_surface(self):
        return self.surface

    def create_loop(self):
        """
        Creates the game loop and checks for mouse clicks
        :return: none
        """

        running = True
        while running:
            for event in pg.event.get():

                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    for t in self.tiles:
                        if t.collidepoint(pos):
                            t.change_color('black')
                            if t.is_bomb == 1:
                                t.change_color('red')

                if event.type == pg.QUIT:
                    running = False

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

    @staticmethod
    def shift_row(pos_left, pos_top, col, dimension, t):
        """
        Once column index reaches end of column length, row has to shift
        down one and column has to reset to 0
        :param pos_left: position of tile from left
        :param pos_top: position of tile from top
        :param col: current column
        :param dimension: tile size
        :param t: object Tile
        :return: pos_left & pos_top
        """
        pos_left += t.get_width()
        print(pos_left)
        if col == dimension - 1:
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
        for row in range(dimension):
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
                self.tiles.append(t)
                pos_left, pos_top = self.shift_row(pos_left, pos_top, col, dimension, t)

    def create_grid(self, dimension):
        grid = self.create_mines(dimension, 8)
        print(grid)
