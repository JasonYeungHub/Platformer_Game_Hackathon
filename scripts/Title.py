from scripts.path_utils import IMG_DIR
import pygame, pathlib
'''
Title class for image
-> Set up the Title of the main menu
-> Most useless class ever
-> Fun
'''
class Title():
    def __init__(self, x, y, image):
        # Image define in main
        self.image = image
        # Get rectangular coordinates
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # Draw the image
    def draw(self, screen):
        
        screen.blit(self.image, self.rect)