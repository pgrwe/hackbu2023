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
        self.rect = self.image.get_rect()
        self.rect.center = 500,350
        self.rect.x = 0
        self.rect.y = 0
        self.direction = "U"
        self.name = "Val"
        self.rect = pygame.Rect((self.rect.x,self.rect.y),(50,50))
        self.speed = 15
        self.lives = 9
        # self.attack_ani_R = [pygame.image.load("animationright"),pygame.image.load("animation two")]
        # self.attack_ani_L = [pygame.image.load(animationLEft), pygame.image.load("animation 2 left")]
        # self.attacking = False
        # self.attack_frame = 0


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

    # def attack(self):
        # """
        # description: makes the character attack with an animation. also states how much damage it is able to do while also taking damage too.
        # args: none.
        # return: none.
        # """
        # if self.attack_frame > 1:
            # self.attack_frame = 0
            # self.attacking = False

        # if self.direction == "R":
            # self.image = self.attack_ani_R[self.attack_frame]
        # else:
            # self.image = self.attack_ani_L[self.attack_frame]

        # self.attack_frame += 1
        # if self.attacking == False:
            # self.move()

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
