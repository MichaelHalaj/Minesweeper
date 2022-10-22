"""Class for individual tile objects"""
import pygame as pg
import color
import numpy as np


class Tile(pg.Rect):
    dimension = 0
    width = 0
    display_width = 0
    color_index = ""

    def __init__(self, surface, color_index, dimension, pos_left, pos_top, is_bomb):
        self.surface = surface
        self.display_width = self.get_display_width()
        self.set_width(self.display_width, dimension)
        self.color_index = color_index
        self.dimension = dimension
        self.is_bomb = is_bomb
        super().__init__(pos_left, pos_top, self.get_width(), self.get_width())
        self.draw_rect(self.color_index)

    def get_size(self):
        """
        Gets and returns dimension of the tile
        :return: dimension
        """
        return self.dimension

    def get_width(self):
        """
        Gets and returns the width of the tile to shift by
        :return: width
        """
        return self.width

    def change_color(self, color_idx):
        """
        Changes color of tile according to provided color name
        :param color_idx: String name of color
        :return:
        """
        self.draw_rect(color_idx)
        pass

    def check_bomber_number(self):
        """
        Checks surrounding tiles if they are bombs
        :return: bomb count
        """
    def set_bomb_number(self):
        """
        Sets the number within the tile
        :return: none
        """
        pass

    def set_width(self, screen_width, dimension):
        """
        Sets the width of a tile as a function of the screen width
        :param screen_width: width of screen
        :param dimension: dimension of tile
        :return: none
        """

        self.width = screen_width / dimension

    @staticmethod
    def get_display_width():
        """
        Gets and returns the screen width
        :param surface: screen
        :return: screen width
        """
        return pg.display.get_surface().get_width()

    def draw_rect(self, color_index):
        """
        Draws the tile on the game surface according to color specified in color index
        :param color_index: index of size 2 color array
        :return: none
        """

        pg.draw.rect(self.surface,
                     color.get_color(color_index),
                     super().copy(),
                     0)
        pg.display.flip()
