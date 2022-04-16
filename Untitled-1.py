from pygame import *
 
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
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
player1 = Player1('l.png', 5, win_height - 80, 4)
player2 = Player2('l.png', 5, win_height - 80, 4)
ball = Player1('ОООО.png',9 ,win_height - 70, 4  )

speed_x=3
speed_y = 3
game = True
finish = False
clock = time.Clock()
FPS = 60
font.init()
font = font.Font(None, 70)
lose = font.render('YOU LOSE!', True, (180, 0, 0))
while game:
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.y < 0 or ball.rect.y > win_height:
        ball.rect.y *= -1

    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        player1.update()
        ball.update()
        player1.reset()
        ball.reset()
        player2.update()
        player2.reset()
        
    
    display.update()
    clock.tick(FPS)
 
