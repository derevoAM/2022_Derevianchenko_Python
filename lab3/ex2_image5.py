import pygame
import pygame.draw as dr
import numpy as np

pygame.init()

COLOR1 = (252, 152, 49)
COLOR2 = (172, 67, 52)
COLOR3 = (179, 134, 148)
COLOR4 = (254, 213, 148)
COLOR5 = (254, 213, 196)

FPS = 30
screen = pygame.display.set_mode((1500, 800))
#backend fill
screen.fill(COLOR3)
dr.polygon(screen, 'NavajoWhite', ([0, 0], [1500, 0], [1500, 200], [0, 200]))
dr.polygon(screen, COLOR5, ([0, 200], [1500, 200], [1500, 350], [0, 350]))
dr.polygon(screen, COLOR4, ([0, 350], [1500, 350], [1500, 510], [0, 510]))
dr.circle(screen, 'yellow', (700, 170), 100)

#upper mountain
dr.polygon(screen, COLOR1, ([8, 370], [1500, 250], [1390, 210], [1340, 230], [1290, 202], [1265, 192], [1253, 189],
                            [1233, 189], [1180, 200], [1120, 150], [970, 270], [900, 240],
                            [860, 270], [800, 255], [725, 310], [675, 290], [570, 300], [390, 200], [365, 175],
                            [305, 160],
                            [175, 300], [20, 330]))
dr.aalines(screen, COLOR1, True,
           ([8, 370], [1500, 250], [1390, 210], [1340, 230], [1290, 202], [1265, 192], [1253, 189],
            [1233, 189], [1180, 200], [1120, 150], [970, 270], [900, 240],
            [860, 270], [800, 255], [725, 310], [675, 290], [570, 300], [390, 200], [365, 175],
            [305, 160],
            [175, 300], [20, 330]))
dr.arc(screen, COLOR1, [-425, -42, 700, 380], 1.6 * np.pi, 1.87 * np.pi, 2)
for i in range(-42, -20, 1):
    dr.arc(screen, COLOR1, [-425, i, 700, 380], 1.6 * np.pi, 1.87 * np.pi, 2)
dr.circle(screen, COLOR1, (1097, 160), 30)
dr.arc(screen, COLOR1, [775, 2, 300, 240], 1.45 * np.pi, 1.9 * np.pi, 2)
for i in range(2, 40, 1):
    dr.arc(screen, COLOR1, [775, i, 300, 240], 1.45 * np.pi, 1.9 * np.pi, 2)
dr.polygon(screen, COLOR1, ([1100, 170], [1065, 165], [1050, 220]))


#lower mountain
dr.polygon(screen, COLOR2,
           ([0, 550], [1500, 510], [1500, 290], [1440, 360], [1380, 355], [1350, 400], [1290, 360], [1220, 430],
            [860, 420], [720, 450], [610, 390], [480, 360], [430, 470], [320, 430], [260, 510], [40, 410],
            [10, 400], [0, 400]))

dr.ellipse(screen, COLOR2, (5, 320, 260, 420))

dr.ellipse(screen, COLOR2, (960, 325, 115, 65))
dr.arc(screen, COLOR2, [840, 325, 400, 340], 0.6 * np.pi, np.pi)
for i in range(325, 365, 1):
    dr.arc(screen, COLOR2, [840, i, 400, 340], 0.6 * np.pi, np.pi)
dr.arc(screen, COLOR2, [1100, 200, 300, 225], 1.25 * np.pi, 1.5 * np.pi)
for i in range(200, 250, 1):
    dr.arc(screen, COLOR2, [1100, i, 300, 225], 1.25 * np.pi, 1.5 * np.pi)
dr.aaline(screen, COLOR2, (1150, 395), (1050, 330))
dr.polygon(screen, COLOR2, ([1150, 395], [1050, 330], [930, 370], [850, 450], [1160, 470]))
dr.polygon(screen, COLOR3, ([0, 800], [1500, 800], [1500, 510], [0, 550]))
dr.aalines(screen, COLOR2, True,
           ([0, 550], [1500, 510], [1500, 290], [1440, 360], [1380, 355], [1350, 400], [1290, 360], [1220, 430],
            [860, 420], [720, 450], [610, 390], [480, 360], [430, 470], [320, 430], [260, 510], [40, 410],
            [10, 400], [0, 400]))



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
