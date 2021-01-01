import pygame
from figures import FigureL

elem_size = 30
fieldx, fieldy = 20, 20
size = width, height = 500, 640
screen = pygame.display.set_mode(size)
screen.fill((128, 128, 128))
pygame.display.set_caption('Tetris')


clock = pygame.time.Clock()


def draw_square(screen):
    color = pygame.Color(60, 60, 60)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 40, hsv[3])
    pygame.draw.rect(screen, color, (4, 4, 492, 632), 0)

    pygame.draw.rect(screen, (0, 0, 0), (fieldx, fieldy, 300, 600), 0)

    font = pygame.font.Font(None, 30)
    text = font.render("Next figure", True, (155, 17, 30))
    screen.blit(text, (355, 44))

    pygame.draw.rect(screen, (0, 0, 0), (340, 100, 137, 115), 0)

    font = pygame.font.Font(None, 40)
    text = font.render("Score", True, (155, 17, 30))
    screen.blit(text, (370, 270))
    font = pygame.font.Font(None, 40)
    text = font.render("0", True, 'red')
    screen.blit(text, (400, 310))


class Figure:
    def __init__(self, f_class):
        self.fclass = f_class
        self.h, self.w = 4, 0

    def draw(self):
        per = self.fclass.get()
        for i in range(len(per)):
            for j in range(len(per)):
                if per[i][j] == 1:
                    pygame.draw.rect(screen, pygame.Color('red'),
                                     (j * 30 + self.h * 30 + fieldx, self.w * 30 + 30 * i + fieldy, 30, 30), 0)


if __name__ == '__main__':
    pygame.init()
    draw_square(screen)
    a = Figure(FigureL())
    a.draw()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
