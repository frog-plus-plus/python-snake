# Library imports
import pygame

# SETTINGS - CHANGE TO WHAT YOU WANT
CONST_WINDOW_START_SIZE_PX = (800, 600)
CONST_WINDOW_FLAGS = pygame.RESIZABLE
CONST_BACKGROUND_COLOUR = pygame.Color(0, 140, 0)
CONST_GRID_COLOUR = pygame.Color(0, 200, 0)
CONST_BORDER_WIDTH_PX = 6

# Class to manage the grid
class SnakeGrid:
    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height

    # Render the grid in the window (should be called once every frame)
    def render(self, game_window : pygame.Surface):

        # Iterate over every grid square
        for column in range(self.__width):
            for row in range(self.__height):
                # Get the allocated space that each grid square can take up
                # TODO: Change later so that each grid item is always a square (NOT RECTANGLE)
                allocated_width = (game_window.get_size()[0]) / self.__width
                allocated_height = (game_window.get_size()[1]) / self.__height
                square_width = allocated_width - CONST_BORDER_WIDTH_PX
                square_height = allocated_height - CONST_BORDER_WIDTH_PX
                allocated_top_left_position = (allocated_width * column, allocated_height * row)
                position_x = allocated_top_left_position[0] + (CONST_BORDER_WIDTH_PX / 2)
                position_y = allocated_top_left_position[1] + (CONST_BORDER_WIDTH_PX / 2)
                grid_square = pygame.rect.Rect(position_x, position_y, square_width, square_height)
                pygame.draw.rect(game_window, CONST_GRID_COLOUR, grid_square)


# Create and return the window
def init_window() -> pygame.Surface:
    return pygame.display.set_mode(CONST_WINDOW_START_SIZE_PX, flags=CONST_WINDOW_FLAGS)

# Check whether the user wants to close the window
def check_for_window_close_signal(event : pygame.event.Event) -> bool:
    if event.type == pygame.QUIT:
        return False
    else:
        return True

# Get events happening to the window
#  -- Calls checkForWindowCloseSignal()
def window_events(game_window : pygame.Surface) -> bool:
    running = True
    for event in pygame.event.get():
        running = check_for_window_close_signal(event)
    return running

def main():
    # Initialize the library and create the window
    pygame.init()
    game_window = init_window()

    my_grid = SnakeGrid(20, 20)

    # Main game loop - each iteration is a frame
    game_is_running = True
    while game_is_running:
        game_window.fill(CONST_BACKGROUND_COLOUR)

        # RENDERING GOES HERE
        my_grid.render(game_window)

        pygame.display.update()
        game_is_running = window_events(game_window)
    
    pygame.quit()

if __name__ == "__main__":
    main()
else:
    print("This is an imported file!")
