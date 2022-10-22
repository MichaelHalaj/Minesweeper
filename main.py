from gameloop import GameLoop
import pygame as pg


def main():
    pg.display.set_caption('Minesweeper')
    difficulty = 8
    game = GameLoop(560, 560, difficulty)


if __name__ == "__main__":
    main()
