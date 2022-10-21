from gameloop import GameLoop
import pygame as pg


def main():
    pg.display.set_caption('Minesweeper')
    game = GameLoop(560, 560)


if __name__ == "__main__":
    main()
