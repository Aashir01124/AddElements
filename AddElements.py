import pygame

pygame.init()

Width, Height = 800, 600
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Pygame Rectangle and Text Example")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 74)
text_surface = font.render('Hello, World.', True, BLACK)

rect_width, rect_height = 200, 100
rect_x, rect_y = (Width - rect_width) // 2, (Height - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, rectangle)
    screen.blit(text_surface, (Width // 2 - text_surface.get_width() // 2, Height // 2 - text_surface.get_height() // 2))
    pygame.display.flip()

pygame.quit()