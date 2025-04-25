from scripts.path_utils import IMG_DIR
import pygame, pathlib
from scripts.enemy import Enemy, Enemy_group 
from scripts.poison import Poison, Poison_group 
from scripts.Exit import Exit, Exit_group

# Get the Screen surface
screen = pygame.display.get_surface()

# Block Size
tile_size = 50

'''
World class
-> Set up the whole game for block, Enemy, Poison, and Exit
-> Adding up all the blocks 
-> I'm the top of the World
'''
class World():
    def __init__(self, data):
        # tile list for graph
        self.tile_list = []
        # Block image
        img_redblock = pygame.image.load(IMG_DIR / "Red_Block.webp").convert_alpha()
        # row for window
        row_count = 0
        for row in data:
            # col for window
            col_count = 0
            # Each block 
            for tile in row:
                # Tile 1 for Block
                if tile == 1:
                    # Block Size
                    image1 = pygame.transform.scale(img_redblock, (tile_size, tile_size))
                    # Get rectangular coordinates
                    img_rect = image1.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    # Image showing
                    tile = (image1, img_rect)
                    # Add the block
                    self.tile_list.append(tile)
                # Tile 2 for Enemy
                if tile == 2:
                    # Enemy Size
                    Enemyobject1 = Enemy(col_count * tile_size, row_count * tile_size + 20)
                    # Add the Enemy to the tiles
                    Enemy_group.add(Enemyobject1)
                # Tile 4 for poison
                if tile == 4:
                    # Poison Size
                    poison = Poison(col_count * tile_size, row_count * tile_size + ((tile_size)// 2))
                    # Add the poison
                    Poison_group.add(poison)
                # Tile 5 for Exit
                if tile == 5:
                    # Exit Size
                    exit = Exit(col_count * tile_size, row_count * tile_size - 40)
                    # Add the exit
                    Exit_group.add(exit)
                # Loop for each col and row
                col_count += 1
            row_count += 1
    # Draw the world
    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
