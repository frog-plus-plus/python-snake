import pygame

GRID_SLOT_EMPTY = 0

class SnakeGrid:
    def __init__(self, width : int, height : int,
     squareColour : pygame.Color, gameWindow : pygame.Surface) -> None:
        self.__width = width
        self.__height = height
        self.__squareColour = squareColour
        self.__gameWindow = gameWindow
        self.__grid = []
        for widthCounter in range(self.__width):
            self.__grid.append([])
            for heightCounter in range(self.__height):
                self.__grid[widthCounter][heightCounter] = 0

    def render(self):
        for widthCounter in range(self.__width):
            for heightCounter in range(self.__height):
                pygame.draw.rect(self.__gameWindow, self.__squareColour, pygame.Rect())

