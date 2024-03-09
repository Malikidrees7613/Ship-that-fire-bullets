import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien



class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings= Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))


        self.screen =pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets= pygame.sprite.Group()
        self.aliens= pygame.sprite.Group()
        self.bg_color= (230, 230,230)
       
        

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            #print(len(self.bullets))
            self._update_screen()
            self._create_fleet()
            


           
    def _check_events(self):
        for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    sys.exit()
                elif event.type== pygame.KEYDOWN:
                    self._check_keydown_event(event)
                   
                elif event.type== pygame.KEYUP:
                    self._check_keyup_event(event)
                    
    
    def _check_keydown_event(self, event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key==pygame.K_UP:
            self.ship.moving_up = True
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_event(self, event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key==pygame.K_UP:
            self.ship.moving_up = False
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _fire_bullet(self):
        #creating new bullet and add it to the bullet group
        if len(self.bullets)< self.settings.bullet_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    def _create_fleet(self):
        #creating the fleet of alien
        alien = Alien(self)
        self.aliens.add(alien)

    def _update_bullets(self):
        self.bullets.update()
            #Delleting the bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitem()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

if __name__=='__main__':
    ai= AlienInvasion()
    ai.run_game()