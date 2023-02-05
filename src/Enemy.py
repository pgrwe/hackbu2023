import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        """
        description: Initializes the enemy state and sprite.
        args: name, x, y, img_file
        return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/ratKing.png").convert_alpha()
        self.image = pygame.Surface([10,20])
        self.image.fill("blue")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = pygame.Rect((self.rect.x, self.rect.y),(10,20))
        self.speed = 3
        self.name = "RAT"
        self.health = 1

    def update(self):
        # """
        # description: Kills the enemy if its health reaches 0 or is less than 0.
        # args: None
        # return: None
        # """
        if self.health <= 0:
          self.kill()
