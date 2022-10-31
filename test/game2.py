import pygame
from random import uniform as func

pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

bound = 5
c2s = 30
white = (255, 255, 255)
black = (0, 0, 0)
x, y = WIDTH // 2, HEIGHT // 2
radius = 10
velocity = 12
vx = velocity*func(-1, 1)
vy = velocity*func(-1, 1)

border_l = bound + radius
border_u = bound + radius
border_r = WIDTH - bound - radius
border_d = HEIGHT - bound - radius

height = 10
width = 50
xp = (WIDTH - width) // 2
yp = HEIGHT - height
vp = 10

def drawWindow():
    win.fill(black)
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))  # up
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))  # left
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))  # right
    pygame.draw.rect(win, (0, 255, 0), (xp, yp, width, height))  # paddle
    # pygame.draw.rect(win, white, (0, HEIGHT - bound, WIDTH, bound))  # down
    pygame.draw.circle(win, (0, 255, 0), (x, y), radius)
    pygame.display.update()


run = True

while run:
    clock.tick(c2s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < WIDTH - width - bound:
        xp += vp

    if x + vx < border_l or x + vx > border_r:
        vx = -vx
    if y + vy < border_u:
        vy = -vy
    if y + vy > border_d:
        # if xp <= x + vx <= xp + width:
        if x + vx >= xp and x + vx <= xp + width:
            vy = -vy
        else:
            run = False

    x += vx
    y += vy

    drawWindow()

pygame.quit()
