import pygame as pg
import random as r
from copy import deepcopy

class Figure:

    def __init__(self, screen, width, height, tile):
        self.move_sound = pg.mixer.Sound('source/music/move.ogg')
        self.move_sound.set_volume(0.2)
        self.fall_sound = pg.mixer.Sound('source/music/fall.ogg')
        self.rotate_sound = pg.mixer.Sound('source/music/rotate.ogg')
        self.rotate_sound.set_volume(0.2)
        self.game_over_music = pg.mixer.Sound("source/music/game_over.ogg")

        self.s = screen
        self.t = tile
        self.w = width
        self.h = height
        figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
                       [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                       [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                       [(0, 0), (-1, 0), (0, 1), (-1, -1)],
                       [(0, 0), (0, -1), (0, 1), (-1, -1)],
                       [(0, 0), (0, -1), (0, 1), (1, -1)],
                       [(0, 0), (0, -1), (0, 1), (-1, 0)]]

        self.figures = [[pg.Rect(x + self.w // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
        self.figure_rect = pg.Rect(0, 0, self.t - 2, self.t - 2)
        self.bottom = [[0 for i in range(self.w)] for j in range(self.h)]

        self.colors = [pg.Color(1, 240, 241),
                       pg.Color(241, 227, 16),
                       pg.Color(240, 1, 2),
                       pg.Color(0, 239, 2),
                       pg.Color(239, 130, 1),
                       pg.Color(1, 1, 240),
                       pg.Color(159, 1, 241)]

        self.light_colors = [pg.Color(171, 252, 254),
                             pg.Color(250, 251, 205),
                             pg.Color(252, 88, 91),
                             pg.Color(170, 255, 173),
                             pg.Color(252, 176, 108),
                             pg.Color(62, 106, 243),
                             pg.Color(187, 89, 254)]

        self.shadow_colors =[pg.Color(1, 192, 182),
                             pg.Color(244, 192, 5),
                             pg.Color(163, 4, 1),
                             pg.Color(5, 164, 1),
                             pg.Color(210, 96, 25),
                             pg.Color(3, 4, 152),
                             pg.Color(113, 0, 165)]

        num = r.randint(0, 6)
        self.color = self.colors[num]
        self.light_color = self.light_colors[num]
        self.shadow_color = self.shadow_colors[num]
        self.figure = deepcopy(self.figures[num])

        self.next_color = pg.Color(0, 0, 0)
        self.next_light_color = pg.Color(0, 0, 0)
        self.next_shadow_color = pg.Color(0, 0, 0)
        self.next_figure = deepcopy(self.figures[0])
        self.next_figure_rect = pg.Rect(0, 0, self.t-2, self.t-2)

        self.new_figure()

        self.last_line = self.h - 1

    def new_figure(self):
        next_num = r.randint(0, 6)
        self.next_color = self.colors[next_num]
        self.next_light_color = self.light_colors[next_num]
        self.next_shadow_color = self.shadow_colors[next_num]
        self.next_figure = deepcopy(self.figures[next_num])


    def move_x(self, dx):
        figure_temp = deepcopy(self.figure)
        for i in range(4):
            self.figure[i].x += dx
            if not self.borders():
                self.figure = deepcopy(figure_temp)
                break

    def move_y(self):
        pg.mixer.Channel(0).play(self.move_sound)
        figure_temp = deepcopy(self.figure)
        for i in range(4):
            self.figure[i].y += 1
            if not self.borders():
                for i in range(4):
                    self.bottom[figure_temp[i].y][figure_temp[i].x] = self.color
                pg.mixer.Channel(1).play(self.fall_sound)
                self.figure = deepcopy(self.next_figure)
                self.color = self.next_color
                self.light_color = self.next_light_color
                self.shadow_color = self.next_shadow_color

                while self.figure == self.next_figure:
                    self.new_figure()
                break

    def rotate(self):
        if  not self.color == pg.Color(241, 227, 16):
            pg.mixer.Channel(2).play(self.rotate_sound)
            center = self.figure[0]
            figure_temp = deepcopy(self.figure)
            for i in range(4):
                dx = self.figure[i].y - center.y
                dy = self.figure[i].x - center.x
                self.figure[i].x = center.x - dx
                self.figure[i].y = center.y + dy
                if not self.borders():
                    self.figure = deepcopy(figure_temp)
                    break

    def borders(self):
        for i in range(4):
            if self.figure[i].x < 0 or self.figure[i].x > self.w - 1:
                return False
            elif self.figure[i].y > self.h - 1 or self.bottom[self.figure[i].y][self.figure[i].x]:
                return False
        return True

    def draw_figure(self):
        for i in range(4):
            self.figure_rect.x = self.figure[i].x * self.t
            self.figure_rect.y = self.figure[i].y * self.t
            pg.draw.rect(self.s, self.color, self.figure_rect)

            pg.draw.line(self.s, self.light_color,
                         [self.figure_rect.x + 2, self.figure_rect.y + 2],
                         [self.figure_rect.x + 2, self.figure_rect.y + 38], 5)
            pg.draw.line(self.s, self.light_color,
                         [self.figure_rect.x, self.figure_rect.y + 2],
                         [self.figure_rect.x + 38, self.figure_rect.y + 2], 5)
            pg.draw.line(self.s, self.shadow_color,
                         [self.figure_rect.x, self.figure_rect.y + 40],
                         [self.figure_rect.x + 43, self.figure_rect.y + 40], 5)
            pg.draw.line(self.s, self.shadow_color,
                         [self.figure_rect.x + 42, self.figure_rect.y],
                         [self.figure_rect.x + 42, self.figure_rect.y + 42], 5)

    def draw_bottom(self):
        for y, raw in enumerate(self.bottom):
            for x, color in enumerate(raw):
                if color:
                    self.figure_rect.x = x * self.t
                    self.figure_rect.y = y * self.t
                    pg.draw.rect(self.s, pg.Color(122, 122, 122), self.figure_rect)

                    pg.draw.line(self.s, pg.Color(175, 175, 175),
                                 [self.figure_rect.x + 2, self.figure_rect.y + 2],
                                 [self.figure_rect.x + 2, self.figure_rect.y + 38], 5)
                    pg.draw.line(self.s, pg.Color(175, 175, 175),
                                 [self.figure_rect.x, self.figure_rect.y + 2],
                                 [self.figure_rect.x + 38, self.figure_rect.y + 2], 5)
                    pg.draw.line(self.s, pg.Color(80, 80, 80),
                                 [self.figure_rect.x, self.figure_rect.y + 40],
                                 [self.figure_rect.x + 43, self.figure_rect.y + 40], 5)
                    pg.draw.line(self.s, pg.Color(80, 80, 80),
                                 [self.figure_rect.x + 42, self.figure_rect.y],
                                 [self.figure_rect.x + 42, self.figure_rect.y + 42], 5)
    def draw_next_figure(self, screen):
        for i in range(4):
            self.next_figure_rect.x = self.next_figure[i].x * self.t + 503
            self.next_figure_rect.y = self.next_figure[i].y * self.t + 250
            pg.draw.rect(screen, self.next_color, self.next_figure_rect)

            pg.draw.line(screen, self.next_light_color,
                         [self.next_figure_rect.x + 2, self.next_figure_rect.y + 2],
                         [self.next_figure_rect.x + 2, self.next_figure_rect.y + 38], 5)
            pg.draw.line(screen, self.next_light_color,
                         [self.next_figure_rect.x, self.next_figure_rect.y + 2],
                         [self.next_figure_rect.x + 38, self.next_figure_rect.y + 2], 5)
            pg.draw.line(screen, self.next_shadow_color,
                         [self.next_figure_rect.x, self.next_figure_rect.y + 40],
                         [self.next_figure_rect.x + 43, self.next_figure_rect.y + 40], 5)
            pg.draw.line(screen, self.next_shadow_color,
                         [self.next_figure_rect.x + 42, self.next_figure_rect.y],
                         [self.next_figure_rect.x + 42, self.next_figure_rect.y + 42], 5)
    def delete_line(self):
        lines = 0
        self.last_line = self.h - 1
        for row in range(self.h - 1, -1, -1):
            count = 0
            for i in range(self.w):
                if self.bottom[row][i]:
                    count += 1
                self.bottom[self.last_line][i] = self.bottom[row][i]
            if count < self.w:
                self.last_line -= 1
            else:
                lines += 1
        return lines

    def game_over(self):
        for i in range(self.w):
            if self.bottom[0][i]:
                pg.mixer.Channel(3).play(self.game_over_music)
                return True