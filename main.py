import pygame
import math

# INITIALIZATIONS
pygame.init()

# ------------------------------ VARIABLES ------------------------------
WIDTH, HEIGHT = 750, 750


array = [3, 4, 5]

# linked list
CIRCLE_RAD = 50

window = pygame.display.set_mode((WIDTH, HEIGHT))


# ------------------------------ FUNCTIONS ------------------------------
# --- DRAWING ---
def draw_bg(win):
    win.fill("white")


def draw_list(win, arr):
    if len(arr) == 1:
        pygame.draw.circle(win, "red", (WIDTH/2, HEIGHT/2), CIRCLE_RAD)


def draw_list_1(win, arr):
    coordinates = polygone_calculator(len(arr), 200)
    for coord in coordinates:
        pygame.draw.circle(win, "red", coord, 50)


def draw(win, arr):
    draw_bg(win)
    draw_list_1(win, arr)



# --- position calculator
# Calculates the x,y coordinates of a polygone given the number of sides it has
def polygone_calculator(n, d):

    if n<3:
        return ((0,0))
    else:
        # Calculate the angle between consecutive vertices
        angle = 360 / n

        # Initialize a list to store the coordinates
        coordinates = []

        # Calculate coordinates for each vertex
        for i in range(n):
            x = d * math.cos(math.radians(i * angle)) + WIDTH/2
            y = d * math.sin(math.radians(i * angle)) + HEIGHT/2
            coordinates.append((x, y))

        return coordinates


def main(win, arr):
    clock = pygame.time.Clock()

    run = True
    while run:
        # Set a fixed number of frames per second
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    arr.append(1)
                if event.key == pygame.K_1:
                    arr.insert(0, 1)
                if event.key == pygame.K_2:
                    arr.insert(1, 1)
                if event.key == pygame.K_3:
                    arr.insert(2, 1)
                if event.key == pygame.K_4:
                    arr.insert(3, 1)
                if event.key == pygame.K_5:
                    arr.insert(4, 1)

        # drawing methods
        draw(win, arr)

        pygame.display.update()

    # Quit the program
    pygame.quit()
    quit()

# if we're running the main file directly
if __name__ == '__main__':
    main(window, array)

