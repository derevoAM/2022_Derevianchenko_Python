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
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
    def move(self, x0, y0):
        pass
    def draw(self):
        pass
    def hittest(self, obj):
        pass





# class Ball:
#     def __init__(self, screen: pygame.Surface, x=40, y=450):
#         """ Конструктор класса ball
#
#         Args:
#         x - начальное положение мяча по горизонтали
#         y - начальное положение мяча по вертикали
#         """
#         self.screen = screen
#         self.x = x
#         self.y = y
#         self.r = 10
#         self.vx = 0
#         self.vy = 0
#         self.color = choice(GAME_COLORS)
#         self.live = 30
#
#     def move(self):
#         """Переместить мяч по прошествии единицы времени.
#
#         Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
#         self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
#         и стен по краям окна (размер окна 800х600).
#         """
#         # FIXME
#         if (self.x + self.vx * 1 / 2 > 810) or (self.x + self.vx * 1 / 2 < -10):
#             self.vx *= -0.9
#         elif self.y + self.vy < 0:
#             self.vy *= -1
#         elif self.y + self.vy > 580:
#             self.vy *= -0.5
#             self.vx *= 0.5
#
#         self.x += self.vx * 1 / 2
#         self.y += self.vy * 1 / 2
#         if abs(self.vx) < 1:
#             self.vy = 0
#             self.vx = 0
#         else:
#             self.vy += 9.81 * 1 / 5
#
#     def draw(self):
#         pygame.draw.circle(
#             self.screen,
#             self.color,
#             (self.x, self.y),
#             self.r
#         )
#
#     def hittest(self, obj):
#         """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
#
#         Args:
#             obj: Обьект, с которым проверяется столкновение.
#         Returns:
#             Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
#         """
#         # FIXME
#         if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2:
#             return True
#         else:
#             return False

class Ball(Bullet):
    def __init__(self, screen: pygame.Surface):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        super().__init__(screen)
        self.r = 10

    def move(self, x0, y0):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
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

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r + 5) ** 2:
            return True
        else:
            return False


class Missile(Bullet):
    def __init__(self, screen: pygame.surface, event):
        """
        Конструктор класса Missile
        :param screen:
        """
        super().__init__(screen)
        self.length = 20
        self.width = 5
        self.event = event
        self.an = 1
        self.r = 10

    def move(self, x_cor, y_cor):
        self.an = math.atan2((y_cor - self.y), (x_cor - self.x))
        self.x += 30 * math.cos(self.an)
        self.y += 30 * math.sin(self.an)

    def draw(self):
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




class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event, arr, bullet_number):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        if event.button == 3:
            new_missile = Missile(screen, event)
            arr.append(new_missile)
            bullet_number += 1
        elif event.button == 1:
            bullet_number += 1
            new_ball = Ball(self.screen)
            new_ball.r += 5
            self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = + self.f2_power * math.sin(self.an)
            arr.append(new_ball)

        self.f2_on = 0
        self.f2_power = 10
        return arr, bullet_number

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] - 20 != 0:
                self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 20))
            elif event.pos[1] - 450 > 0:
                self.an = math.pi / 2
            else:
                self.an = -math.pi / 2

        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.polygon(
            self.screen,
            self.color,
            [[20, 450], [20 - 5 * math.sin(self.an), 450 + 5 * math.cos(self.an)],
             [20 - 5 * math.sin(self.an) + self.f2_power * math.cos(self.an),
              450 + 5 * math.cos(self.an) + self.f2_power * math.sin(self.an)],
             [20 + self.f2_power * math.cos(self.an), 450 + self.f2_power * math.sin(self.an)]]
        )

    # FIXIT don't know how to do it

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY





class Target:
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()
    def __init__(self, screen, number):
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
        self.screen = screen

    def new_target(self, number):
        """ Инициализация новой цели. """
        if number == 0:
            self.x = randint(900, 1150)
        else:
            self.x = randint(900, 1150)
        self.y = randint(50, 750)
        self.r = randint(15, 50)
        self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        self.y += self.vy
        if (self.y < 50) or (self.y >750):
            self.vy *= -1
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
missiles = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = [Target(screen, 0), Target(screen, 1)]

finished = False

start_ticks = pygame.time.get_ticks()

missile_seconds = 0
flag_seconds = [0, 0]

while not finished:
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    screen.fill(WHITE)
    gun.draw()
    if seconds - flag_seconds[0] > 3:
        target[0].draw()
    if seconds - flag_seconds[1] > 3:
        target[1].draw()
    for b in balls:
        b.draw()
    for m in missiles:
        if seconds - missile_seconds < 2:
            m.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                missiles, bullet = gun.fire2_end(event, missiles, bullet)
                missile_seconds = seconds
            elif event.button == 1:
                balls, bullet = gun.fire2_end(event, balls, bullet)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for m in missiles:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        m.move(mouse_x, mouse_y)
        for i in range(2):
            if m.hittest(target[i]) and target[i].live:
                target[i].live = 0
                target[i].hit()
                target[i].new_target(i)
                flag_seconds[i] = seconds
                missiles.remove(m)
            if seconds - flag_seconds[i] > 3:
                target[i].live = 1

    for b in balls:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        b.move(mouse_x, mouse_y)
        for i in range(2):
            if b.hittest(target[i]) and target[i].live:
                target[i].live = 0
                target[i].hit()
                target[i].new_target(i)
                flag_seconds[i] = seconds
            if seconds - flag_seconds[i] > 3:
                target[i].live = 1

        if (b.vx == 0) and (b.vy == 0):
            balls.remove(b)
    gun.power_up()

pygame.quit()
