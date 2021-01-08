import pygame
from random import *
from figures import *

elem_size = 30
fieldx, fieldy = 20, 20
size = width, height = 500, 640
screen = pygame.display.set_mode(size)
screen.fill((128, 128, 128))
pygame.display.set_caption('tetris')
clock = pygame.time.Clock()
FPS = 50


def load_image(name, color_key=None):
    fullname = name
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


class Figure:
    def __init__(self, f_class):
        self.fclass = f_class
        self.h, self.w = 4, 0
        self.lasth, self.lastw = 4, 0
        self.lastfclass = self.fclass.get()
        self.color = choice(['red', 'blue', 'green', 'yellow'])

    def draw_n_f(self):
        e_s = 20
        h = 19
        w = 6
        pygame.draw.rect(screen, pygame.Color('black'), (340, 100, 137, 115), 0)
        per = self.fclass.get()
        for i in range(len(per)):
            for j in range(len(per)):
                if per[i][j] == 1:
                    pygame.draw.rect(screen, pygame.Color(self.color),
                                     (j * e_s + h * e_s, w * e_s + e_s * i, e_s, e_s), 0)
                    pygame.draw.rect(screen, pygame.Color('black'),
                                     (j * e_s + h * e_s, w * e_s + e_s * i, e_s, e_s), 1)

    def draw(self):
        per = self.lastfclass
        for i in range(len(per)):
            for j in range(len(per)):
                if per[i][j] == 1:
                    pygame.draw.rect(screen, pygame.Color('black'),
                                     (j * elem_size + self.lasth * elem_size + fieldx, self.lastw * elem_size +
                                      elem_size * i + fieldy, elem_size, elem_size), 0)
        per = self.fclass.get()
        for i in range(len(per)):
            for j in range(len(per)):
                if per[i][j] == 1:
                    pygame.draw.rect(screen, pygame.Color(self.color),
                                     (j * elem_size + self.h * elem_size + fieldx, self.w * elem_size + elem_size * i
                                      + fieldy, elem_size, elem_size), 0)
                    pygame.draw.rect(screen, pygame.Color('black'),
                                     (j * elem_size + self.h * elem_size + fieldx, self.w * elem_size + elem_size * i
                                      + fieldy, elem_size, elem_size), 1)
        self.lasth, self.lastw = self.h, self.w
        self.lastfclass = self.fclass.get()

    def check_element(self, content, elx, ely):
        if elx < 0 or elx > 9 or ely < 0 or ely > 19:
            return False
        if content[ely][elx] != 0:
            return False
        return True

    def move_left(self, content):
        per = self.fclass.get()
        for i in range(len(per)):
            for j in range(len(per)):
                if per[i][j] == 1:
                    if not self.check_element(content, self.h + j - 1, self.w + i):
                        return
        self.h -= 1

    def move_right(self, content):
        per = self.fclass.get()
        for i in range(len(per)):
            for j in range(len(per)):
                if per[i][j] == 1:
                    if not self.check_element(content, self.h + 1 + j, self.w + i):
                        return
        self.h += 1

    def move_down(self, content):
        per = self.fclass.get()
        for i in range(len(per)):
            for j in range(len(per)):
                if per[i][j] == 1:
                    if not self.check_element(content, self.h + j, self.w + 1 + i):
                        return False
        self.w += 1
        return True

    def rotate(self, content):
        per = self.fclass.get_rotated()
        for i in range(len(per)):
            for j in range(len(per)):
                if per[i][j] == 1:
                    if not self.check_element(content, self.h + j, self.w + i):
                        return
        self.fclass.rotate()

    def checkSpawn(self, content):
        per = self.fclass.get()
        for i in range(len(per)):
            for j in range(len(per)):
                if per[i][j] == 1:
                    if not self.check_element(content, self.h + j, self.w + i):
                        return False
        return True


class Field:
    def __init__(self):
        self.figurestypes = (FigureL(), FigureJ(), FigureT(), FigureZ(), FigureS(), FigureO(), FigureI())
        self.score_counter = 0
        self.content = list([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

    def draw_window(self, screen):
        self.color = pygame.Color(60, 60, 60)
        hsv = self.color.hsva
        self.color.hsva = (hsv[0], hsv[1], hsv[2] + 40, hsv[3])
        pygame.draw.rect(screen, self.color, (4, 4, 492, 632), 0)
        pygame.draw.rect(screen, (110, 110, 110), (15, 15, 310, 610), 0)
        pygame.draw.rect(screen, (110, 110, 110), (336, 96, 145, 123), 0)

        font = pygame.font.Font(None, 30)
        text = font.render("Next figure", True, (155, 17, 30))
        screen.blit(text, (355, 44))

        pygame.draw.rect(screen, (0, 0, 0), (340, 100, 137, 115), 0)

        font = pygame.font.Font(None, 40)
        text = font.render("Score", True, (155, 17, 30))
        screen.blit(text, (373, 270))
        pygame.draw.rect(screen, (205, 205, 205), (340, 250, 140, 110), 3)

        font1 = pygame.font.Font(None, 40)
        score = str(self.score_counter)
        self.score_text = font1.render(score, True, 'red')
        screen.blit(self.score_text, (403, 310))
        self.draw_field(screen)
        pygame.display.flip()

    def draw_field(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (fieldx, fieldy, 300, 600), 0)
        for i in range(len(self.content)):
            for j in range(len(self.content[0])):
                if self.content[i][j] != 0:
                    pygame.draw.rect(screen, self.content[i][j],
                                     (j * elem_size + fieldx, elem_size * i + fieldy, elem_size, elem_size), 0)
                    pygame.draw.rect(screen, pygame.Color('black'),
                                     (j * elem_size + fieldx, elem_size * i + fieldy, elem_size, elem_size), 1)
        pygame.display.flip()

    def delete_rows(self):
        lcontent = []
        needdraw = False
        for i in range(len(self.content)):
            found0 = False
            for j in self.content[i]:
                if j == 0:
                    found0 = True
                    break

            if found0:
                lcontent.append(self.content[i])
            else:
                needdraw = True
                lcontent = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] + lcontent
                self.score_counter += 100
                pygame.draw.rect(screen, self.color, (345, 300, 130, 35), 0)

                font1 = pygame.font.Font(None, 40)
                score = str(self.score_counter)
                self.score_text = font1.render(score, True, 'red')
                self.place = self.score_text.get_rect(center=(410, 320))
                screen.blit(self.score_text, self.place)
                pygame.display.flip()
        self.content = lcontent
        if needdraw:
            self.draw_field(screen)

    def mainloop(self):
        running = True
        MYEVENTTYPE = pygame.USEREVENT + 1
        pygame.time.set_timer(MYEVENTTYPE, 600)
        f = Figure(choice(self.figurestypes))
        new_f = Figure(choice(self.figurestypes))

        f.draw()
        new_f.draw_n_f()
        while running:
            f.fclass.current_version = 0
            if not f.checkSpawn(self.content):
                break
            f.draw()
            pygame.display.flip()
            next_figure = False
            while not next_figure:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            f.rotate(self.content)
                        elif event.key == pygame.K_DOWN:
                            if not f.move_down(self.content):
                                next_figure = True
                                self.store_figure(f)
                        elif event.key == pygame.K_LEFT:
                            f.move_left(self.content)
                        elif event.key == pygame.K_RIGHT:
                            f.move_right(self.content)
                        elif event.key == pygame.K_SPACE:
                            while f.move_down(self.content):
                                pass
                            next_figure = True
                            self.store_figure(f)
                        elif event.key == pygame.K_ESCAPE:
                            start_screen()
                            running = False
                            field = Field()
                            field.draw_window(screen)
                            field.mainloop()
                    elif event.type == MYEVENTTYPE:
                        if not f.move_down(self.content):
                            next_figure = True
                            self.store_figure(f)
                f.draw()
                self.delete_rows()
                pygame.display.flip()

            f = new_f

            new_f = Figure(choice(self.figurestypes))
            new_f.draw_n_f()

    def store_figure(self, f):
        per = f.fclass.get()
        for i in range(len(per)):
            for j in range(len(per)):
                if per[i][j] == 1:
                    self.content[i + f.w][j + f.h] = f.color
        new_f = Figure(choice(self.figurestypes))
        new_f.draw_n_f()


def start_screen():
    fon = pygame.transform.scale(load_image('fon.png'), (492, 631))
    screen.blit(fon, (4, 5))
    font = pygame.font.Font(None, 70)
    text = font.render("TETRIS", True, (155, 17, 30))
    screen.blit(text, (160, 64))

    font = pygame.font.Font(None, 35)
    text = font.render("> press any key to start <", True, (155, 17, 30))
    screen.blit(text, (110, 544))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def play_again(score_counter):
    intro_text = "Would you like to play again?"
    sc_c = 'Final score: ' + str(score_counter)
    fon = pygame.transform.scale(load_image('final_fon.png'), (492, 631))
    screen.blit(fon, (4, 5))

    font = pygame.font.Font(None, 30)
    text = font.render(sc_c, True, (175, 17, 30))
    screen.blit(text, (180, 384))

    font = pygame.font.Font(None, 40)
    text = font.render(intro_text, True, (80, 90, 255))
    screen.blit(text, (60, 460))

    font = pygame.font.Font(None, 60)
    text = font.render('yes', True, (155, 0, 0))
    screen.blit(text, (110, 500))
    font = pygame.font.Font(None, 60)
    text = font.render('no', True, (0, 155, 0))
    screen.blit(text, (330, 500))

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pos()[0] >= 80) and (pygame.mouse.get_pos()[1] >= 490)\
                        and (pygame.mouse.get_pos()[0] <= 160) and (pygame.mouse.get_pos()[1] <= 540):
                    return True
                elif (pygame.mouse.get_pos()[0] >= 300) and (pygame.mouse.get_pos()[1] >= 490)\
                        and (pygame.mouse.get_pos()[0] <= 380) and (pygame.mouse.get_pos()[1] <= 540):
                    return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_RETURN:
                    return True
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    pygame.key.set_repeat(270)
    checker = True
    while checker:
        start_screen()
        field = Field()
        field.draw_window(screen)
        field.mainloop()
        if not play_again(field.score_counter):
            break
    pygame.quit()
