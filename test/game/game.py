import pygame

pygame.init()
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Cubes Game")

walkRight = [pygame.image.load('game/pictures/right_1.png'), pygame.image.load('game/pictures/right_2.png'),
             pygame.image.load('game/pictures/right_3.png'), pygame.image.load('game/pictures/right_4.png'),
             pygame.image.load('game/pictures/right_5.png'), pygame.image.load('game/pictures/right_6.png')]

walkLeft = [pygame.image.load('game/pictures/left_1.png'), pygame.image.load('game/pictures/left_2.png'),
            pygame.image.load('game/pictures/left_3.png'), pygame.image.load('game/pictures/left_4.png'),
            pygame.image.load('game/pictures/left_5.png'), pygame.image.load('game/pictures/left_6.png')]

bg = pygame.image.load('game/pictures/bg.jpg')
playerStand = pygame.image.load('game/pictures/idle.png')

clock = pygame.time.Clock()

x = 50
y = 410
width = 60
height = 71
speed = 5
bound = 5

isJump = False
g = 10
JumpCount = g

left = False
right = False
animCount = 0
lastmove = "right"

Nframes = 5
Ncadrs = 6
c2s = Nframes*Ncadrs


class Proj():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= c2s: # 30 = 6 cadrs * 5 frames
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    for bullet in bullets:
        bullet.draw(win)

    # win.fill((0, 0, 0))

    # pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()


run = True
bullets = []

while run:
    # pygame.time.delay(50)
    clock.tick(c2s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if 0 < bullet.x < WIDTH:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        facing = 1 if lastmove == "right" else -1
        if len(bullets) < 5:
            xb, yb = round(x + width // 2), round(y + height // 2)
            bullets.append(Proj(xb, yb, 5, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and x > bound:
        x -= speed
        left = True
        right = False
        lastmove = "left"
    elif keys[pygame.K_RIGHT] and x < WIDTH - width - bound:
        x += speed
        left = False
        right = True
        lastmove = "right"
    else:
        left = False
        right = False
        animCount = 0
    if not isJump:
        if keys[pygame.K_UP] and y > bound:
            y -= speed
        if keys[pygame.K_DOWN] and y < HEIGHT - height - bound:
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if JumpCount >= -g:
            if JumpCount < 0:
                y += (JumpCount ** 2) / 2
            else:
                y -= (JumpCount ** 2) / 2
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = g

    drawWindow()

pygame.quit()
