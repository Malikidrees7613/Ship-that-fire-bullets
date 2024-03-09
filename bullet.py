import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    #class that manges the bullets fired from the ship
    def __init__(self,ai_game):
        super().__init__()
        #creating bullets
        self.screen =ai_game.screen
        self.settings =ai_game.settings
        self.color =self.settings.bullet_color

        #creating a bullet at (0,0)and seting the correct position
        self.rect= pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop= ai_game.ship.rect.midtop

        #storing bullet's position as a decimal value
        self.y= float(self.rect.y)
    def update(self):
        #updating the decimal position of bullet.
        self.y -=self.settings.bullet_speed

        #updating the rect position
        self.rect.y= self.y
    def draw_bullet(self):
        #drawing the bullets to the scree.
        pygame.draw.rect(self.screen, self.color, self.rect)
