import pygame
import pygame.draw as dr
from random import randint
import os


'''REMEMBER! GAME STOPS WHENEVER A KEY IS PRESSED! SO BE CAREFUL!'''
pygame.init()

FPS = 100
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    '''
    Function, which draws a random circle
    :return: circle parameters
    '''
    xcor = randint(100, 1100)
    ycor = randint(100, 900)
    radius = randint(20, 40)
    dx = randint(2, 5) * randint(-5, -2)
    dy = randint(2, 5) * randint(-5, -2)
    color = COLORS[randint(0, 5)]
    dr.circle(screen, color, (xcor, ycor), radius)
    return xcor, ycor, radius, dx, dy, color


def bonus_target(xcor, ycor):
    '''
    Function, which creates a bonus target
    :param xcor: x coordinate of a target
    :param ycor: y coordinate of a target
    :return: coordinates of a bonus target
    '''
    dr.circle(screen, 'green', (xcor, ycor), 60)
    dr.circle(screen, 'yellow', (xcor, ycor), 45)
    dr.circle(screen, 'purple', (xcor, ycor), 35)
    dr.circle(screen, 'orange', (xcor, ycor), 25)
    dr.circle(screen, 'red', (xcor, ycor), 10)


def ball_movement(xcor, ycor, rad, dx, dy, color, flag):
    '''
    Function, which redraws a circle as it moves and also changes it's direction, if a circle hits a wall
    :param xcor: x coordinate of a circle
    :param ycor: y coordinate of a circle
    :param rad: circle radius
    :param dx: x axis velocity
    :param dy: y axis velocity
    :param color: circle color
    :param flag: checks whether circle is a target (if True, than target)
    :return: circle parameters
    '''
    xcor += dx
    ycor += dy
    if flag == 0:
        dr.circle(screen, color, (xcor, ycor), rad)
    else:
        bonus_target(xcor, ycor)

    return xcor, ycor


def hit_wall(xcor, ycor, dx, dy):
    '''
    Function, which detects whether a circle hit the wall
    :param xcor: x coordinate of a circle
    :param ycor: y coordinate of a circle
    :param dx: x axis velocity
    :param dy: y axis velocity
    :return: x and y axes velocities
    '''
    if xcor + dx >= 1200:
        dx = randint(-10, -5)
        dy = randint(-10, 10)
    elif xcor + dx <= 0:
        dx = randint(5, 10)
        dy = randint(-10, 10)
    elif ycor + dy <= 0:
        dx = randint(-10, 10)
        dy = randint(5, 10)
    elif ycor + dy >= 900:
        dx = randint(-10, 10)
        dy = randint(-10, -5)
    return dx, dy


def click_check(event, xcor, ycor, rad, sc):
    '''
    Function, which checks whether the circle was caught by a mouse click
    :param event: event itself
    :param xcor: x coordinate of a circle
    :param ycor: y coordinate of a circle
    :param rad: radius of a circle
    :param sc: current score
    :return: new score
    '''
    x0, y0 = event.pos
    # print(x0, xcor, y0, ycor)
    if (x0 - xcor) ** 2 + (y0 - ycor) ** 2 <= rad ** 2:
        if rad <= 30:
            sc += 20
        elif rad <= 40:
            sc += 10
    return sc


def bonus_check(event, xcor, ycor, sc):
    '''
    Function, which checks whether the target was caught by a mouse click
    :param event: event itself
    :param xcor: x coordinate of a target
    :param ycor: y coordinate of a target
    :param sc: current score
    :return: new score
    '''
    x0, y0 = event.pos
    if (x0 - xcor) ** 2 + (y0 - ycor) ** 2 <= 60 ** 2:
        if (x0 - xcor) ** 2 + (y0 - ycor) ** 2 >= 45 ** 2:
            sc += 20
        elif (x0 - xcor) ** 2 + (y0 - ycor) ** 2 >= 35 ** 2:
            sc += 30
        elif (x0 - xcor) ** 2 + (y0 - ycor) ** 2 >= 25 ** 2:
            sc += 60
        else:
            sc += 100
    return sc


def find_name(name, lines, total):
    '''
    Function that determines whether a player is already in the results table
    :param name: Player name
    :param lines: Text file with results in the form of a list of lines
    :param total: current result of a player
    :return: 1.max value between current and past results
             2.index of a line, where the name of a player is occurred in file(return -1 if not found)
    '''
    for i in range(0, len(lines), 1):
        if name == lines[i].split()[0]:
            return max(total, int(lines[i].split()[1])), i
    return total, -1


def upload_file(name, total, row, lines):
    '''
    Funciton that upload Results table text file
    :param name: Player name
    :param total: current result of a player
    :param row: index of a line, where the name of a player is occurred in original file(equals -1 if not)
    :param lines: Text file with results in the form of a list of lines
    :return: none
    '''
    file.write('Results table\n')
    flag_name_written = 0
    for i in range(1, len(lines), 1):
        if i == row:
            if total <= int(lines[i].split()[1]):
                file.write(lines[i])
            else:
                if flag_name_written == 0:
                    file.write(name + ' ' + str(total) + '\n')
            flag_name_written = 1
        else:
            if (total > int(lines[i].split()[1])) and (flag_name_written == 0):
                file.write(name + ' ' + str(total) + '\n')
                flag_name_written = 1
            file.write(lines[i])
    if flag_name_written == 0:
        file.write(name + ' ' + str(total) + '\n')


pygame.display.update()
clock = pygame.time.Clock()
finished = False

n = 10 #number of targets

Xcor = []
Ycor = []
Radius = []
Vx = []
Vy = []
Color = []

score = 0

for i in range(n):
    x, y, r, vx, vy, col = new_ball()
    Xcor.append(x)
    Ycor.append(y)
    Radius.append(r)
    Vx.append(vx)
    Vy.append(vy)
    Color.append(col)

start_ticks = pygame.time.get_ticks()  # starter tick

xbonus = 0
ybonus = 0
Vxbonus = 0
Vybonus = 0
seconds = 0

time_flag = 0
pygame.display.update()
screen.fill(BLACK)
while (not finished) and (seconds <= 30):
    clock.tick(FPS)
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
    # print(seconds)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print('Click!')
            flag_penalty = 0
            for i in range(n):
                t = score
                score = click_check(event, Xcor[i], Ycor[i], Radius[i], score)
                if score > t:
                    Xcor[i], Ycor[i], Radius[i], Vx[i], Vy[i], Color[i] = new_ball()
                    flag_penalty = 1
            if flag_penalty == 0:
                score -= 10
            score = bonus_check(event, xbonus, ybonus, score)

    for i in range(n):
        Xcor[i], Ycor[i] = ball_movement(Xcor[i], Ycor[i], Radius[i], Vx[i], Vy[i], Color[i], 0)
        Vx[i], Vy[i] = hit_wall(Xcor[i], Ycor[i], Vx[i], Vy[i])

    if (seconds // 3) % 2 == 1:
        if time_flag == 0:
            xbonus = randint(100, 1100)
            ybonus = randint(100, 900)
            Vxbonus = randint(5, 10) * randint(-10, -5)
            Vybonus = randint(5, 10) * randint(-10, -5)
            time_flag = 1

        xbonus, ybonus = ball_movement(xbonus, ybonus, 0, Vxbonus, Vybonus, 0, 1)
        Vxbonus, Vybonus = hit_wall(xbonus, ybonus, Vxbonus, Vybonus)
    else:
        time_flag = 0
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
print('Total score: ', score)

player_name = input('Enter your name')

# creating and opening a file
if not os.path.exists("Results table.txt"):
    file = open("Results table.txt", "w+")
    file.write('Results table')
    file.close()

file = open("Results table.txt", "r+")
all = file.readlines()
file.close()

file = open("Results table.txt", "w+")
#

file.seek(0)
file.truncate(0)

total_score, row_number = find_name(player_name, all, score)
upload_file(player_name, total_score, row_number, all)

file.close()
