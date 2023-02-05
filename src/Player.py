import pygame

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        """
        description: Function initializes the player state and the sprite.
        args: None
        return: None
        """
        self.imagepath = "assets/catval.png"
        pygame.sprite.Sprite.__init__(self)

        self.img = pygame.image.load(self.imagepath).convert_alpha()
        self.image =pygame.transform.scale(self.img, (100, 100))
        # self.image = pygame.image.load("assets/cat.png").convert_alpha()
        # self.image = pygame.Surface([10,20])
        # self.image.fill("white")

        self.rect = self.image.get_rect()
        self.rect.center = 500,350
        self.rect.x = 0
        self.rect.y = 0
        self.direction = "U"
        self.name = "Val"
        self.rect = pygame.Rect((self.rect.x,self.rect.y),(50,50))
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
          # self.image = pygame.image.load(self.image)
          self.rect.y -= self.speed
        elif direction == "D":
          self.direction = "D"
          # self.image = pygame.image.load(self.image)
          # self.image = pygame.image.load("assets/cat.png")
          self.rect.y += self.speed
        elif direction == "L":
          self.direction = "L"
          self.rect.x -= self.speed
          # self.image = pygame.image.load(self.image)
        elif direction == "R":
          self.direction = "R"
          self.rect.x += self.speed
          # self.image = pygame.image.load("assets/cat.png")
    def collide(self, rect1, rect2):
      if  pygame.Rect.colliderect(rect1, rect2) == True:
          if self.direction == "R":
            #player loses a life
            self.lives -= 1
            self.rect.x -= 3*self.speed
            print("Ouch")
          if self.direction == "D":
             self.lives -= 1
             self.rect.x += 3*self.speed
             self.rect.y += self.speed
          if self.direction == "L":
             self.lives -= 1
             self.rect.x += 3*self.speed


    def levelcollide(self, level, player):
        if pygame.Rect.colliderect(level, player):
            self.rect.y -= 1
