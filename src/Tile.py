import pygame

class Tiles(pygame.sprite.Sprite):
    def __init__(self,pos,size):
    
    
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size,size))
        white = (250,250,250)
        self.image.fill(white)
        self.rect = self.image.get_rect(topleft=pos)
        
        
    