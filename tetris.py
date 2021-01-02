import pygame
from figures import FigureL

elem_size = 30
fieldx, fieldy = 20, 20
size = width, height = 500, 640
screen = pygame.display.set_mode(size)
screen.fill((128, 128, 128))
pygame.display.set_caption('tetris')


def draw_square(screen):
    color = pygame.Color(60, 60, 60)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 40, hsv[3])
    pygame.draw.rect(screen, color, (4, 4, 492, 632), 0)
    pygame.draw.rect(screen, (110, 110, 110), (15, 15, 310, 610), 0)
    pygame.draw.rect(screen, (110, 110, 110), (336, 96, 145, 123), 0)
    pygame.draw.rect(screen, (0, 0, 0), (fieldx, fieldy, 300, 600), 0)

    font = pygame.font.Font(None, 30)
    text = font.render("Next figure", True, (155, 17, 30))
    screen.blit(text, (355, 44))

    pygame.draw.rect(screen, (0, 0, 0), (340, 100, 137, 115), 0)

    font = pygame.font.Font(None, 40)
    text = font.render("Score", True, (155, 17, 30))
    screen.blit(text, (373, 270))
    pygame.draw.rect(screen, (205, 205, 205), (340, 250, 140, 110), 3)

    font = pygame.font.Font(None, 40)
    text = font.render("0", True, 'red')
    screen.blit(text, (403, 310))


class Figure:
    def __init__(self, f_class):
        self.fclass = f_class
        self.h, self.w = 4, 0
        self.lasth, self.lastw = 4, 0
        self.lastfclass = self.fclass.get()

    def draw(self):
        per = self.lastfclass
        for i in range(len(per)):
            for j in range(len(per)):
                if per[i][j] == 1:
                    pygame.draw.rect(screen, pygame.Color('black'),
                                     (j * elem_size + self.lasth * elem_size + fieldx, self.lastw * elem_size + elem_size * i
                                      + fieldy, elem_size, elem_size), 0)
        per = self.fclass.get()
        for i in range(len(per)):
            for j in range(len(per)):
                if per[i][j] == 1:
                    pygame.draw.rect(screen, pygame.Color('red'),
                                     (j * elem_size + self.h * elem_size + fieldx, self.w * elem_size + elem_size * i
                                      + fieldy, elem_size, elem_size), 0)
        self.lastfclass = self.fclass.get()

    # def redraw(self):



if __name__ == '__main__':
    pygame.init()
    draw_square(screen)
    a = Figure(FigureL())
    a.draw()
    a.w = 1
    a.fclass.rotate()
    a.draw()
    # fps = 50
    # clock = pygame.time.Clock()
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_DOWN:
            #         Figure.redraw()
        # # формирование кадра
        # # ...
        # pygame.display.flip()  # смена кадра
        # # изменение игрового мира
        # # ...
        # # временная задержка
        # clock.tick(fps)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
