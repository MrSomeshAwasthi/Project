import pygame 
import random
colors = [(102, 157, 179),
          (227, 224, 132),
          (168, 156, 148),
          (255,  79,  88),
          (255, 187,  51),
          (153, 153, 255),
          (152, 255, 152)]
class Figure:
    x = 0
    y = 0
    shapes = [ [[2,6,10,14], [8,9,10,11]],
               [[4,5,9,10],[2,6,5,9]],
               [[5,6,8,9],[1,5,6,10]],
               [[1,2,5,9],[4,5,6,10],[1,5,9,8],[0,4,5,6]],
               [[1,2,6,10],[3,5,6,7],[2,6,10,11],[5,6,7,9]],
               [[1,4,5,6],[1,5,6,9],[4,5,6,9],[1,4,5,9]],
               [[5,6,9,10]]]

    def __init__(self, x, y):                      
        self.x = x
        self.y = y
        self.type=random.randint(0,len(self.shapes)-1)  
        self.color=random.randint(0,len(colors)-1)   
        self.rotation=0                                
    def image(self):
        return self.shapes [self.type] [self.rotation]
    def rotate(self):
        self.rotation=(self.rotation + 1) % len(self.shapes[self.type])
class Tetris:
    level = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    p = 100
    q = 60
    bs=20
    figure = None
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)
    def new_figure(self):
        self.figure=Figure(3, 0)
    def intersects(self):
        a=False    
        for i in range(4):
            for j in range(4):
                if i*4+j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        a=True
        return a
    def break_lines(self):     
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2
    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()
    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "game over"
    def go_side(self, t):
        old_x = self.figure.x
        self.figure.x += t
        if self.intersects():
            self.figure.x = old_x
    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation
pygame.init()
icon = pygame.image.load('icon.png') 
pygame.display.set_icon(icon)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Modern Tetris")
done = False
clock = pygame.time.Clock()
fps = 60
game = Tetris(20, 10)
counter = 0
pressing_down = False
while not done:
    if game.figure is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0
    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False
    screen.fill(WHITE)
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.p + game.bs* j, game.q + game.bs * i, game.bs, game.bs], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.p + game.bs* j + 1, game.q + game.bs* i + 1, game.bs- 2, game.bs - 1])
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                if i * 4 + j in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                     [game.p + game.bs * (j + game.figure.x) + 1,
                                      game.q + game.bs * (i + game.figure.y) + 1,
                                      game.bs - 2, game.bs - 2])
    font = pygame.font.SysFont('Ink Free', 25, True, False)
    font1 = pygame.font.SysFont('Ink Free', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))
    screen.blit(text, [0, 0])
    if game.state == "game over":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
