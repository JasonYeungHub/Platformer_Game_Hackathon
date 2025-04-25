from scripts.path_utils import IMG_DIR
import pygame, pathlib

# Set up Sprite Group for Exit
Exit_group = pygame.sprite.Group()

# Block size
tile_size = 50
'''
Exit class
-> For Exit
-> Set up the Sprite group to make it reachable
-> I quit bro it's too hard to play
'''
class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Sprite
        pygame.sprite.Sprite.__init__(self)
        # Image
        image = pygame.image.load(IMG_DIR / 'Exit_Door.png').convert_alpha()
        # Image Size
        self.image = pygame.transform.scale(image, (tile_size , tile_size * 2))
        # Get rectangular coordinates
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y