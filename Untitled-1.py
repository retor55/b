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
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
class Player2(GameSprite):
def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
class boll (GameSprite):
    def update(self): 

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
player1 = Player1('hero.png', 5, win_height - 80, 4)
player2 = Player2('hero.png', 5, win_height - 80, 4)
ball = boll('',9 ,win_height - 70, 4  )
w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
game = True
finish = False
clock = time.Clock()
FPS = 60
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()
        player.reset()
        monster.reset()
        final.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
      #Ситуация "Проигрыш"
        if sprite.collide_rect(player1,player2, ball ) or sprite.collide_rect(player1,player2, w1) or sprite.collide_rect(player1, player2, w2)or sprite.collide_rect(player1, player2, w3):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
      #Ситуация "Выигрыш"
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()
    display.update()
    clock.tick(FPS)
 