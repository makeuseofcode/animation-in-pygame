import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game")

# Game variables
player_x = 400
player_y = 500
player_speed = 5
platform_x = 300
platform_y = 550
platform_width = 200
platform_height = 20

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Update game logic

    # Render the game
    screen.fill((0, 0, 0))  
    platform_pos = (platform_x, platform_y, platform_width, platform_height)
    player_pos = (player_x, player_y, 20, 20)
    pygame.draw.rect(screen, (255, 255, 255), platform_pos)  
    pygame.draw.rect(screen, (255, 0, 0), player_pos) 

    pygame.display.flip()

# Quit the game
pygame.quit()
