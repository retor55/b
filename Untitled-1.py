from pygame import *
 
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
   def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s]  and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("g.jpg"), (win_width, win_height))
player1 = Player1('l.png', 630, win_height -80, 100, 100, 10) #повернуть и обрезать
player2 = Player2('l.png', 10, win_height - 149, 100, 100, 10)
ball = Player1('ОООО.png', win_width/2, win_height/2, 200, 200, 4)
back = (200, 255 , 255)
game = True
finish = False
clock = time.Clock()
FPS = 60
font.init()
font = font.Font(None, 70)
lose1 = font.render('Player1 LOSE!', True, (180, 0, 0))
lose2 = font.render('Player2 LOSE!', True, (180, 0, 0))
speed_y = 2
speed_x = 2
while game:
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        if ball.rect.y < 0 or ball.rect.y > win_height:
            ball.rect.y *= -1
        if sprite.collide_rect(player1 , ball) or sprite.collide_rect(player2 , ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-100 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0 :
            finish = True
            window.blit(lose1, (200,200))
            game_over = True 
        if ball.rect.x < 0 :
            finish = True
            window.blit(lose2, (200,200))
            game_over = True 

        window.blit(background,(0, 0))
        player1.update()
        ball.update()
        player1.reset()
        ball.reset()

        player2.update()
        player2.reset()
        
    
    display.update()
    clock.tick(FPS)
