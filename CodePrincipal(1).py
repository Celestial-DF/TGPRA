import pygame
print(pygame.ver)


pygame.init()
WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h
BACKGROUND = (0, 0, 0)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        screen.fill(BACKGROUND)
        pygame.display.flip()

        clock.tick(60)



if __name__ == "__main__":
    main()

https://youtu.be/YWN8GcmJ-jA