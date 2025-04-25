from scripts.path_utils import IMG_DIR
import pygame, pathlib

'''
Button Class
-> Set up buttons
-> Start, Exit
-> Get mouse position for checking the clicks of the button
'''
class Button():
    def __init__(self, x, y, image):
        # Image define in main
        self.image = image
        # Get rectangular coordinates
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Check clicking
        self.click = False

    def draw(self, screen):

        action = False
        # Get Mouse Position
        pos = pygame.mouse.get_pos()

        # Check mouseover and click the button
        if self.rect.collidepoint(pos):
            # Check if the button get pressed
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                action = True
                self.click == True
        # Check the button is not clicked
        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False
        
        # Show the button
        screen.blit(self.image, self.rect)

        return action