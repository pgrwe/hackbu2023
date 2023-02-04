import pygame, sys, os
from src import Player
from src import Enemy
from pygame import *

class Controller:
    def __init__(self):
        """
        description: sets up pygame and window.
        args: None
        return: None
        """
        pygame.init()
        self.window_width = 1000
        self.window_height = 700
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.Surface((self.window_width, self.window_height))
        pygame.display.set_caption("Cat Valentine Adventure")
        pygame.key.set_repeat(10, 50)
        self.state = "GAME"

        self.player = Player.Player()
        self.enemy = Enemy.Enemy("Ghosty", 700, 350,)
        self.all_sprites = pygame.sprite.Group((self.player),(self.enemy))


    def gameLoop(self):
        """
        description: player moves based on what key is pressed, if player collides with enemy starts a fight
        args: (None)
        return: (None)
        """
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP):
                        self.player.move("U")
                    elif (event.key == pygame.K_DOWN):
                        self.player.move("D")
                    elif (event.key == pygame.K_LEFT):
                        self.player.move("L")
                    elif (event.key == pygame.K_RIGHT):
                        self.player.move("R")

                self.player.move()
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
        clock.tick(60)

    def create_level(self):
        """
        description: creates the level
        args: (None)
        return: (None)
        """
        