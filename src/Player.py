import pygame

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        """
        description: Function initializes the player state and the sprite.
        args: None
        return: None
        """
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load("assets/cat.png").convert_alpha()
        self.image = pygame.Surface([10,20])
        self.image.fill("white")

        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 350
        self.direction = "U"
        self.name = "Val"
        self.rect = pygame.Rect((self.rect.x,self.rect.y),(10,20))
        self.speed = 15
        self.lives = 9

    def move(self, direction = None):
        """
        description: Moves Player based on direction
        args: direction
        return: None
        """
        if direction == "U":
          self.direction = "U"
          # self.image = pygame.image.load("assets/cat.png")
          self.rect.y -= self.speed
        elif direction == "D":
          self.direction = "D"
          # self.image = pygame.image.load("assets/cat.png")
          self.rect.y += self.speed
        elif direction == "L":
          self.direction = "L"
          self.rect.x -= self.speed
          # self.image = pygame.image.load("assets/cat.png")
        elif direction == "R":
          self.direction = "R"
          self.rect.x += self.speed
          # self.image = pygame.image.load("assets/cat.png")
