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
        self.state = "TITLE"

        self.player = Player.Player()
        self.enemy = Enemy.Enemy("Ghosty", 700, 350,)
        self.all_sprites = pygame.sprite.Group((self.player),(self.enemy))

        self.buttonimg = pygame.image.load("assets/redButton.png")
        self.button = pygame.transform.scale(self.buttonimg, (150, 150))

    def mainLoop(self):
        """
        If game is still running, runs gameLoop; if game is over(player health is at 0), runs gameover; if game is at a savepoint, runs savepoint; if player won(enemy health is at 0), runs win
        args: None
        return: None
        """
        while True:
            if (self.state == "GAME"):
                self.gameLoop()
            elif (self.state == "TITLE"):
                self.title()
            # elif (self.state == "WIN"):
            #     self.win()
            # elif (self.state == "GAMEOVER"):
            #     self.gameOver()

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
            self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def title(self):
        """
        description: Sets up title screen with it text, buttons, and images.
        args: None
        return: None
        """
        while self.state == "TITLE":
            pygame.font.init()
            font = pygame.font.Font("assets/Blantick_Script.ttf", 80)
            title1 = font.render('Cat Valentine', True, (131, 139, 139))
            title2 = font.render('Adventure', True, (131, 139, 139))
            start = font.render('Start', True, (131, 139, 139))
            exit = font.render('Exit', True, (131, 139, 139))

            button_start = pygame.Rect((25, 190), (150, 40))
            button_exit = pygame.Rect((25, 350), (150, 40))

            self.screen.blit(title1, (20, 10))
            self.screen.blit(title2, (40, 75))

            self.screen.blit(self.button, (25, 155))
            self.screen.blit(self.button, (25, 350))

            self.screen.blit(start, (40, 200))
            self.screen.blit(exit, (70, 350))

            click = False
            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                event.type == pygame.mouse.get_pressed()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if button_start.collidepoint((mx, my)):
                if click:
                    self.state = "GAME"

            if button_exit.collidepoint((mx, my)):
                if click:
                    self.exitGame()

            pygame.display.update()

    #
    # def win(self):
    #     while self.state == "WIN":
    #
    # def gameOver(self):
    #     while self.state == "GAMEOVER":

    def exitGame(self):
        """
        description: stops running program ("Exits game")
        args: None
        return: None
        """
        pygame.quit()
        sys.exit()
