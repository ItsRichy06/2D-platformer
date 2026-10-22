import pygame
import sys

# 1. Initialize Pygame and Setup Window
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer Prototype")
clock = pygame.time.Clock()

# 2. Player Properties (Circle)
player_radius = 20
player_x = 100
player_y = 300
player_speed = 5

# Physics Variables
vel_y = 0
gravity = 0.8
jump_strength = -22
is_grounded = False

# 3. Platform Properties (Rectangle)
platform_rect = pygame.Rect(300, 400, 200, 20)  # X, Y, Width, Height

# Game Loop
running = True
while running:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 4. Input & Horizontal Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # 5. Apply Gravity
    vel_y += gravity
    player_y += vel_y

    # Create a bounding box for the circle to handle platform collisions easily
    player_rect = pygame.Rect(player_x - player_radius, player_y - player_radius, player_radius * 2, player_radius * 2)

    # 6. Collision: Floor of the screen
    if player_y + player_radius >= HEIGHT:
        player_y = HEIGHT - player_radius
        vel_y = 0
        is_grounded = True
    else:
        is_grounded = False

    # 7. Collision: Platform (Only land on top if falling down)
    if player_rect.colliderect(platform_rect):
        # Check if the player's bottom is hitting the top of the platform
        if vel_y > 0 and (player_y + player_radius - vel_y) <= platform_rect.top:
            player_y = platform_rect.top - player_radius
            vel_y = 0
            is_grounded = True

    # 8. Jump Input (Only allowed if standing on the floor or a platform)
    if keys[pygame.K_SPACE] and is_grounded:
        vel_y = jump_strength
        is_grounded = False

    # 9. Drawing Everything
    screen.fill((30, 30, 30))  # Dark gray background

    # Draw Platform (Green)
    pygame.draw.rect(screen, (46, 204, 113), platform_rect)

    # Draw Player (Red Circle)
    pygame.draw.circle(screen, (231, 76, 60), (int(player_x), int(player_y)), player_radius)

    # Update Display
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()
sys.exit()
