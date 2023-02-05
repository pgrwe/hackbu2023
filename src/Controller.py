import pygame, sys, os
from src import Player
from src import Enemy
from src import Tiles
from pygame import *

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
        self.state = "TITLE" # game state

        self.cat1path = ("assets/catval.png")
        self.cat2path = ("assets/cat2.png")
        self.cat3path = ("assets/cat3.png")
        self.catsoulpath = ("assets/catsoul.png")
        self.heartpath  = ('assets/heart.png')
        self.wintertreepath = ("assets/wintertree.png")

        self.player = Player.Player() # init Player class from Player file
        self.enemy = Enemy.Enemy("RAT", 700, 350,) # init Enemy class from
        #self.tiles = Tiles.Tile()
        self.all_sprites = pygame.sprite.Group((self.player),(self.enemy),(self.tiles)) # group of all sprites

        self.imgSnowmain = pygame.image.load("assets/cobbleSnowMainRoad.png").convert_alpha()
        self.imgSnowbedrock = pygame.image.load("assets/cobbleSnowBedrock.png").convert_alpha()
        self.imgSnowRightcorner =  pygame.image.load("assets/cobbleSnowright.png").convert_alpha()
        self.imgSnowLeftcorner = pygame.image.load("assets/cobbleSnowleft.png").convert_alpha()
        self.imgSkyblock = pygame.image.load("assets/skyblock.png")

        pygame.key.set_repeat(10, 50)
        self.tileRects = []

        self.buttonimg = pygame.image.load("assets/redButton.png")
        self.button = pygame.transform.scale(self.buttonimg, (150, 60))
        # self.screen.blit(self.player.image, self.player.rect)

        self.cat1_img = pygame.image.load(self.cat1path)
        self.cat1 = pygame.transform.scale(self.cat1_img, (250, 250))
        self.cat2_img = pygame.image.load(self.cat2path)
        self.cat2 = pygame.transform.scale(self.cat2_img, (250, 250))
        self.cat3_img = pygame.image.load(self.cat3path)
        self.cat3 = pygame.transform.scale(self.cat3_img, (250, 250))
        self.catsoul_img = pygame.image.load(self.catsoulpath)
        self.catsoul = pygame.transform.scale(self.catsoul_img, (250, 250))
        self.heart_img = pygame.image.load(self.heartpath)
        self.heart = pygame.transform.scale(self.heart_img, (64, 64))

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
            elif (self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        """
        description: player moves based on what key is pressed, if player collides with enemy starts a fight
        args: (None)
        return: (None)
        """
        while self.state == "GAME":
            if self.player.lives == 0:
                self.state = "GAMEOVER"
                # print(self.player.lives, self.state)
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(self.tileRects)
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
                    elif (event.key == pygame.K_x):
                        self.player.attacking = True
                        self.player.attack()
                self.player.move()
                self.create_level()
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            #self.screen.fill("black")
            self.player.collide(self.player.rect, self.enemy.rect)
            # if self.player.fight == True:
            #     if self.player.attacking == True:
            #         if self.enemy.name == "RAT":
            #             if self.player.weapon == "CLAW":
            #                 self.enemy.health = 5
            #             elif self.player.weapon == "SABER":
            #                 self.enemy.health = 0
            #     else:
            #         self.player.lives -= 1
            for i in self.tileRects:
                if self.player.levelcollide(i, self.player.rect):
                    print("working")
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
        clock.tick(60)
 

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
                    ['0','0','0','0','0','0','0','4','1','1','1'],
                    ['1','1','3','0','4','1','1','2','2','2','2'],
                    ['2','2','2','1','2','2','2','2','2','2','2'],
                    ['2','2','2','2','2','2','2','2','2','2','2']]
        tileSize = 90
        # for y in range(len(gameMap)):
            # for x in range(len(gameMap[y])):
                # if gameMap[y][x] == "1":
                    # self.screen.blit(self.imgSnowmain, (x*tileSize, y*tileSize))
                    
                # elif gameMap[y][x] == "2":
                    # self.temp2 = self.screen.blit(self.imgSnowbedrock, (x*tileSize, y*tileSize))
                    # self.tileRects.append(pygame.Rect(self.temp2))
                # elif gameMap[y][x] == "3":
                    # self.temp3 = self.screen.blit(self.imgSnowRightcorner, (x*tileSize, y*tileSize))
                    # self.tileRects.append(pygame.Rect(self.temp3))
                # elif gameMap[y][x] == "4":
                    # self.temp4 = self.screen.blit(self.imgSnowLeftcorner, (x*tileSize, y*tileSize))
                    # self.tileRects.append(pygame.Rect(self.temp4))
                # elif gameMap[y][x] == "0":
                    # self.screen.blit(self.imgSkyblock, (x*tileSize, y*tileSize))
            
        self.tileGroup = pygame.sprite.Group()
        for row_index,row in enumerate(gameMap):
            for col_index,column in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if column == '1':
                    tile = Tiles.Tile((x,y),tile_size)
                    self.tiles.add(tile)        
                    
                    
        
                    
                """
                TO-DO: make the blits here sprites (if possible) to smooth collisions
                Add moving camera/larger level
                Remember that level size scales with window size (vertically), if you make the blocks smaller you will need to change around the window size and number of rows/columns
                """

    def title(self):
        """
        description: Sets up title screen with it text, buttons, and images.
        args: None
        return: None
        """
        while self.state == "TITLE":
            self.screen.fill((255,141,133))
            pygame.font.init()
            font = pygame.font.Font("assets/Blantick_Script.ttf", 80)
            font2 = pygame.font.Font("assets/Blantick_Script.ttf", 55)
            title1 = font.render('Cat Valentine', True, (250, 222, 220))
            title2 = font.render('Adventure', True, (250, 222, 220))
            start = font2.render('Start', True, (250, 222, 220))
            exit = font2.render('Exit', True, (250, 222, 220))

            button_start = pygame.Rect((420, 250), (150, 60))
            button_exit = pygame.Rect((420, 350), (150, 60))

            self.screen.blit(title1, (330, 10))
            self.screen.blit(title2, (380, 75))

            self.screen.blit(self.button, (420, 250))
            self.screen.blit(self.button, (420, 350))

            self.screen.blit(start, (450, 250))
            self.screen.blit(exit, (450, 350))

            self.screen.blit(self.cat1, (180, 450))
            self.screen.blit(self.heart, (470, 575))
            self.screen.blit(self.catsoul, (600, 450))

            click = False
            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # event.type == pygame.mouse.get_pressed()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if button_start.collidepoint((mx, my)):
                if click:
                    self.state = "CHOICE"

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
        self.screen.fill("black")
        while self.state == "CHOICE":
            input_box = pygame.Rect((310, 10), (25, 28))
            inside_box = pygame.Rect((313, 10), (500, 32))
            font = pygame.font.Font('assets/Blantick_Script.ttf', 40)
            color_inactive = pygame.Color('red')
            color_active = pygame.Color('darkorchid3')
            color = color_inactive
            text1 = font.render('Enter Name:', True, (250, 0, 0))
            self.screen.blit(text1, (100, 10))
            text = ""
            writing = True
            cha_choice = False
            while writing == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if input_box.collidepoint(event.pos):
                            color = color_active
                    if color == color_active:
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            elif event.key == pygame.K_RETURN:
                                self.screen.fill((0, 0, 0))
                                writing = False
                            else:
                                text += event.unicode
                                self.player.name = text
                                # print(self.player.name)
                txt_surface = font.render(text, True, color)
                width = max(150, txt_surface.get_width() + 10)
                input_box.w = width
                pygame.draw.rect(self.screen, (0,0,0), inside_box)
                self.screen.blit(txt_surface, (input_box.x + 5, input_box.y - 5))
                pygame.draw.rect(self.screen, color , input_box, 2)
                # pygame.display.update()
                pygame.display.flip()
                if writing == False:
                    cha_choice = True
                    break

            while cha_choice == True:

                cat_1 = pygame.Rect((50, 190), (250, 250))
                cat_2 = pygame.Rect((350, 190), (250, 250))
                cat_3 = pygame.Rect((650, 190), (250, 250))

                self.screen.blit(self.cat1, (50, 190))
                self.screen.blit(self.cat2, (350, 190))
                self.screen.blit(self.cat3, (650, 190))

                click = False
                mx, my = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    event.type == pygame.mouse.get_pressed()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

                if cat_1.collidepoint((mx, my)):
                    if click:
                        cha_choice = False
                        self.state = "GAME"

                if cat_2.collidepoint((mx, my)):
                    if click:
                        self.player.img = pygame.image.load(self.cat2path).convert_alpha()
                        self.player.image = pygame.transform.scale(self.player.img, (100, 100))
                        cha_choice = False
                        self.state = "GAME"
                if cat_3.collidepoint((mx, my)):
                    if click:
                        self.player.img = pygame.image.load(self.cat3path).convert_alpha()
                        self.player.image = pygame.transform.scale(self.player.img, (100, 100))
                        cha_choice = False
                        self.state = "GAME"
                pygame.display.update()

    #
    # def win(self):
    #     while self.state == "WIN":
    #
    def gameOver(self):
        self.screen.fill("black")
        while self.state == "GAMEOVER":
            pygame.font.init()
            font = pygame.font.Font("assets/Blantick_Script.ttf", 80)
            retry = font.render('Retry', True, (131, 139, 139))
            exit = font.render('Quit', True, (131, 139, 139))

            button_retry = pygame.Rect((25, 190), (150, 40))
            button_exit = pygame.Rect((25, 350), (150, 40))

            self.screen.blit(self.button, (25, 155))
            self.screen.blit(self.button, (25, 350))

            self.screen.blit(retry, (40, 200))
            self.screen.blit(exit, (70, 350))

            click = False
            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                event.type == pygame.mouse.get_pressed()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if button_retry.collidepoint((mx, my)):
                if click:
                    self.state = "TITLE"

            if button_exit.collidepoint((mx, my)):
                if click:
                    self.exitGame()

            pygame.display.update()
    def exitGame(self):
        """
        description: stops running program ("Exits game")
        args: None
        return: None
        """
        pygame.quit()
        sys.exit()

    def collision_test(rect, tiles):
        hitlist = []
        for tile in tiles:
            if rect.colliderect(tile):
                hitlist.append(tile)
