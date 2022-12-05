import pygame

CONST_WINDOW_START_SIZE_PX = (800, 600)
CONST_WINDOW_FLAGS = pygame.RESIZABLE

def initWindow() -> pygame.Surface:
    return pygame.display.set_mode(CONST_WINDOW_START_SIZE_PX, flags=CONST_WINDOW_FLAGS)

def checkForWindowCloseSignal(event : pygame.event.Event) -> bool:
    if event.type == pygame.QUIT:
        return False
    else:
        return True

def windowEvents(gameWindow : pygame.Surface) -> bool:
    running = True
    for event in pygame.event.get():
        running = checkForWindowCloseSignal(event)
    return running

def main():
    pygame.init()
    gameWindow = initWindow()

    gameIsRunning = True
    while gameIsRunning:
        gameWindow.fill((0, 0, 0))

        pygame.draw.circle(gameWindow, pygame.Color( 255, 255, 255 ), pygame.mouse.get_pos(), 5)
        pygame.display.update()
        gameIsRunning = windowEvents(gameWindow)
    
    pygame.quit()

if __name__ == "__main__":
    main()
else:
    print("This is an imported file!")