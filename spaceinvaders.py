def main():
    import pygame
    import random
    import math
    pygame.init()

    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Space Invaders")

    running = True
    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

main()