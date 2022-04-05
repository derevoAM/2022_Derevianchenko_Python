import math
from random import choice
from random import randint
import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 1400
HEIGHT = 800


class Bullet:
    def __init__(self, scr: pygame.Surface, x=40, y=450):
        """
        Constructor of class Bullet
        :param scr: screen
        :param x: initial x coordinate
        :param y: initial y coordinate
        """
        self.screen = scr
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.r = 0

    def move(self, x0, y0):
        pass

    def draw(self):
        """
        Function, which draws a bullet
        """
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r + 5) ** 2:
            return True
        else:
            return False


class Ball(Bullet):
    def __init__(self, scr: pygame.Surface, x_cor, y_cor):
        """ Constructor of class ball
        :param x_cor: initial x coordinate
        :param y_cor: initial y coordinate
        """
        super().__init__(scr)
        self.r = 5
        self.x = x_cor
        self.y = y_cor

    def move(self, x0, y0):
        """
        Function, which moves the ball
        x0 and y0 - flags for a mine
        """
        if (x0 != -10) or (y0 != -10):
            if (self.x + self.vx > 1410) or (self.x + self.vx * 1 / 2 < -10):
                self.vx *= -0.9
            elif self.y + self.vy < 0:
                self.vy *= -1
            elif self.y + self.vy > 780:
                self.vy *= -0.5
                self.vx *= 0.5

        self.x += self.vx
        self.y += self.vy * 1 / 2
        if abs(self.vx) < 1:
            self.vy = 0
            self.vx = 0
        else:
            self.vy += 9.81 * 1 / 5


class BrokenMissile(Bullet):
    def __init__(self, scr: pygame.surface, eve, x_cor, y_cor):
        """
        Constructor of class BrokenMissile
        :param scr: screen
        :param eve: events
        :param x_cor: initial x coordinate of a missile
        :param y_cor: initial y coordinate of a missile
        """
        super().__init__(scr)
        self.length = 20
        self.width = 5
        self.event = eve
        self.an = 1
        self.r = 10
        self.x = x_cor
        self.y = y_cor

    def move(self, x_cor, y_cor):
        """
        Function, which draws a missile
        :param x_cor: x coordinate of a mouse
        :param y_cor: x coordinate of a mouse
        :return:
        """
        self.an = -math.atan2((y_cor - self.y), (x_cor - self.x))
        self.x += 30 * math.cos(self.an)
        self.y += 30 * math.sin(self.an)


class Gun:
    def __init__(self, scr, tank_type):
        """
        Constructor of class Gun
        :param scr: screen
        :param tank_type: type of tank: either the one that we control("friend"), either the one that tries to kill us("enemy")
        """
        self.screen = scr
        self.f2_power = 20
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.direction = "left"
        self.left = 0
        self.right = 0
        self.type = tank_type
        if self.type == "friend":
            self.x = 50
            self.y = 700
        else:
            self.x = 20
            self.y = 51

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, eve, arr, bullet_number):
        """
        Ball shooting
        Happens when the mouse button is unpressed
        If left mouse button is pressed, a typical bullet(ball) flies out. If right mouse button is pressed, a broken missile flies out
        :param eve: events
        :param arr: array of bullets(balls)
        :param bullet_number: index of a bullet
        :return balls array, index of a ball
        """
        if eve.button == 3:
            new_missile = BrokenMissile(screen, eve, self.x, self.y)
            arr.append(new_missile)
            bullet_number += 1
        elif eve.button == 1:
            bullet_number += 1
            new_ball = Ball(self.screen, self.x, self.y)
            new_ball.r += 5
            self.an = math.atan2((eve.pos[1] - new_ball.y), (eve.pos[0] - new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = + self.f2_power * math.sin(self.an)
            arr.append(new_ball)

        self.f2_on = 0
        self.f2_power = 10
        return arr, bullet_number

    def target_enemy(self, obj, obj2):
        """
        Function, which checks whether an enemy tank hit us. If so, the game stops.
        :param obj: object of class Gun ("friend" one)
        :param obj2: object of class Ball - shot by the enemy tank
        :return:
        """
        if obj.x - self.x != 0:
            self.an = math.atan((obj.y - self.y) / (obj.x - self.x))
        else:
            self.an = math.pi / 2
        obj2.move(-10, -10)
        obj2.draw()
        if (obj.x - obj2.x) ** 2 + (obj.y - obj2.y) ** 2 <= 28 ** 2:
            return True
        return False

    def new_enemy(self):
        """
        Function, which creates a bullet for enemy tank
        :return: object ball
        """
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        new_ball.vx = self.f2_power * math.cos(self.an) * 1.3
        new_ball.vy = + self.f2_power * math.sin(self.an)
        return new_ball

    def targeting(self, eve):
        """
        Targeting of a gun, depends on a mouse position
        :param eve: events
        :return:
        """
        if eve:
            if eve.pos[0] - self.x != 0:
                self.an = math.atan((eve.pos[1] - self.y) / (eve.pos[0] - self.x))
                if eve.pos[0] < self.x:
                    self.direction = "left"
                else:
                    self.direction = "right"
            elif eve.pos[1] - self.y > 0:
                self.an = math.pi / 2
            else:
                self.an = -math.pi / 2

        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def event_check(self, event_list):
        """
        Function, which is used to move a tank, when any arrow is pressed
        :param event_list: events
        """
        if self.type == "friend":
            for event in event_list:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.left = 1
                    elif event.key == pygame.K_RIGHT:
                        self.right = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.left = 0
                    elif event.key == pygame.K_RIGHT:
                        self.right = 0
            if self.left == 1:
                self.x -= 6
                if self.x < 50:
                    self.x += 6
            if self.right == 1:
                self.x += 6
                if self.x > 550:
                    self.x -= 6

    def draw_tank(self, tank_type):
        """
        Function, which is used to draw a tank without a gun
        :param tank_type: checks the type of tank: "friend" or "enemy
        """
        k = 1
        if tank_type == "enemy":
            k = -1
            pygame.draw.polygon(self.screen,
                                "green",
                                [[0, 22], [1400, 22], [1400, 0], [0, 0]])
        else:
            pygame.draw.polygon(self.screen,
                                "green",
                                [[0, 728], [1400, 728], [1400, 800], [0, 800]])
        pygame.draw.polygon(
            self.screen,
            "dark green",
            [[self.x - 25, self.y + k * 5], [self.x + 25, self.y + k * 5], [self.x + 25, self.y + k * 20],
             [self.x - 25, self.y + k * 20]]
        )
        pygame.draw.polygon(
            self.screen,
            "dark green",
            [[self.x - 10, self.y - k * 10], [self.x + 10, self.y - k * 10], [self.x + 10, self.y + k * 5],
             [self.x - 10, self.y + k * 5]]
        )
        pygame.draw.circle(
            self.screen,
            "black",
            [self.x - 15, self.y + k * 20], 8
        )
        pygame.draw.circle(
            self.screen,
            "black",
            [self.x + 15, self.y + k * 20], 8
        )

    def draw(self, event_list):
        """
        Function, which is used to draw a whole tank with a gun
        :param event_list: events
        """
        self.event_check(event_list)
        self.draw_tank(self.type)
        if self.direction == "right" and self.type == "friend" or self.direction == "left" and self.type == "enemy":
            pygame.draw.polygon(
                self.screen,
                self.color,
                [[self.x, self.y], [self.x - 5 * math.sin(self.an), self.y + 5 * math.cos(self.an)],
                 [self.x - 5 * math.sin(self.an) + self.f2_power * math.cos(self.an),
                  self.y + 5 * math.cos(self.an) + self.f2_power * math.sin(self.an)],
                 [self.x + self.f2_power * math.cos(self.an), self.y + self.f2_power * math.sin(self.an)]]
            )
        else:
            pygame.draw.polygon(
                self.screen,
                self.color,
                [[self.x, self.y], [self.x + 5 * math.sin(self.an), self.y - 5 * math.cos(self.an)],
                 [self.x + 5 * math.sin(self.an) - self.f2_power * math.cos(self.an),
                  self.y - 5 * math.cos(self.an) - self.f2_power * math.sin(self.an)],
                 [self.x - self.f2_power * math.cos(self.an), self.y - self.f2_power * math.sin(self.an)]]
            )

    def power_up(self):
        """
        Function, which increases shot power
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, scr, number):
        """
        Constructor for class Target
        :param scr: screen
        :param number: index of a target - a position of main targets depends on this parameter
        """
        if number == 0:
            self.x = randint(1200, 1350)
            self.vy = -10
        else:
            self.x = randint(900, 1150)
            self.vy = 10
        self.y = randint(50, 750)
        self.r = randint(15, 50)
        self.color = BLACK
        self.points = 0
        self.live = 1
        self.screen = scr

    def new_target(self, number):
        """
        Function, which creates a new target
        :param number: index of a target
        """
        if number == 0:
            self.x = randint(900, 1150)
        else:
            self.x = randint(900, 1150)
        self.y = randint(50, 750)
        self.r = randint(15, 50)
        self.color = RED

    def hit(self, points=1):
        """
        Adding points, if the target was hit
        """
        self.points += points

    def draw(self):
        """
        Function, which draws two main targets
        """
        self.y += self.vy
        if (self.y < 50) or (self.y > 750):
            self.vy *= -1
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


class Mine(Target):
    def __init__(self, scr, number):
        """
        constructor for class Mine
        :param scr: screen
        :param number: index of a target
        """
        super().__init__(scr, number)
        self.x = randint(100, 1100)
        self.y = randint(100, 700)
        self.r = 20
        self.dx = randint(2, 5) * randint(-5, -2)
        self.dy = randint(2, 5) * randint(-5, -2)

    def hit_wall(self):
        """
        Function, which checks if a wall was hit by a mine
        """
        if self.x + self.dx >= 1200:
            self.dx = randint(-20, -10)
            self.dy = randint(-20, 20)
        elif self.x + self.dx <= 0:
            self.dx = randint(10, 20)
            self.dy = randint(-20, 20)
        elif self.y + self.dy <= 0:
            self.dx = randint(-20, 20)
            self.dy = randint(10, 20)
        elif self.y + self.dy >= 700:
            self.dx = randint(-20, 200)
            self.dy = randint(-20, -10)

    def move(self):
        """
        Function, which draws a mine
        """
        self.hit_wall()
        self.x += self.dx
        self.y += self.dy
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.polygon(self.screen, self.color,
                            [[self.x - 20, self.y], [self.x, self.y - 50], [self.x + 20, self.y]])
        pygame.draw.polygon(self.screen, self.color,
                            [[self.x - 20, self.y], [self.x, self.y + 50], [self.x + 20, self.y]])
        pygame.draw.polygon(self.screen, self.color,
                            [[self.x, self.y - 20], [self.x - 50, self.y], [self.x, self.y + 20]])
        pygame.draw.polygon(self.screen, self.color,
                            [[self.x, self.y - 20], [self.x + 50, self.y], [self.x, self.y + 20]])
        pygame.draw.polygon(self.screen, self.color,
                            [[self.x - 20 / math.sqrt(2), self.y + 20 / math.sqrt(2)],
                             [self.x - 50 / math.sqrt(2), self.y - 50 / math.sqrt(2)],
                             [self.x + 20 / math.sqrt(2), self.y - 20 / math.sqrt(2)]])
        pygame.draw.polygon(self.screen, self.color,
                            [[self.x - 20 / math.sqrt(2), self.y + 20 / math.sqrt(2)],
                             [self.x + 50 / math.sqrt(2), self.y + 50 / math.sqrt(2)],
                             [self.x + 20 / math.sqrt(2), self.y - 20 / math.sqrt(2)]])
        pygame.draw.polygon(self.screen, self.color,
                            [[self.x + 20 / math.sqrt(2), self.y + 20 / math.sqrt(2)],
                             [self.x - 50 / math.sqrt(2), self.y + 50 / math.sqrt(2)],
                             [self.x - 20 / math.sqrt(2), self.y - 20 / math.sqrt(2)]])
        pygame.draw.polygon(self.screen, self.color,
                            [[self.x + 20 / math.sqrt(2), self.y + 20 / math.sqrt(2)],
                             [self.x + 50 / math.sqrt(2), self.y - 50 / math.sqrt(2)],
                             [self.x - 20 / math.sqrt(2), self.y - 20 / math.sqrt(2)]])

    def hit_check(self, arr):
        """
        Function, which checks whether any ball hit a mine. If so, the game stops.
        :param arr: array of balls
        :return: true or false,
        """
        for a in arr:
            if (a.x - self.x) ** 2 + (a.y - self.y) ** 2 <= (a.r + self.r + 40) ** 2:
                return True
        return False


class SmallTarget(Target):
    def __init__(self, scr, number):
        """
        Constructor for class SmallTarget - small targets, which suddenly flies out of nowhere.
        :param scr: screen
        :param number: index of a small target
        """
        super().__init__(scr, number)
        self.x = randint(50, 1000)
        self.y = randint(60, 100)
        self.color = choice(GAME_COLORS)
        self.vx = 15 * math.cos(math.pi * number / 10)
        self.vy = 15 * math.sin(math.pi * number / 10)
        self.border_color = choice(GAME_COLORS)
        self.r = randint(8, 15)

    def move(self):
        """
        Function, which moves a small target
        """
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        """
        Function, which draws a small target
        """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.arc(self.screen, self.border_color, (self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r), 0,
                        2 * math.pi, 4)


def flag_checks(sec, flag, target_array, balls_array, missiles_array, missile_flag):
    """
    Function, which controls when to draw objects(targets and guns)
    :param sec: seconds
    :param flag: flag, which controls target appearance
    :param target_array: targets
    :param balls_array: balls
    :param missiles_array: missiles
    :param missile_flag: moment of time, when right mouse button was clicked
    :return: none
    """
    if sec - flag[0] > 3:
        target_array[0].draw()
    if sec - flag[1] > 3:
        target_array[1].draw()
    for ball in balls_array:
        ball.draw()
    for missile in missiles_array:
        if sec - missile_flag < 2:
            missile.draw()
        else:
            missiles_array.remove(missile)


def event_analyzer(event_list, finish, sec, missiles_array, bullet_array, balls_array, missile_flag):
    """
    Function, which analyzes events
    :param event_list: event list
    :param finish: checks, whether window was closed
    :param sec: seconds
    :param missiles_array: missiles
    :param bullet_array: bullets
    :param balls_array: balls
    :param missile_flag: moment of time, when right mouse button was clicked
    :return: finish, missiles_array, missile_flag, balls_array, bullet_array
    """
    for event in event_list:
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                missiles_array, bullet_array = gun.fire2_end(event, missiles_array, bullet_array)
                missile_flag = sec
            elif event.button == 1:
                balls_array, bullet_array = gun.fire2_end(event, balls_array, bullet_array)
        elif event.type == pygame.MOUSEMOTION:
            gun.targeting(event)
    return finish, missiles_array, missile_flag, balls_array, bullet_array


def bullet_position_analyzer(bullet_array, target_array, flag, sec, x, y, define_bullet):
    """
    Function, which analyzes bullet position and checks, whether it hit a target
    :param bullet_array: balls
    :param target_array: targets
    :param flag:  flag, which controls target appearance
    :param sec: seconds
    :param x: mouse position x coordinate
    :param y: mouse position y coordinate
    :param define_bullet: checks, whether it's a ball or a missile
    :return: target_array, missiles_array, flag
    """
    for b in bullet_array:
        b.move(x, y)
        for i in range(len(target_array)):
            if b.hittest(target_array[i]) and target_array[i].live:
                target_array[i].live = 0
                target_array[i].hit()
                target_array[i].new_target(i)
                flag[i] = sec
                bullet_array.remove(b)

            if sec - flag[i] > 3:
                target_array[i].live = 1
        if define_bullet == "ball":
            if (b.vx == 0) and (b.vy == 0):
                bullet_array.remove(b)
    return target_array, bullet_array, flag


def initiate_small_targets(scr):
    """
    Function, which initiates small targets
    :return: array of small targets
    """
    arr = []
    for i in range(21):
        arr.append(SmallTarget(scr, i))
    return arr


def enemy_analyzer(arr, sec, en_sec, en_ball):
    """
    Function, which controls the appearance of small targets
    :param arr: array of small targets
    :param sec: seconds
    :param en_sec: flag for enemy shooting
    :param en_ball:enemy ball
    :return:enemy seconds, enemy ball, array of small targets
    """
    for small_target in arr:
        small_target.move()
        small_target.draw()
    if sec - en_sec >= 4:
        en_sec = sec
        en_ball = enemy.new_enemy()
        arr = initiate_small_targets(screen)
    return en_sec, en_ball, arr


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
missiles = []
target = [Target(screen, 0), Target(screen, 1)]
gun = Gun(screen, "friend")
finished = False
missile_seconds = 0
enemy_seconds = -1
flag_seconds = [0, 0]
enemy = Gun(screen, "enemy")
enemy_flag = 0
enemy_ball = Ball(screen, enemy.x, enemy.y)
mine = Mine(screen, 1)
small_targets = initiate_small_targets(screen)
flag_small = [0] * 21

clock = pygame.time.Clock()

start_ticks = pygame.time.get_ticks()

while not finished:
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000

    screen.fill(WHITE)
    events = pygame.event.get()
    gun.draw(events)
    enemy_seconds, enemy_ball, small_targets = enemy_analyzer(small_targets, seconds, enemy_seconds, enemy_ball)
    flag1_finished = enemy.target_enemy(gun, enemy_ball)
    enemy.draw(events)

    flag_checks(seconds, flag_seconds, target, balls, missiles, missile_seconds)
    mine.move()
    flag2_finished = mine.hit_check(balls)
    if (flag2_finished == True) or (flag1_finished == True):
        finished = True
    else:
        finished = False
    pygame.display.update()
    clock.tick(FPS)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    finished, missiles, missile_seconds, balls, bullet = event_analyzer(events, finished, seconds, missiles, bullet,
                                                                        balls, missile_seconds)
    target, missiles, flag_seconds = bullet_position_analyzer(missiles, target, flag_seconds, seconds, mouse_x, mouse_y,
                                                              "missile")
    target, balls, flag_seconds = bullet_position_analyzer(balls, target, flag_seconds, seconds, mouse_x, mouse_y,
                                                           "ball")
    small_targets, balls, flag_small = bullet_position_analyzer(balls, small_targets, flag_small, seconds, mouse_x,
                                                                mouse_y, "ball")
    gun.power_up()

pygame.quit()
