from pygame import *
from random import randint 

back = (200, 255, 255)
windows_width, windows_height = 600, 500
windows = display.set_mode((windows_width, windows_height))
display.set_caption("Pong")
windows.fill(back)

clock = time.Clock()
FPS = 60
gameLoop = True
finish = False
font.init()
font2 = font.Font(None,36)
win1 = font2.render("Вийграв гравець 1",True,(0,0,0))
win2 = font2.render("Вийграв гравець 2",True,(171,33,33))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()

        if  keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < windows_height - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()

        if  keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < windows_height - 80:
            self.rect.y += self.speed

racket1 = Player("racket.png", 30, 200, 25, 50, 3)
racket2 = Player("racket.png", 530, 200, 25, 50, 3)
ball = GameSprite('tenis_ball.png', 280, 200, 50, 50, 3)
ball_speed_x = 2
ball_speed_y = 2
speed_x = 3
speed_y = 3
a = randint(1,2)
b = randint(1,2)
while gameLoop:

    for e in event.get():
        if e.type == QUIT:
            gameLoop = False

    if finish != True:
        windows.fill(back)
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        ball.reset()
        if a == 1:
            ball.rect.x += ball_speed_x
        if a == 2:
            ball.rect.x -= ball_speed_x
        if b == 1:
            ball.rect.y += ball_speed_y
        if b == 2:
            ball.rect.y -= ball_speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball_speed_x *= -1
            ball_speed_y *= 1
        if ball.rect.y > windows_height or ball.rect.y < 0:
            ball_speed_y *= -1
        if ball.rect.x < 0:
            windows.blit(win1,(200, 200))
        if ball.rect.x > 600:
            windows.blit(win2, (200,200))
    display.update()
    clock.tick(FPS)

