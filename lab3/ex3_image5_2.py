from math import pi

import pygame
import pygame.draw as dr

# Constant fields
COLOR1 = (252, 152, 49)
COLOR2 = (172, 67, 52)
COLOR3 = (179, 134, 148)
COLOR4 = (254, 213, 148)
COLOR5 = (254, 213, 196)
COLOR6 = (48, 16, 38)
COLOR7 = (66, 33, 11)

HEIGHT = 800
WIDTH = 1500
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def bird(x, y):
    """
    Function to draw a bird
    :param x: coordinate
    :param y: coordinate
    :return: none
    """
    dr.polygon(screen, COLOR7, ([x, y], [x - 70, y - 32], [x - 63, y - 32], [x + 5, y - 15], [x + 70, y - 30],
                                [x + 73, y - 28]))
    for j in range(5):
        dr.arc(screen, COLOR7, [x - 247, y - 34 + j, 265, 65], 0.1 * pi, 0.36 * pi)
    for j in range(7):
        dr.arc(screen, COLOR7, [x + 5, y - 30 + j, 125, 45], (0.5 + j * 0.01) * pi, pi, 3)


def bird_squad(coordinates_array):
    """
    Function to draw a number of birds
    :param coordinates_array: array of birds' coordinates [[x1, y1], [x2, y2],...]
    :return: none
    """
    for coordinate in coordinates_array:
        bird(coordinate[0], coordinate[1])


def backend_fill(surface, width, fill_color, additional_color_1, additional_color_2, additional_color_3,
                 additional_color_4):
    """
    Function to fill the backend
    :param surface: surface to fill
    :param width: window width
    :param fill_color: main color to fill the surface
    :param additional_color_1: additional color
    :param additional_color_2: additional color
    :param additional_color_3: additional color
    :param additional_color_4: additional color
    :return: none
    """
    screen.fill(fill_color)
    dr.polygon(surface, additional_color_1, ([0, 0], [width, 0], [width, 200], [0, 200]))
    dr.polygon(surface, additional_color_2, ([0, 200], [width, 200], [width, 350], [0, 350]))
    dr.polygon(surface, additional_color_3, ([0, 350], [width, 350], [width, 510], [0, 510]))
    dr.circle(surface, additional_color_4, (700, 170), 100)


def draw_upper_mountain(surface, tuples_array, color):
    """
    Function to draw upper mountain
    :param surface: surface to draw upper mountain onto
    :param tuples_array: coordinates of key points to draw a chain
    :param color: color used
    :return: none
    """

    dr.polygon(surface, color, tuples_array)

    dr.aalines(surface, color, True,
               tuples_array)

    for iterator in range(-42, -20, 1):
        dr.arc(surface, color, [-425, iterator, 700, 380], 1.6 * pi, 1.87 * pi, 2)

    dr.circle(surface, color, (1097, 160), 30)

    for iterator in range(2, 40, 1):
        dr.arc(screen, color, [775, iterator, 300, 240], 1.45 * pi, 1.9 * pi, 2)
    dr.polygon(screen, color, ([1100, 170], [1065, 165], [1050, 220]))


def draw_second_mountain(surface, tuples_array, color, additional_color):
    """
    Function to draw the second mountain
    :param surface: surface to draw second mountain onto
    :param tuples_array: coordinates of key points to draw a chain
    :param color: color used
    :param additional_color: additional color
    :return: none
    """
    dr.polygon(surface, color, tuples_array)
    dr.aalines(surface, color, True, tuples_array)

    dr.ellipse(surface, color, (5, 320, 260, 420))

    dr.ellipse(surface, color, (960, 325, 115, 65))

    for iterator in range(325, 365, 1):
        dr.arc(surface, color, [840, iterator, 400, 340], 0.6 * pi, pi)

    for iterator in range(200, 250, 1):
        dr.arc(surface, color, [1100, iterator, 300, 225], 1.25 * pi, 1.5 * pi)

    dr.aaline(surface, color, (1150, 395), (1050, 330))
    dr.polygon(surface, color, ([1150, 395], [1050, 330], [930, 370], [850, 450], [1160, 470]))
    dr.polygon(surface, additional_color, ([0, 800], [1500, 800], [1500, 510], [0, 550]))


def draw_lowest_mountain(surface, tuples_array, color):
    """
    Function to draw the lowest mountain
    :param surface: surface to draw the lowest mountain onto
    :param tuples_array: coordinates of key points to draw a chain
    :param color: color used
    :return: none
    """
    dr.polygon(surface, color, tuples_array)
    dr.aalines(surface, color, True, tuples_array)

    for i in range(641, 670, 1):
        dr.arc(surface, color, [446, i, 360, 140], 1.13 * pi, pi * 1.5)

    for i in range(487, 550, 1):
        dr.arc(surface, color, [955, i, 315, 240], 1.25 * pi, 1.8 * pi)

    for i in range(400, 500, 1):
        dr.arc(surface, color, [1220, i, 1230, 780], 0.55 * pi, 0.9 * pi)

    for i in range(20):
        dr.aaline(surface, color, (1238, 678 + i), (1260, 650 + i))


upper_mountain_tuples = ([8, 370], [1500, 250], [1390, 210], [1340, 230], [1290, 202], [1265, 192], [1253, 189],
                         [1233, 189], [1180, 200], [1120, 150], [970, 270], [900, 240],
                         [860, 270], [800, 255], [725, 310], [675, 290], [570, 300], [390, 200], [365, 175],
                         [305, 160],
                         [175, 300], [20, 330])

second_mountain_tuples = (
    [0, 550], [1500, 510], [1500, 290], [1440, 360], [1380, 355], [1350, 400], [1290, 360], [1220, 430],
    [860, 420], [720, 450], [610, 390], [480, 360], [430, 470], [320, 430], [260, 510], [40, 410],
    [10, 400], [0, 400])

lowest_mountain_tuples = ([0, 400], [175, 440], [325, 590], [450, 730], [510, 780], [700, 780], [950, 670], [1000, 690],
                          [1110, 780], [1500, 475], [1500, 800], [0, 800])

bird_coordinates = [[1170, 635], [1025, 590], [1200, 570], [940, 540], [715, 330], [720, 290], [580, 280], [595, 360],
                    [580, 280]]

backend_fill(screen, WIDTH, COLOR3, 'NavajoWhite', COLOR5, COLOR4, 'yellow')
draw_upper_mountain(screen, upper_mountain_tuples, COLOR1)
draw_second_mountain(screen, second_mountain_tuples, COLOR2, COLOR3)
draw_lowest_mountain(screen, lowest_mountain_tuples, COLOR6)

bird_squad(bird_coordinates)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
