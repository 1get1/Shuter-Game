#Создай собственный Шутер!
 
from pygame import *
from random import *
 
FPS = 60
lost = 0
clock = time.Clock()
 
class GameSprite(sprite.Sprite):
    def __init__(self, p_image, width, height, x, y, speed):
        super().__init__()
        #self.image = transform.scale(image.load(player_image), (65, 65))
        self.image = transform.scale(image.load(p_image),(width , height))
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
 
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
 
    def move_rocket(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', 15,20, self.rect.centerx,self.rect.top,5)
        bullets.add(bullet)
 
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.x = randint(20, 610)
            self.rect.y = 0
            lost = lost+1
        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        for i in sprites_list:
            ufo7 = GameSprite('ufo.png', 65,65, randint(20,610), 0, randint(1,1))
            monsters.add(ufo7)
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.x = randint(20, 610)
            self.rect.y = 0
            lost = lost+1


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
 
font.init()
font1 = font.Font(None, 36)
#miss_enemy = font1.render('Miss' + str(lost), 1 , (255,255,255))
 
 
window = display.set_mode((700,500))
display.set_caption('shooter')
background = transform.scale(image.load('galaxy.jpg'),(700,500))
rocket = GameSprite('rocket.png',65,100,325,390,5)
ufo1 = GameSprite('ufo.png', 65,65, randint(20,610), 0, randint(1,1))
ufo2 = GameSprite('ufo.png', 65,65, randint(20,610), 0, randint(1,1))
ufo3 = GameSprite('ufo.png', 65,65, randint(20,610), 0, randint(1,1))
ufo4 = GameSprite('ufo.png', 65,65, randint(20,610), 0, randint(1,1))
ufo5 = GameSprite('ufo.png', 65,65, randint(20,610), 0, randint(1,1))
ufo6 = GameSprite('ufo.png', 65,65, randint(20,610), 0, randint(1,1))
monsters = sprite.Group()
monsters.add(ufo1, ufo2, ufo3, ufo4, ufo5, ufo6)
#ufo = GameSprite('ufo.png', 200,200,randint(20,610),0,randint(1,5))

asteroid1 = GameSprite('asteroid.png', 65,65, randint(20,610), 0, randint(1,1))
asteroids = sprite.Group()
asteroids.add(asteroid1,)

bullets = sprite.Group()

game = True
while game:
    window.blit(background,(0,0))
    rocket.reset()
 
    #ufo.reset()
    monsters.draw(window)
    monsters.update()
    bullets.draw(window)
    bullets.update()
    asteroids.draw(window)
    asteroids.update()
    miss_enemy = font1.render('что нибудь: ' + str(lost), 1, (255, 255, 255))
    window.blit(miss_enemy, (10,10))
    for el in event.get():
        if el.type == QUIT:
            game = False
        elif el.type == KEYDOWN:
            if el.key == K_SPACE:
                rocket.fire()
    keys = key.get_pressed()
    rocket.move_rocket()
    clock.tick(FPS)
    time.delay(5)
    display.update()