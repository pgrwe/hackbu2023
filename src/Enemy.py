import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        """
        description: Initializes the enemy state and sprite.
        args: name, x, y, img_file
        return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/rat.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = pygame.Rect((self.rect.x, self.rect.y),(10,20))
        self.speed = 3
        self.name = "RAT"
