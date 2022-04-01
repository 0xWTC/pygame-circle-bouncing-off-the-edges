# Use Pygame to draw a circle on the screen. The circle will move around the screen in a random direction. The circle will be red. The background will be black. The circle will bounce off the edges of the screen. The screen will flash white when it touches the edges of the screen and print the number of edge collisions to the console every time the circle touches the edges of the screen.

import pygame
import random

def random_move():
    ''' Return a random number. '''
    return random.randint(1, 4)

def count_edge_collisions(x, y, width, height):
    ''' Count the number of edge collisions. '''
    count = 0
    if x <= 0:
        count += 1
    if x >= width:
        count += 1
    if y <= 0:
        count += 1
    if y >= height:
        count += 1
    return count

def print_edge_collisions(count):
    ''' Print the number of edge collisions to the console. '''
    print("Edge collisions: " + str(count))

def display_edge_collisions_on_screen(count, screen):
    ''' Display the number of edge collisions on the screen. '''
    font = pygame.font.Font(None, 36)
    text = font.render("Edge collisions: " + str(count), 1, (255, 255, 255))
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    textpos.centery = screen.get_rect().centery
    screen.blit(text, textpos)
    pygame.display.update()
    pygame.time.wait(500)


def flash_screen_white(screen, width, height):
    ''' Flash the screen white for a short period of time. '''
    screen.fill((255, 255, 255))
    pygame.display.update()
    pygame.time.wait(40)
    screen.fill((0, 0, 0))
    pygame.display.update()
    pygame.time.wait(40)

def main():
    ''' Main function for the program. '''

    # Initialize Pygame
    pygame.init()
    
    # Set the height and width of the screen
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))

    # Set the title of the window
    pygame.display.set_caption("Circle")

    # Loop until the user clicks the close button.
    clock = pygame.time.Clock()

    # Set the background color
    screen.fill((0, 0, 0))

    # Initialize the circle
    x = 320
    y = 240

    # Initialize the circle's speed
    x_speed = random_move()
    y_speed = random_move()

    # Initialize the number of edge collisions
    edge_collisions = 0

    # Loop until the user clicks close or presses space.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    quit()

        # Move the circle
        screen.fill((0,0,0))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 40)
        pygame.display.update()
        clock.tick(150)

        x += x_speed
        y += y_speed

        # Check if the circle has collided with the edge of the screen
        if (x <= 0 or x >= width):
            x_speed *= -1
            edge_collisions += 1
            flash_screen_white(screen, width, height)
            display_edge_collisions_on_screen(edge_collisions, screen)
        if y <= 0 or y >= height:
            y_speed *= -1
            edge_collisions += 1
            flash_screen_white(screen, width, height)
            display_edge_collisions_on_screen(edge_collisions, screen)
    

if __name__ == "__main__":
    main()
