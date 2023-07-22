import pygame as pg
import sys

class Menu:

    def __init__(self):

        self.done, self.start, self.records, self.rules = False, False, False, False # булевы переменные, предназначенные для открытия определённого окна в будущем

        self.level = 1
        self.resolution = 900, 1025 # разрешение окна в пикселях
        self.screen = pg.display.set_mode(self.resolution, pg.SCALED)
        self.screen.fill(pg.Color(188, 204, 203))
        self.fps = 60 # количество кадров / выполнений цикла в секунду
        self.clock = pg.time.Clock()
        self.mouse = pg.mouse.get_pos() # позиция мыши
        self.font = pg.font.Font('source/Boxigen.otf', 65) # инициализаия шрифтов
        self.main_font = pg.font.Font('source/Boxigen.otf', 85)
        self.add_font = pg.font.Font('source/izis-one.ttf', 35)


    def render_menu(self): # функция для отрисовки главного окна меню
        self.screen.fill(pg.Color(188, 204, 203))

        tetris_text2 = self.main_font.render("TETRIS", True, pg.Color(0, 0, 0))
        tetris_text = self.main_font.render("TETRIS", True, pg.Color(1, 192, 182))
        tetris_rect = tetris_text.get_rect()
        tetris_rect.center = (self.resolution[0] / 2, 100)
        self.screen.blit(tetris_text2, (tetris_rect.x + 2, tetris_rect.y + 2))
        self.screen.blit(tetris_text, tetris_rect)

        '''отрисовка "кнопок" на экране'''
        start_game_text = self.font.render("START", True, pg.Color(74, 102, 47))
        start_game_rect = start_game_text.get_rect()
        start_game_rect.center = (self.resolution[0] / 2, 400)
        self.screen.blit(start_game_text, start_game_rect)

        records_text = self.font.render("RECORDS", True, pg.Color(74, 102, 47))
        records_rect = records_text.get_rect()
        records_rect.center = (self.resolution[0] / 2, 600)
        self.screen.blit(records_text, records_rect)

        rules_text = self.font.render("CONTROL", True, pg.Color(74, 102, 47))
        rules_rect = rules_text.get_rect()
        rules_rect.center = (self.resolution[0] / 2, 800)
        self.screen.blit(rules_text, rules_rect)
        ''''''

        '''если курсор мыши наведён на "кнопку", то меняем её цвет'''
        self.mouse = pg.mouse.get_pos()
        if start_game_rect.left <= self.mouse[0] <= start_game_rect.right and start_game_rect.top <= self.mouse[1] <= start_game_rect.bottom:
            start_game_text = self.font.render("START", True, pg.Color(142, 172, 80))
            self.screen.blit(start_game_text, start_game_rect)

        elif records_rect.left <= self.mouse[0] <= records_rect.right and records_rect.top <= self.mouse[1] <= records_rect.bottom:
            records_text = self.font.render("RECORDS", True, pg.Color(142, 172, 80))
            self.screen.blit(records_text, records_rect)

        elif rules_rect.left <= self.mouse[0] <= rules_rect.right and rules_rect.top <= self.mouse[1] <= rules_rect.bottom:
            rules_text = self.font.render("CONTROL", True, pg.Color(142, 172, 80))
            self.screen.blit(rules_text, rules_rect)
        ''''''

        for event in pg.event.get(): # элементы управления
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if start_game_rect.left <= self.mouse[0] <= start_game_rect.right and start_game_rect.top <= self.mouse[1] <= start_game_rect.bottom:
                    self.done = True

                elif records_rect.left <= self.mouse[0] <= records_rect.right and records_rect.top <= self.mouse[1] <= records_rect.bottom:
                    self.records = True

                elif rules_rect.left <= self.mouse[0] <= rules_rect.right and rules_rect.top <= self.mouse[1] <= rules_rect.bottom:
                    self.rules = True

        pg.display.flip()
        self.clock.tick(self.fps)

    def render_controls(self):
        self.screen.fill(pg.Color(188, 204, 203))

        tetris_text2 = self.main_font.render("TETRIS", True, pg.Color(0, 0, 0))
        tetris_text = self.main_font.render("TETRIS", True, pg.Color(1, 192, 182))
        tetris_rect = tetris_text.get_rect()
        tetris_rect.center = (self.resolution[0] / 2, 100)
        self.screen.blit(tetris_text2, (tetris_rect.x + 2, tetris_rect.y + 2))
        self.screen.blit(tetris_text, tetris_rect)

        y = 200
        f = open('source/controls.txt', 'r')
        for line in f.readlines():
            text = self.add_font.render(line, True, pg.Color(74, 102, 47))
            self.screen.blit(text, (100, y))
            y += 50
        f.close()

        ok_text = self.font.render("BACK", True, pg.Color(74, 102, 47))
        ok_rect = ok_text.get_rect()
        ok_rect.center = (self.resolution[0] / 2, 870)
        self.screen.blit(ok_text, ok_rect)

        start_game_text = self.font.render("START", True, pg.Color(74, 102, 47))
        start_game_rect = start_game_text.get_rect()
        start_game_rect.center = (self.resolution[0] / 2, 950)
        self.screen.blit(start_game_text, start_game_rect)

        if ok_rect.left <= self.mouse[0] <= ok_rect.right and ok_rect.top <= self.mouse[1] <= ok_rect.bottom:
            ok_text = self.font.render("BACK", True, pg.Color(142, 172, 80))
            self.screen.blit(ok_text, ok_rect)

        if start_game_rect.left <= self.mouse[0] <= start_game_rect.right and start_game_rect.top <= self.mouse[1] <= start_game_rect.bottom:
            start_game_text = self.font.render("START", True, pg.Color(142, 172, 80))
            self.screen.blit(start_game_text, start_game_rect)

        self.mouse = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if ok_rect.left <= self.mouse[0] <= ok_rect.right and ok_rect.top <= self.mouse[1] <= ok_rect.bottom:
                    self.rules = False
                elif start_game_rect.left <= self.mouse[0] <= start_game_rect.right and start_game_rect.top <= self.mouse[1] <= start_game_rect.bottom:
                    self.done = True
                    self.rules = False

        pg.display.flip()
        self.clock.tick(self.fps)

    def render_records(self):
        self.screen.fill(pg.Color(188, 204, 203))

        tetris_text2 = self.main_font.render("TETRIS", True, pg.Color(0,0,0))
        tetris_text = self.main_font.render("TETRIS", True, pg.Color(1, 192, 182))
        tetris_rect = tetris_text.get_rect()
        tetris_rect.center = (self.resolution[0] / 2, 100)
        self.screen.blit(tetris_text2, (tetris_rect.x+2, tetris_rect.y+2))
        self.screen.blit(tetris_text, tetris_rect)

        y = 250
        f = open('source/records.txt', 'r')
        for i in range(10):
            line = f.readline()
            if line:
                num = self.add_font.render(str(i+1)+'.', True, pg.Color(74, 102, 47))
                self.screen.blit(num, (100, y))
                points = self.add_font.render(line, True, pg.Color(74, 102, 47))
                self.screen.blit(points, (150, y))
                text = self.add_font.render('points', True, pg.Color(74, 102, 47))
                self.screen.blit(text, (250, y))
                y += 50
        f.close()

        back_text = self.font.render("BACK", True, pg.Color(74, 102, 47))
        back_rect = back_text.get_rect()
        back_rect.center = (self.resolution[0] / 2, 800)
        self.screen.blit(back_text, back_rect)

        if back_rect.left <= self.mouse[0] <= back_rect.right and back_rect.top <= self.mouse[1] <= back_rect.bottom:
            back_text = self.font.render("BACK", True, pg.Color(142, 172, 80))
            self.screen.blit(back_text, back_rect)

        self.mouse = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if back_rect.left <= self.mouse[0] <= back_rect.right and back_rect.top <= self.mouse[1] <= back_rect.bottom:
                    self.records = False

        pg.display.flip()
        self.clock.tick(self.fps)

    def render_level(self):
        self.screen.fill(pg.Color(188, 204, 203))

        tetris_text2 = self.main_font.render("TETRIS", True, pg.Color(0, 0, 0))
        tetris_text = self.main_font.render("TETRIS", True, pg.Color(1, 192, 182))
        tetris_rect = tetris_text.get_rect()
        tetris_rect.center = (self.resolution[0] / 2, 100)
        self.screen.blit(tetris_text2, (tetris_rect.x + 2, tetris_rect.y + 2))
        self.screen.blit(tetris_text, tetris_rect)

        easy_text = self.font.render("EASY", True, pg.Color(74, 102, 47))
        easy_rect = easy_text.get_rect()
        easy_rect.center = (self.resolution[0] / 2, 300)
        self.screen.blit(easy_text, easy_rect)

        medium_text = self.font.render("MEDIUM", True, pg.Color(74, 102, 47))
        medium_rect = medium_text.get_rect()
        medium_rect.center = (self.resolution[0] / 2, 500)
        self.screen.blit(medium_text, medium_rect)

        hard_text = self.font.render("HARD", True, pg.Color(74, 102, 47))
        hard_rect = hard_text.get_rect()
        hard_rect.center = (self.resolution[0] / 2, 700)
        self.screen.blit(hard_text, hard_rect)

        back_text = self.font.render("BACK", True, pg.Color(74, 102, 47))
        back_rect = back_text.get_rect()
        back_rect.center = (self.resolution[0] / 2, 900)
        self.screen.blit(back_text, back_rect)

        if back_rect.left <= self.mouse[0] <= back_rect.right and back_rect.top <= self.mouse[1] <= back_rect.bottom:
            back_text = self.font.render("BACK", True, pg.Color(142, 172, 80))
            self.screen.blit(back_text, back_rect)

        self.mouse = pg.mouse.get_pos()
        if easy_rect.left <= self.mouse[0] <= easy_rect.right and easy_rect.top <= self.mouse[1] <= easy_rect.bottom:
            easy_text = self.font.render("EASY", True, pg.Color(142, 172, 80))
            self.screen.blit(easy_text, easy_rect)

        elif medium_rect.left <= self.mouse[0] <= medium_rect.right and medium_rect.top <= self.mouse[1] <= medium_rect.bottom:
            medium_text = self.font.render("MEDIUM", True, pg.Color(142, 172, 80))
            self.screen.blit(medium_text, medium_rect)

        elif hard_rect.left <= self.mouse[0] <= hard_rect.right and hard_rect.top <= self.mouse[1] <= hard_rect.bottom:
            hard_text = self.font.render("HARD", True, pg.Color(142, 172, 80))
            self.screen.blit(hard_text, hard_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if easy_rect.left <= self.mouse[0] <= easy_rect.right and easy_rect.top <= self.mouse[1] <= easy_rect.bottom:
                    self.start = True
                    self.level = 1
                    self.done = False

                elif medium_rect.left <= self.mouse[0] <= medium_rect.right and medium_rect.top <= self.mouse[1] <= medium_rect.bottom:
                    self.start = True
                    self.level = 2
                    self.done = False

                elif hard_rect.left <= self.mouse[0] <= hard_rect.right and hard_rect.top <= self.mouse[1] <= hard_rect.bottom:
                    self.start = True
                    self.level = 3
                    self.done = False

                elif back_rect.left <= self.mouse[0] <= back_rect.right and back_rect.top <= self.mouse[1] <= back_rect.bottom:
                    self.done = False

        pg.display.flip()
        self.clock.tick(self.fps)