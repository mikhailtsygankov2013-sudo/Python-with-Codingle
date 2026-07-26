import pygame

pygame.init()
screen = pygame.display.set_mode((300,400))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(100,150,120,60))
    pygame.display.flip()
