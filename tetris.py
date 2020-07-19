import pygame
import random

# use for initializing Py game which we have imported
pygame.init()
# use to give heading to game
pygame.display.set_caption('Modern Tetris')
# use to load icon
icon = pygame.image.load('icon.png')
# use to display icon
pygame.display.set_icon(icon)
# screen size (sw = screen width, sh = screen height)
sw = 800
sh = 700
# use to give size to window
screen = pygame.display.set_mode((sw, sh))
# box size (actual play width = pw, play height = ph)
pw = 300
ph = 600
# starting point of board (top left x= tlx, top left Y= tly)
tlx = (sw - pw) // 2
tly = (sh - ph)
# size of single block
bs=30
# shapes
S = [['.....',
      '..00.',
      '.00..',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '...0.',
      '..00.',
      '..0..',
      '.....']]
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
L = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '.00..',
      '.0...',
      '.0...',
      '.....']]
J = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '...0.',
      '...0.',
      '.....']]
T = [['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '...0.',
      '..00.',
      '...0.',
      '.....'],
     ['.....',
      '.....',
      '..0..',
      '.000.',
      '.....'],
     ['.....',
      '.0...',
      '.00..',
      '.0...',
      '.....']]
# colouring the letter
shapes = [S, O, Z, I, L, J, T]
shape_colour = [(102, 157, 179), (240, 246, 247), (168, 156, 148), (255, 79, 88), (255, 187, 51), (153, 153, 255),
                (152, 255, 152)]


class obj(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.colour = shape_colour[shapes.index(shape)]
        self.rotation = 0

    def create_grid(self, locked_pos={}):
        grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in locked_pos:
                    c = locked_pos[(i, j)]
                    grid[i][j] = c
        return grid

    def get_shape (self):
        return (5, 0, random.choice(shapes))

    def draw_window (self, surface, grid):
        surface.fill(0, 0, 0)
        pygame.font.init()
        font = pygame.font.SysFont('Ink Free', 60)
        label = font.render('TETRIS', 1, (255, 255, 255))
        surface.blit(label, (tlx + pw / 2)-(label.get_width()/2), 30)

    def draw_grid (self, surface, grid):
        for i in range(len(grid)):
            pygame.draw.line(surface, (192, 192, 192), (tlx, tly + i * bs), (tlx + pw, tly + i * bs))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (192, 192, 192), (tlx + j * bs, tly), (tlx + j * bs, tly + ph))

    def draw_text_middle(self, surface, text, size, color):
        font = pygame.font.SysFont('Ink Free', size, bold=True)
        label=font.render(text, 1, color)
        surface.blit(label, (tlx + pw / 2)-label.get_width)

# game loop
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0, 127, 225))
    pygame.display.update()