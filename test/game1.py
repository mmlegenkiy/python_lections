import pygame
import random

pygame.init()
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Cubes Game")

clock = pygame.time.Clock()

bound = 5
height = 10
width = 100
c2s = 30
white = (255, 255, 255)
radius = 10
velocity = 8
vp = 5
vx = velocity*random.uniform(-1, 1)
vy = velocity*random.uniform(-1, 1)

border_l = bound + radius
border_u = bound + radius
border_r = WIDTH - bound - radius
border_d = HEIGHT - bound - radius
x = random.randint(border_l + bound, border_r - bound)
y = random.randint(border_u + bound, border_d - bound)
xp = (WIDTH - width) // 2
yp = HEIGHT - height

def drawWindow():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))  # up
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))  # left
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))  # right
    pygame.draw.rect(win, white, (xp, yp, width, height))  # paddle
    pygame.draw.circle(win, white, (x, y), radius)
    pygame.display.update()


run = True

while run:
    clock.tick(c2s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > bound:
        xp -= vp
    if keys[pygame.K_RIGHT] and x < WIDTH - width - bound:
        xp += vp

    if x + vx < border_l or x + vx > border_r:
        vx = -vx
    if y + vy < border_u:
        vy = -vy
    if y + vy > border_d:
        if xp <= x + vx <= xp + width:
            vy = -vy
        else:
            run = False
    x += vx
    y += vy

    drawWindow()


pygame.quit()
