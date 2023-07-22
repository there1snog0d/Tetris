import pygame as pg
from Figures import Figure
import sys
from Menu import Menu

def main():
    icon = pg.image.load('source/images/icon.png') # задаём иконку окна
    pg.display.set_icon(icon)

    '''инициализируем библиотеку pygame, её модули для дисплея и текста'''
    pg.init()
    pg.display.init()
    pg.font.init()
    ''''''
    pg.display.set_caption('Tetris') # задаём заголовок окна

    score_arr = [0, 100, 300, 700, 1500]
    score = 0

    big_text = pg.font.Font('source/Boxigen.otf', 65)
    add_text = pg.font.Font('source/Boxigen.otf', 45)
    small_text = pg.font.Font('source/Boxigen.otf', 23)

    title = big_text.render('TETRIS', True, pg.Color(74, 102, 47))
    title2 = big_text.render('TETRIS', True, pg.Color(50, 69, 31))
    next_fig = add_text.render('NEXT FIGURE', True, pg.Color(74, 102, 47))
    next_fig2 = add_text.render('NEXT FIGURE', True,  pg.Color(50, 69, 31))
    score_text = add_text.render('SCORE', True, pg.Color(74, 102, 47))
    score_text2 = add_text.render('SCORE', True, pg.Color(50, 69, 31))
    top_record = add_text.render('TOP RECORD', True, pg.Color(74, 102, 47))
    top_record2 = add_text.render('TOP RECORD', True, pg.Color(50, 69, 31))

    music_off = pg.image.load('source/images/music_off.png')
    music_off = pg.transform.scale(music_off, (100, 50))
    music_on = pg.image.load('source/images/music_on.png')
    music_on = pg.transform.scale(music_on, (100, 50))
    music_rect = music_on.get_rect()
    music_rect.center = (735, 935)
    pg.mixer.music.load("source/music/main_theme.ogg")
    pg.mixer.music.set_volume(0)
    pg.mixer.music.play(-1)
    music = False

    fall_count, fall_limit, fall_limit_temp = 0, 48, 0
    fps = 60  # количество кадров в секунду

    tile = 45  # размер клетки
    cup_width, cup_height = 10, 20  # размер игрового окна в клетках

    game_resolution = cup_width * tile, cup_height * tile  # разрешение ирового окна в пикселях

    resolution = 900, 1025 # разрешение окна

    grid = [pg.Rect(x * tile, y * tile, tile, tile) for x in range(cup_width) for y in range(cup_height)]  # задаём сетку

    screen = pg.display.set_mode(resolution, pg.SCALED)
    game_screen = pg.Surface(game_resolution)

    clock = pg.time.Clock()
    pause = False

    f = Figure(game_screen, cup_width, cup_height, tile)
    menu = Menu()
    while True:

        if menu.records:
            menu.render_records()

        elif menu.rules:
            menu.render_controls()
            pause = False

        elif menu.done:
            menu.render_level()
            if menu.level == 1:
                fall_limit = 48
            elif menu.level == 2:
                fall_limit = 23
            else:
                fall_limit = 5

        elif menu.start:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        pause = False
                    elif event.key == pg.K_BACKSPACE:
                        if not music:
                            pg.mixer.music.set_volume(0.2)
                            music = not music
                        f = Figure(game_screen, cup_width, cup_height, tile)
                        pause = False
                    elif event.key == pg.K_ESCAPE:
                        menu.start = False
                        pause = True

                if event.type == pg.QUIT:
                    sys.exit()

            while not pause:
                mouse = pg.mouse.get_pos()

                screen.fill(pg.Color(188, 204, 203))
                screen.blit(game_screen, (tile + 20, tile + 20))
                game_screen.fill(pg.Color(80, 80, 80))
                dx = 0

                # элементы управления
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        sys.exit()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_LEFT:
                            dx = -1
                        elif event.key == pg.K_RIGHT:
                            dx = 1
                        elif event.key == pg.K_DOWN:
                            fall_limit_temp = fall_limit
                            fall_limit = 1
                        elif event.key == pg.K_UP:
                            f.rotate()
                        elif event.key == pg.K_SPACE:
                            if music:
                                pg.mixer.music.set_volume(0)
                                music = not music
                            pause = True
                        elif event.key == pg.K_ESCAPE:
                            score = 0
                            f = Figure(game_screen, cup_width, cup_height, tile)
                            menu.start = False
                            pause = True
                        elif event.key == pg.K_BACKSPACE:
                            f = Figure(game_screen, cup_width, cup_height, tile)

                    elif event.type == pg.KEYUP:
                        if event.key == pg.K_DOWN:
                            fall_limit = fall_limit_temp

                    elif event.type == pg.MOUSEBUTTONDOWN:
                        if music_rect.left <= mouse[0] <= music_rect.right and music_rect.top <= mouse[1] <= music_rect.bottom:
                            if not music:
                                pg.mixer.music.set_volume(0.2)
                                screen.blit(music_on, music_rect)
                            else:
                                pg.mixer.music.set_volume(0)
                                screen.blit(music_off, music_rect)
                            music = not music

                for rect in grid:
                    pg.draw.rect(game_screen, pg.Color(55, 55, 55), rect, 1)  # рисуем сетку на игровом поле

                for y in range(65, 1005, tile):  # рисуем оформление вокруг игрового поля
                    pg.draw.rect(screen, pg.Color(74, 102, 47), (20, y, tile, tile))
                    pg.draw.rect(screen, pg.Color(74, 102, 47), (515, y, tile, tile))

                    pg.draw.line(screen, pg.Color(142, 172, 80), [21, y], [21, y + 43], 5)
                    pg.draw.line(screen, pg.Color(142, 172, 80), [21, y + 2], [58, y + 2], 5)
                    pg.draw.line(screen, pg.Color(142, 172, 80), [517, y], [517, y + 38], 5)
                    pg.draw.line(screen, pg.Color(142, 172, 80), [517, y + 2], [555, y + 2], 5)

                    pg.draw.line(screen, pg.Color(50, 69, 31), [20, y - 3], [62, y - 3], 5)
                    pg.draw.line(screen, pg.Color(50, 69, 31), [62, y - 4], [62, y + 40], 5)
                    pg.draw.line(screen, pg.Color(50, 69, 31), [514, y - 3], [557, y - 3], 5)
                    pg.draw.line(screen, pg.Color(50, 69, 31), [557, y - 4], [557, y + 42], 5)

                for x in range(20, 540, tile):  # рисуем оформление вокруг игрового поля
                    pg.draw.rect(screen, pg.Color(74, 102, 47), (x, 20, tile, tile))
                    pg.draw.rect(screen, pg.Color(74, 102, 47), (x, 965, tile, tile))

                    pg.draw.line(screen, pg.Color(142, 172, 80), [x + 2, 22], [x + 2, 58], 5)
                    pg.draw.line(screen, pg.Color(142, 172, 80), [x, 22], [x + 38, 22], 5)
                    pg.draw.line(screen, pg.Color(142, 172, 80), [x + 2, 967], [x + 2, 1003], 5)
                    pg.draw.line(screen, pg.Color(142, 172, 80), [x, 967], [x + 38, 967], 5)

                    pg.draw.line(screen, pg.Color(50, 69, 31), [x, 62], [x + 44, 62], 5)
                    pg.draw.line(screen, pg.Color(50, 69, 31), [x + 42, 20], [x + 42, 63], 5)
                    pg.draw.line(screen, pg.Color(50, 69, 31), [x, 1007], [x + 44, 1007], 5)
                    pg.draw.line(screen, pg.Color(50, 69, 31), [x + 42, 965], [x + 42, 1007], 5)

                f.draw_figure()
                f.draw_next_figure(screen)
                f.move_x(dx)

                fall_count += 1
                if fall_count >= fall_limit:
                    fall_count = 0
                    f.move_y()

                f.draw_bottom()
                score_temp = score
                score += score_arr[f.delete_line()] * menu.level
                if score - score_temp:
                    if fall_limit > 1:
                        fall_limit -= 1
                    else:
                        fall_limit = 1

                screen.blit(title2, (638, 20))
                screen.blit(title, (635, 19))

                screen.blit(next_fig2, (607, 151))
                screen.blit(next_fig, (605, 150))

                screen.blit(score_text2, (677, 451))
                screen.blit(score_text, (675, 450))

                screen.blit(top_record2, (607, 701))
                screen.blit(top_record, (605, 700))

                score_points = add_text.render(str(score), True, pg.Color(74, 102, 47))

                score_text_rect = score_points.get_rect()
                score_text_rect.center = (735, 520)
                screen.blit(score_points, score_text_rect)

                with open('source/records.txt', 'r') as file:
                    high_score_text = add_text.render(file.read().split('\n')[0], True, pg.Color(74, 102, 47))
                high_score_rect = high_score_text.get_rect()
                high_score_rect.center = (735, 775)
                screen.blit(high_score_text, high_score_rect)

                if not music:
                    screen.blit(music_off, music_rect)
                else:
                    screen.blit(music_on, music_rect)

                if f.game_over():
                    music = False
                    pg.mixer.music.set_volume(0)
                    pause = f.game_over()
                    game_over_text = big_text.render("GAME OVER", True, pg.Color(240, 1, 2))
                    game_over_rect = game_over_text.get_rect()
                    game_over_rect.center = (cup_width / 2 * tile + tile + 20, resolution[1] / 2)
                    screen.blit(game_over_text, game_over_rect)

                    restart_text = small_text.render("press BACKSPACE to restart", True, pg.Color(240, 1, 2))
                    screen.blit(restart_text, (132, 545))
                    fall_count, fall_limit = 0, 48

                    with open('source/records.txt', 'r') as original:
                        temp = original.read()
                    temp += '\n' + str(score)
                    record = ""
                    temp_list = []
                    for line in temp.split('\n'):
                        if line != '':
                            temp_list.append(int(line))
                    temp_list.sort(reverse=True)
                    temp_list = temp_list[:10]
                    for line in temp_list:
                        record += str(line) + '\n'

                    with open('source/records.txt', 'w+') as modified:
                        modified.write(record)

                    score = 0

                pg.display.flip()
                clock.tick(fps)

        else:
            menu.render_menu()
            pause = False

if __name__ == '__main__':
    main()