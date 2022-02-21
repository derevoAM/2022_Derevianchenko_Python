import pygame
import pygame.draw as dr

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill('grey')
dr.circle(screen, 'yellow', (300, 300), 200)
dr.rect(screen, 'black', (200, 400, 200, 50))
dr.circle(screen, 'red', (210, 240), 35)
dr.circle(screen, 'black', (210, 240), 20)
dr.circle(screen, 'red', (390, 240), 25)
dr.circle(screen, 'black', (390, 240), 15)
dr.polygon(screen, 'black', ([120, 130], [260, 220], [250, 230], [110, 140]))
dr.polygon(screen, 'black', ([485, 170], [355, 220], [360, 230], [490, 180]))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()