import pygame
import math
import random
import proxy
import iterator
import singleton
import strategy


pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman Game!')


LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)


RADIUS = 20
GAP = 15
letters = []
start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
start_y = 400
A = 65

for result in iterator.count_to_max:
    x = start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (result % 13))
    y = start_y + ((result // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + result), True])


hangman_status = 0
word = random.choice(proxy.words)
guessed = []


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


FPS = 60
clock = pygame.time.Clock()
run = True


class Drawing:

    @staticmethod
    def draw():
        win.fill(WHITE)
        text = TITLE_FONT.render('HANGMAN GAME', True, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width() / 2, 20))

        display_word = ''
        for letter in singleton.wrd:
            if letter in guessed:
                display_word += letter + ' '
            else:
                display_word += '_ '
        text = WORD_FONT.render(display_word, True, BLACK)
        win.blit(text, (400, 200))

        for _letter in letters:
            ex, why, let, vis = _letter
            if vis:
                pygame.draw.circle(win, BLACK, (ex, why), RADIUS, 3)
                text = LETTER_FONT.render(let, True, BLACK)
                win.blit(text, (ex - text.get_width() / 2, why - text.get_height() / 2))

        win.blit(strategy.strategy0[hangman_status], (150, 100))
        pygame.display.update()


class DisplayMessage:

    @staticmethod
    def display_message(message):
        pygame.time.delay(1000)
        win.fill(WHITE)
        text = WORD_FONT.render(message, True, BLACK)
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(3000)


class DrawAndDisplay:

    def __init__(self):
        self.drawing = Drawing()
        self.display1 = DisplayMessage()
        self.display2 = DisplayMessage()

    def start_draw(self):
        self.drawing.draw()

    def start_display1(self):
        self.display1.display_message('You Won!')

    def start_display2(self):
        self.display2.display_message('You Lost!')


draw_and_display = DrawAndDisplay()


while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in singleton.wrd:
                            hangman_status += 1

    draw_and_display.start_draw()

    won = True
    for letter in singleton.wrd:
        if letter not in guessed:
            won = False
            break

    if won:
        draw_and_display.start_display1()
        break

    if hangman_status == 6:
        draw_and_display.start_display2()
        break


pygame.quit()
