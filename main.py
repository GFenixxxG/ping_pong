#Підключення біблеотек
from pygame import *
#Ініацалізація всіх процесів
init()
#Розміри екрану
W = 800
H = 500
#
player_l_point = 0
player_r_point = 0
#
speed_x = 1
speed_y = 1
#Задній фон
back = (0, 255, 100)
#Екран
window = display.set_mode((W, H))
display.set_icon(image.load("tenis_ball.png"))
display.set_caption("PING PONG")
window.fill(back)
"""FONTS"""

#Ініціалізація шрифту
font.init()
#Шрифти
font = font.SysFont("Arial", 50)


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

ball = GameSprite('tenis_ball.png', 200, 200, 75, 75, 1)

#Змінні для гри
finish = False
game = True
#Цикл гри
while game:
    #Перевірка закриття гри
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill(back)

    point_l_txt = font.render(str(player_l_point), 1, (0, 0, 0))
    point_r_txt = font.render(str(player_r_point), 1, (0, 0, 0))

    window.blit(point_l_txt, (725, 25))
    window.blit(point_r_txt, (54, 25))

    if not finish:
        time.delay(5)

        player_l.reset()
        player_l.update_l() 

        player_r.reset()
        player_r.update_r()

        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
            
        if ball.rect.y < 0 or ball.rect.y > H - 75:    
            speed_y *= -1

        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1

        if ball.rect.x > W - 75:    
            player_l_point += 1
            finish == True
            ball.rect.x = 200
            ball.rect.y = 200

        if ball.rect.x < 0: 
            player_r_point += 1
            finish == True
            ball.rect.x = 200
            ball.rect.y = 200
        #Оновлення екрану
        display.update()

