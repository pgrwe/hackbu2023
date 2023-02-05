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
        pygame.key.set_repeat(10, 50)
        self.state = "TITLE"

        # self.player = Player.Player()
        # self.enemy = Enemy.Enemy("Ghosty", 700, 350,)
        # self.all_sprites = pygame.sprite.Group((self.player),(self.enemy))

        self.buttonimg = pygame.image.load("assets/redButton.png")
        self.button = pygame.transform.scale(self.buttonimg, (150, 150))
        self.screen.blit(self.player.image, self.player.rect)

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
            elif (self.state == "CHOICE"):
                self.choice()
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
                self.create_level()
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            #self.screen.fill("black")
            self.player.collide(self.player.rect, self.enemy.rect)
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

    def choice(self):
        """
        description: Allows type in name and choose cat
        args: None
        return: None
        """
        input_box = pygame.Rect((310, 10), (25, 28))
        inside_box = pygame.Rect((313, 10), (200, 32))
        font = pygame.font.Font('assets/Basking.ttf', 20)
        color_inactive = pygame.Color('darkorchid4')
        color_active = pygame.Color('darkorchid3')
        color = color_inactive
        text1 = font.render('Enter Name:', True, (154, 50, 205))
        self.screen.blit(text1, (200, 10))
        text = ""
        active = False
        done = False
        pygame.display.update()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                        color = color_active
                    if active:
                        color = color_active
                    else:
                        color = color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_RETURN:
                            text = ""
                            self.state == "GAME"
                            self.screen.fill((0, 0, 0))
                            done = True
                        else:
                            text += event.unicode
                            self.player.name = text
        color2 = (0,0,0)
        txt_surface = font.render(text, True, color)
        width = max(150, txt_surface.get_width() + 10)
        input_box.w = width
        pygame.draw.rect(self.screen, color2, inside_box)
        self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 2))
        pygame.draw.rect(self.screen, color , input_box, 2)


    # def collision(self):
    #     if  pygame.Rect.colliderect(self.player.rect, self.enemy.rect) == True:
    #         #player loses a life
    #         self.player.lives -= 1
    #         self.rect.x -= 3*self.speed
    #         print("Ouch")


        


        pygame.display.flip()
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
        
