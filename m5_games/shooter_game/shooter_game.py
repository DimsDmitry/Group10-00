from pygame import *
from random import randint


'''создаём игровое окно'''

win_width = 700
win_height = 500
display.set_caption('Космическая битва')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))


score = 0 #сбито кораблей
lost = 0 #пропущено кораблей
max_lost = 3 #максимальное кол-во пропущенных кораблей
goal = 20 #сколько кораблей нужно сбить для победы


'''классы для спрайтов игры'''
class GameSprite(sprite.Sprite):
    '''класс-родитель для спрайтов'''
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        '''каждый спрайт - прямоугольник'''
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        '''отрисовка героя на окне'''
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    '''класс главного игрока'''
    def update(self):
        '''движение игрока'''
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        '''стрельба'''
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    '''класс спрайта-врага'''
    def update(self):
        self.rect.y += self.speed
        global lost
        '''враг исчезает, если дойдёт до края экрана'''
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1


class Bullet(GameSprite):
    '''класс спрайта-пули'''
    def update(self):
        '''движение пули'''
        self.rect.y += self.speed
        '''исчезает, если дойдёт до края экрана'''
        if self.rect.y < 0:
            self.kill()


'''создаём спрайты'''
ship = Player('rocket.png', 5, win_height - 100, 80, 100, 10)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

bullets = sprite.Group()

'''фоновая музыка'''
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

fire_sound = mixer.Sound('fire.ogg')

'''шрифты, надписи'''
font.init()

font1 = font.Font(None, 40)
win = font1.render('ПОБЕДА', True, (255, 255, 255))

font2 = font.Font(None, 36)


'''игровой цикл'''
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()

    if not finish:
        '''обновляем фон'''
        window.blit(background, (0, 0))

        '''пишем текст на экране'''
        text = font2.render('Счёт:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        '''включаем движение спрайтов'''
        ship.update()
        monsters.update()
        bullets.update()

        '''обновляем спрайты в новом местоположении при каждой итерации цикла'''
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        '''фиксируем касания монстров и пуль'''
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        '''текст поражения должен постоянно обновлять значение score'''
        lose = font1.render(f'ПОРАЖЕНИЕ! Сбито {str(score)} кораблей', True, (187, 30, 0))

        '''условие поражения'''
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))

        '''условие победы'''
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))

        display.update()

    time.delay(50)

