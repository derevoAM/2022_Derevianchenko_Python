import pygame
import pygame.draw as dr
import numpy as np

pygame.init()

COLOR1 = (252, 152, 49)
COLOR2 = (172, 67, 52)
COLOR3 = (179, 134, 148)
COLOR4 = (254, 213, 148)
COLOR5 = (254, 213, 196)
COLOR6 = (48, 16, 38)
COLOR7 = (66, 33, 11)


def bird(x, y):
    dr.polygon(screen, COLOR7, ([x, y], [x - 70, y - 32], [x - 63, y - 32], [x + 5, y - 15], [x + 70, y - 30],
                                [x + 73, y - 28]))
    for j in range(5):
        dr.arc(screen, COLOR7, [x - 247, y - 34 + j, 265, 65], 0.1 * np.pi, 0.36 * np.pi)
    for j in range(7):
        dr.arc(screen, COLOR7, [x + 5, y - 30 + j, 125, 45], (0.5 + j * 0.01) * np.pi, np.pi, 3)


FPS = 30
screen = pygame.display.set_mode((1500, 800))
# backend fill
screen.fill(COLOR3)
dr.polygon(screen, 'NavajoWhite', ([0, 0], [1500, 0], [1500, 200], [0, 200]))
dr.polygon(screen, COLOR5, ([0, 200], [1500, 200], [1500, 350], [0, 350]))
dr.polygon(screen, COLOR4, ([0, 350], [1500, 350], [1500, 510], [0, 510]))
dr.circle(screen, 'yellow', (700, 170), 100)

# TODO: change something
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

for i in range(-42, -20, 1):
    dr.arc(screen, COLOR1, [-425, i, 700, 380], 1.6 * np.pi, 1.87 * np.pi, 2)
dr.circle(screen, COLOR1, (1097, 160), 30)

for i in range(2, 40, 1):
    dr.arc(screen, COLOR1, [775, i, 300, 240], 1.45 * np.pi, 1.9 * np.pi, 2)
dr.polygon(screen, COLOR1, ([1100, 170], [1065, 165], [1050, 220]))

# 2 mountain
dr.polygon(screen, COLOR2,
           ([0, 550], [1500, 510], [1500, 290], [1440, 360], [1380, 355], [1350, 400], [1290, 360], [1220, 430],
            [860, 420], [720, 450], [610, 390], [480, 360], [430, 470], [320, 430], [260, 510], [40, 410],
            [10, 400], [0, 400]))

dr.ellipse(screen, COLOR2, (5, 320, 260, 420))

dr.ellipse(screen, COLOR2, (960, 325, 115, 65))

for i in range(325, 365, 1):
    dr.arc(screen, COLOR2, [840, i, 400, 340], 0.6 * np.pi, np.pi)

for i in range(200, 250, 1):
    dr.arc(screen, COLOR2, [1100, i, 300, 225], 1.25 * np.pi, 1.5 * np.pi)
dr.aaline(screen, COLOR2, (1150, 395), (1050, 330))
dr.polygon(screen, COLOR2, ([1150, 395], [1050, 330], [930, 370], [850, 450], [1160, 470]))
dr.polygon(screen, COLOR3, ([0, 800], [1500, 800], [1500, 510], [0, 550]))
dr.aalines(screen, COLOR2, True,
           ([0, 550], [1500, 510], [1500, 290], [1440, 360], [1380, 355], [1350, 400], [1290, 360], [1220, 430],
            [860, 420], [720, 450], [610, 390], [480, 360], [430, 470], [320, 430], [260, 510], [40, 410],
            [10, 400], [0, 400]))

# the lowest mountain
dr.polygon(screen, COLOR6,
           ([0, 400], [175, 440], [325, 590], [450, 730], [510, 780], [700, 780], [950, 670], [1000, 690],
            [1110, 780], [1500, 475], [1500, 800], [0, 800]))

for i in range(641, 670, 1):
    dr.arc(screen, COLOR6, [446, i, 360, 140], 1.13 * np.pi, np.pi * 1.5)

for i in range(487, 550, 1):
    dr.arc(screen, COLOR6, [955, i, 315, 240], 1.25 * np.pi, 1.8 * np.pi)

for i in range(400, 500, 1):
    dr.arc(screen, COLOR6, [1220, i, 1230, 780], 0.55 * np.pi, 0.9 * np.pi)

for i in range(20):
    dr.aaline(screen, COLOR6, (1238, 678 + i), (1260, 650 + i))
dr.aalines(screen, COLOR6, True,
           ([0, 400], [175, 440], [325, 590], [450, 730], [510, 780], [700, 780], [950, 670], [1000, 690],
            [1110, 780], [1500, 475], [1500, 800], [0, 800]))

# birds
bird(1170, 635)
bird(1025, 590)
bird(1200, 570)
bird(940, 540)
bird(715, 330)
bird(720, 290)
bird(580, 280)
bird(595, 360)
bird(580, 280)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
