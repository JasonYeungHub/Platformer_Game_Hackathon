from scripts.path_utils import IMG_DIR
import pygame, pathlib

# Set up Poison Group
Poison_group = pygame.sprite.Group()
#Block size
tile_size = 50

'''
Poison class 
-> Set a poison block
-> Player will die after poison
-> As toxic as me
'''
class Poison(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Sprite
        pygame.sprite.Sprite.__init__(self)
        # Image
        image = pygame.image.load(IMG_DIR / 'image_Poison.png').convert_alpha()
        # Size of the image
        self.image = pygame.transform.scale(image, (tile_size, tile_size // 2))
        # Get rectangular coordinates
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
