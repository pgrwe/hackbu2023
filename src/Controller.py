import pygame, sys, os
from src import Player
from src import Enemy
from pygame import *
# from src import CONSTANTS

class Controller:
    def __init__(self):
        """
        description: sets up pygame and window.
        args: None
        return: None
        """
        pygame.init()
        self.window_width = 990
        self.window_height = 800
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.Surface((self.window_width, self.window_height))
        pygame.display.set_caption("Cat Valentine Adventure")
        pygame.key.set_repeat(10, 50) # movement speed repetition 
        self.state = "GAME" # game state

        self.player = Player.Player() # init Player class from Player file
        self.enemy = Enemy.Enemy("Ghosty", 700, 350,) # init Enemy class from Enemy files
        self.all_sprites = pygame.sprite.Group((self.player),(self.enemy)) # group of all sprites 
        
        self.imgSnowmain = pygame.image.load("assets/cobbleSnowMainRoad-PNG.png").convert_alpha()
        self.imgSnowbedrock = pygame.image.load("assets/cobbleSnowBedrock-PNG.png").convert_alpha()
        self.imgSnowcorner =  pygame.image.load("assets/cobbleSnowBedrock.psd.png").convert_alpha()
        self.imgSkyblock = pygame.image.load("assets/skyblock.png")
        
        self.imgSnowmain = pygame.transform.scale(self.imgSnowmain,(90,90))
        self.imgSnowbedrock = pygame.transform.scale(self.imgSnowbedrock,(90,90)) 
        self.imgSnowcorner = pygame.transform.scale(self.imgSnowcorner,(90,90))
        self.imgSkyblock = pygame.transform.scale(self.imgSkyblock,(90,90))
        
       
        #self.scrollval = 0
        

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
                self.create_level()
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
        gameMap =  [['0','0','0','0','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','0','0','0','0'],
                    ['0','0','0','0','0','0','0','3','1','1','1'],
                    ['0','0','0','0','3','1','1','2','2','2','2'],
                    ['1','1','1','1','2','2','2','2','2','2','2'],
                    ['2','2','2','2','2','2','2','2','2','2','2']]
        tileSize = 90
        self.tileRects = []
        for y in range(len(gameMap)):
            for x in range(len(gameMap[y])):
                if gameMap[y][x] == "1":
                    self.screen.blit(self.imgSnowmain, (x*tileSize, y*tileSize))
                elif gameMap[y][x] == "2":
                    self.screen.blit(self.imgSnowbedrock, (x*tileSize, y*tileSize))
                elif gameMap[y][x] == "3":
                    self.screen.blit(self.imgSnowcorner, (x*tileSize, y*tileSize))
                elif gameMap[y][x] == "0":
                    self.screen.blit(self.imgSkyblock, (x*tileSize, y*tileSize))
                # if gameMap[x][y] != "0":
                    # self.tileRects.append(pygame.Rect(x*tileSize, y*tileSize))
                
                
        
        
        
        
        
        
        
        
     