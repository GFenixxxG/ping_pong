#Підключення біблеотек
from pygame import *
#Ініацалізація всіх процесів
init()
#Розміри екрану
W = 800
H = 500
#Задній фон
back = (0, 255, 0)
#Екран
window = display.set_mode((W, H))
display.set_icon(image.load("tenis_ball.png"))
display.set_caption("PING PONG")
window.fill(back)
#Базовий класс для обєктів
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
    #Функція для відмальовування
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#Класс для гравця
class Player(GameSprite):
    #Функція для руху гравця L
    def update_l(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < H - self.size_y:
            self.rect.y += self.speed
    #Функція для руху гравця R
    def update_r(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < H - self.size_y:
            self.rect.y += self.speed

#Гравці
player_l = Player('racket.png', 10, W/3, 50, 150, 5)
player_r = Player('racket.png', 740, W/3, 50, 150, 5)
#Змінні для гри
finish = False
game = True
#Цикл гри
while game:
    time.delay(5)

    window.fill(back)

    player_l.reset()
    player_l.update_l() 

    player_r.reset()
    player_r.update_r()
    
    #Перевірка закриття гри
    for e in event.get():
        if e.type == QUIT:
            game = False
    #Оновлення екрану
    display.update()

