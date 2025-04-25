from scripts.path_utils import IMG_DIR
import pygame, pathlib

Enemy_group = pygame.sprite.Group()

'''
Enemy Class
-> Creating Enemy inside the Game
-> Seting up the Enemy Movement
-> I love slime
'''
class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # Sprite
        pygame.sprite.Sprite.__init__(self)
        # Image for Enemy (Slime)
        self.image = pygame.image.load(IMG_DIR / 'slime_1.png').convert_alpha()
        # Get rectangular coordinates
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Get direction
        self.move_direction = 1
        # Create counter
        self.move_counter = 0

    # Movement for the Enemy
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1

        # Range of Movement
        if abs(self.move_counter) < 1000 and abs(self.move_counter) > 300:
            self.move_direction *= -1
            self.move_counter *= -1
