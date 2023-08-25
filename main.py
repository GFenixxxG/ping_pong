from pygame import *

init()

W = 800
H = 500

back = (0, 255, 0)

window = display.set_mode((W, H))
display.set_icon(image.load("tenis_ball.png"))
display.set_caption("PING PONG")
window.fill(back)

class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.size_x = size_x
        self.size_y = size_y
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < H - self.size_y:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_PageUp] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed[K_PageDown] and self.rect.y < H - self.size_y:
            self.rect.y += self.speed


player_l = Player('racket.png', 10, W/3, 50, 150, 5)

#player_r = Player('racket.png', 480, W/3, 50, 150, 5)


finish = False
game = True


while game:
    time.delay(5)

    window.fill(back)

    player_l.reset()
    player_l.update_l() 

    #player_r.reset()
    #player_r.update_r()
    

    for e in event.get():
        if e.type == QUIT:
            game = False
            
    display.update()

