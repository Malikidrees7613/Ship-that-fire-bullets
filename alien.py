import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    #Aclass tha represent single alien in the flet

    def __init__(self,ai_game):
        #initializing alien ship and its starting position
        super().__init__()
        self.screen = ai_game.screen

        #loading Alien image and seting its rect attributes
        self.image = pygame.image.load('images/alien.png')
        self._original_image = self.image.copy()
        self.rect = self.image.get_rect()

        #Strating new alien ship on the top left
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 

         
        #storing alien at the exact position
        self.x =float(self.rect.x)

        self.new_width = 50  
        self.new_height = 50
        self.scale_image()
       
    def scale_image(self):
        self.image = pygame.transform.scale(self._original_image, (self.new_width, self.new_height))
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        