import pygame, sys


class Controller:
    def __init__(self):
        """
        description: sets up pygame and window.
        args: None
        return: None
        """
        pygame.init()
        self.window_width = 1000
        self.window_height = 800
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.Surface((self.window_width, self.window_height))
        pygame.display.set_caption("Cat Valentine Adventure")
        pygame.key.set_repeat(50, 500)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill(black)
            pygame.time.delay(100)
            pygame.display.flip()
