from scripts.path_utils import IMG_DIR, SND_DIR
import pygame, pathlib
from scripts.world import World
from scripts.enemy import Enemy, Enemy_group # , Enemy_group2
from scripts.poison import Poison, Poison_group 
from scripts.Exit import Exit, Exit_group
from pygame import mixer

# Set up the pygame mixer for sound
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

# Jumping Sound
jump_sound = pygame.mixer.Sound(SND_DIR / 'jump-up-245782.mp3')
jump_sound.set_volume(0.2)
# Winning Sound
win_sound = pygame.mixer.Sound(SND_DIR / 'win.mp3')
win_sound.set_volume(0.3)
# Losing sound
lose_sound = pygame.mixer.Sound(SND_DIR / 'lose.mp3')
lose_sound.set_volume(0.3)

screen_height = 1000 #Define the height locally

# Game over
game_over = 0
game_over2 = 0

'''
Player class
-> Set up player for playing
-> Reseting the character
-> Different Character (Mario blue and red)
-> I played this game beforeeeeee
-> Played 100 times still lose bro
'''
class Player():
    def __init__(self, x, y, skin):

        self.reset(x,y,skin)

    def update_player1(self, screen, world, game_over):
        
        # Direction X and Y, cold down for the image changing
        objectx = 0
        objecty = 0
        object_colddown = 10

        # Make a key object for the move of the player
        key = pygame.key.get_pressed()
        # Key for player1
        # When Up key press then jump
        if game_over == 0:
         if key[pygame.K_UP] and self.jump == False and self.in_air == False:
            jump_sound.play()
            self.vel_y = -12
            self.jump = True
        # Not keep jumping to the moon
         if key[pygame.K_UP] == False:
            self.jump = False
        # Key for going left and direction
         if key[pygame.K_LEFT]:
            objectx -= 2
            self.counter += 1
            self.direction = -1
        # Key for going right and direction
         if key[pygame.K_RIGHT]:
            objectx += 2
            self.counter += 1
            self.direction = 1
        # Stopping image direction
         if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            # Reset
            self.counter = 0
            self.index = 0
            # Check direction is left or right
            if self.direction == 1:
                self.image = self.image_right[self.index]
            if self.direction == -1:
                self.image = self.image_left[self.index]

        # The animation of the character
        # Reset the countering
         if self.counter > object_colddown:
            self.counter = 0
            self.index += 1
        # Over the index of the image then back to 0
         if self.index >= len(self.image_right):
            self.index = 0
        # Direction right image
         if self.direction == 1:
            self.image = self.image_right[self.index]
        # Direction left
         if self.direction == -1:
            self.image = self.image_left[self.index]

       # Gravity of the jump
         self.vel_y += 0.3
        # When the height bigger than the 3 then back to the floor 
         if self.vel_y > 3:
            self.vel_y = 3
         objecty += self.vel_y

        # Check for collision
        # Check in air or not
         self.in_air = True
         for tile in world.tile_list:
            # Check for collision in x direction
            if tile[1].colliderect(self.rect.x + objectx, self.rect.y, self.width, self.height):
                objectx = 0
            # Check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + objecty, self.width, self.height):
                # Check if below ground like jumping
                if self.vel_y < 0:
                    objecty = tile[1].bottom - self.rect.top
                # Check if above the ground like falling
                elif self.vel_y >= 0:
                    objecty = tile[1].top - self.rect.bottom
                    # In air then can't jump
                    self.in_air = False

        # Check for collision with enemy
         if pygame.sprite.spritecollide(self, Enemy_group, False):
            # Game over
            game_over = -1
            # Play lose sound
            lose_sound.play()
         if pygame.sprite.spritecollide(self, Poison_group, False):
            # Game over
            game_over = -1
            # Play lose sound
            lose_sound.play()
        # Check for getting to exit
         if pygame.sprite.spritecollide(self, Exit_group, False):
            # Win
            game_over = 1
            # Play win sound
            win_sound.play()
        
        # Movement
         self.rect.x += objectx
         self.rect.y += objecty

        # Show Player
        screen.blit(self.image, self.rect)

        return game_over
    
    def reset(self, x, y, skin):

        # List for the image right and left
        self.image_right = []
        self.image_left = []

        # Set up index and counting
        self.index = 0
        self.counter = 0

        # Set up two different color of Mario
        if skin == "red":
            name = "Mario_"
        elif skin == "blue":
            name = "BlueMario_"
        # Set up the image
        for i in range(0, 3):
            # Image for blue or red Mario
            image_right = pygame.image.load(IMG_DIR / f'{name}{i}.png').convert_alpha()
            # Size
            image_right = pygame.transform.scale(image_right, (30, 40))
            # Image for right
            self.image_right.append(image_right)
            # Image for left (Flip)
            image_left = pygame.transform.flip(image_right, True, False)
            self.image_left.append(image_left)
        # Image index
        self.image = self.image_right[self.index]

        # Get rectangular coordinates
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Get the area of the block (for collision)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # Player jumping
        self.vel_y = 0
        self.jump = False

        #Direction
        self.direction = 0

        # Collsion for jump
        self.in_air = True
    
    def update_player2(self, screen, world, game_over2):


        # Direction X and Y, cold down for the image changing
        objectx = 0
        objecty = 0
        object_colddown = 10

        # Make a key object for the move of the player
        key = pygame.key.get_pressed()
               
        # Key for player1
        # When Up key press then jump
        if game_over2 == 0:
         if key[pygame.K_w] and self.jump == False and self.in_air == False:
            jump_sound.play()
            self.vel_y = -12
            self.jump = True

        # Not keep jumping to the moon
         if key[pygame.K_w] == False:
            self.jump = False

        # Key for going left and direction
         if key[pygame.K_a]:
            objectx -= 2
            self.counter += 1
            self.direction = -1

        # Key for going right and direction   
         if key[pygame.K_d]:
            objectx += 2
            self.counter += 1
            self.direction = 1

        # Stopping image direction
         if key[pygame.K_a] == False and key[pygame.K_d] == False:
            self.index = 0
            self.counter = 0
            # Check direction is left or right
            if self.direction == 1:
                self.image = self.image_right[self.index]
            if self.direction == -1:
                self.image = self.image_left[self.index]

        # The animation of the character
        # Reset the countering
         if self.counter > object_colddown:
            self.counter = 0
            self.index += 1

        # Over the index of the image then back to 0
         if self.index >= len(self.image_right):
            self.index = 0
        
        # Direction right image
         if self.direction == 1:
            self.image = self.image_right[self.index]
        
        # Direction left
         if self.direction == -1:
            self.image = self.image_left[self.index]
        
        # Gravity of the jump
         self.vel_y += 0.3

        # When the height bigger than the 2.5 then back to the floor 
         if self.vel_y > 3:
            self.vel_y = 3  
         objecty += self.vel_y 

        # Check for collision
        # Check in air or not
         self.in_air = True
         for tile in world.tile_list:
            # Check for collision in x direction
            if tile[1].colliderect(self.rect.x + objectx, self.rect.y, self.width, self.height):
                objectx = 0
            # Check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + objecty, self.width, self.height):
                # Check if below ground like jumping
                if self.vel_y < 0:
                    objecty = tile[1].bottom - self.rect.top
                # Check if above the ground like falling
                elif self.vel_y >= 0:
                    objecty = tile[1].top - self.rect.bottom
                    # No in air then can't jump
                    self.in_air = False
        # Check for collision with enemis
         if pygame.sprite.spritecollide(self, Enemy_group, False):
            # Game over
            game_over2 = -1
             # Play lose sound
            lose_sound.play()
         if pygame.sprite.spritecollide(self, Poison_group, False):
            # Game over
            game_over2 = -1
             # Play lose sound
            lose_sound.play()
        # Check for getting to exit
         if pygame.sprite.spritecollide(self, Exit_group, False):
            # Win
            game_over2 = 1
            # Play win sound
            win_sound.play()
        
        # Movement
         self.rect.x += objectx
         self.rect.y += objecty

        # Show Player
        screen.blit(self.image, self.rect)

        return game_over2
