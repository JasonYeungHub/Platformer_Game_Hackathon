import os, pygame
from pathlib import Path
from scripts.path_utils import IMG_DIR, SND_DIR
from scripts.world import World
from scripts.player import Player, game_over
from scripts.enemy import Enemy, Enemy_group 
from scripts.poison import Poison, Poison_group
from scripts.button import Button
from scripts.Title import Title
from scripts.Exit import Exit, Exit_group
from pygame import mixer

# Set up the sound mixer
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

# Set up the BMG
pygame.mixer.music.load(SND_DIR / 'game-music-loop-6-144641.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1,0.0, 0)
# Game's Screen Size
screen_width = 1750
screen_height = 1000

# Screen Display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption ('Platformer')

# Load background
IMG_DIR = Path(__file__).parent / "assets" / "images"
background_img = pygame.image.load(os.path.join(IMG_DIR / 'abstract-template-blue-background-white-squares-free-vector.jpg')).convert()
restart_image = pygame.image.load(IMG_DIR / 'restart_btn.png').convert_alpha()
Str_image = pygame.image.load(IMG_DIR / 'start_btn.png').convert_alpha()
exit_image = pygame.image.load(IMG_DIR / 'exit_btn.png').convert_alpha()
exit_image1 = pygame.image.load(IMG_DIR / 'exit_btn(1).png').convert_alpha()
Title_image = pygame.image.load(IMG_DIR / 'Title1.png').convert_alpha()

# Create Block inside the game
from scripts.levels import world_data #,world_data1

# Set up world and enemy
world = World(world_data)

#Green color
green = (144, 201, 120)

# Game over
game_over = 0
game_over2 = 0
# Main menu
main_menu = True

Title_text = Title(screen_width // 2 - 550, screen_height // 2 - 300, Title_image)
# Timer Setup
start_ticks = None # Will start when the game begins
time_limit = 30  # seconds

# Set up players
player1 = Player(100, screen_height - 100, "red")
player2 = Player(100, screen_height - 600, "blue")

# Create Restart Button
restart_button = Button(screen_width // 2 - 60, screen_height // 2 - 20, restart_image)

# Create Start Button
Str_button = Button(screen_width // 2 - 500, screen_height // 2, Str_image)

#Create Exit button
Exit_button = Button(screen_width // 2 + 200, screen_height // 2, exit_image)

Exit_button1 = Button(screen_width // 2 - 60, screen_height // 2 + 50, exit_image1)

# Fade overlay
FADE_ALPHA = 160          
fade_overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
fade_overlay.fill((0, 0, 0, FADE_ALPHA))     

# Game loop
running = True
while running:
    # Background
    screen.blit(background_img, (0, 0))

    if main_menu == True:
        # Text Information of the Player 
        Title_text.draw(screen)
        font = pygame.font.SysFont(None, 48)
        Player1__text1 = font.render("Player 1", True, (0, 0, 0))
        Player1__text2 = font.render("Right: D", True, (0, 0, 0))
        Player1__text3 = font.render("Left: A", True, (0, 0, 0))
        Player1__text4 = font.render("Jump: W", True, (0, 0, 0))
        screen.blit(Player1__text1, (20, 20))
        screen.blit(Player1__text4, (20, 70))
        screen.blit(Player1__text3, (20, 120))
        screen.blit(Player1__text2, (20, 170))
        Player2__text1 = font.render("Player 2", True, (0, 0, 0))
        Player2__text2 = font.render("Right: <-", True, (0, 0, 0))
        Player2__text3 = font.render("Left:   ->", True, (0, 0, 0))
        Player2__text4 = font.render("Jump: ^", True, (0, 0, 0))
        Player2__text5 = font.render("|", True, (0, 0, 0))
        screen.blit(Player2__text1, (1600, 20))
        screen.blit(Player2__text4, (1600, 70))
        screen.blit(Player2__text5, (1712, 70))
        screen.blit(Player2__text3, (1600, 120))
        screen.blit(Player2__text2, (1600, 170))

        # Check the Exit button (Exit)
        if Exit_button.draw(screen) == True:
            running = False
        # Check the Start button (Start)
        if Str_button.draw(screen) == True:
            main_menu = False
            start_ticks = pygame.time.get_ticks()
    else:
        # Draw worlds
        world.draw(screen)

        # Draw and update enemies
        Enemy_group.update()
        Enemy_group.draw(screen)

        # Draw Poison 
        Poison_group.draw(screen)

        # Draw Exit
        Exit_group.draw(screen)

        # Timer Countdown
        if start_ticks:
            
            # Time
            seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
            time_left = max(0, time_limit - seconds_passed)

            # Display the timer
            font = pygame.font.SysFont(None, 48)
            timer_text = font.render(f"Time Left: {time_left}", True, (255, 255, 255))
            screen.blit(timer_text, (20, 20))

            # Reset if time is up
            if time_left == 0:
                player1.reset(100, screen_height - 100, "red")
                player2.reset(100, screen_height - 600, "blue")
                game_over = 0
                start_ticks = pygame.time.get_ticks()  # Restart the timer

        # Game Over and adding player
        game_over = player1.update_player1(screen, world, game_over)
        game_over2 = player2.update_player2(screen, world, game_over2)

        # Player died
        # Both died will lose but one died keep playing
        if game_over == -1 and game_over2 == -1:
            # Stop the time
            start_ticks = None
            # Set up the overlay
            screen.blit(fade_overlay, (0, 0))
            # Set text
            font = pygame.font.SysFont(None, 48)
            # Text for lose
            Loser_text = font.render("No hopes for humans... Use the Time machine to go back", True, (255, 255, 255))
            # Show text
            screen.blit(Loser_text, (screen_width // 2 + - 450, screen_height // 2 - 100))
            # Restart
            if restart_button.draw(screen):
                player1.reset(100 ,screen_height - 100, "red")
                player2.reset(100, screen_height - 600, "blue")
                game_over = 0
                game_over2 = 0
                start_ticks = pygame.time.get_ticks()  # Restart the timer too  
            # Quit              
            elif Exit_button1.draw(screen) == True:
                running = False
        # Player win
        # If player 1 or 2 win then win
        if game_over == 1 or game_over2 == 1:
            # Stop the clock
            start_ticks = None
            # Set up the Text
            font = pygame.font.SysFont(None, 48)
            # Visible screen for overlay
            screen.blit(fade_overlay, (0, 0))
            # Text for win
            Winner_text = font.render("You survived!!!!", True, (255, 255, 255))
            # Show text
            screen.blit(Winner_text, (screen_width // 2 - 125, screen_height // 2 - 100))
            # Restart
            if restart_button.draw(screen):
                player1.reset(100 ,screen_height - 100, "red")
                player2.reset(100, screen_height - 600, "blue")
                game_over = 0
                game_over2 = 0
                start_ticks = pygame.time.get_ticks()  # Restart the timer too   
            # Quit             
            elif Exit_button1.draw(screen) == True:
                running = False
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()