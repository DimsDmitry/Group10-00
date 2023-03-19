from pygame import *
from random import randint
from time import time as timer


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
life = 3 #очки здоровья


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


class Asteroid(GameSprite):
    '''класс спрайта-астероида'''
    def update(self):
        self.rect.y += self.speed
        '''враг исчезает, если дойдёт до края экрана'''
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0


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


asteroids = sprite.Group()
for i in range(1, 3):
    meteor = Asteroid('asteroid.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 7))
    asteroids.add(meteor)

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
font3 = font.Font(None, 80)


'''игровой цикл'''
run = True
finish = False

rel_time = False #флаг, отвечающий за перезарядку
num_fire = 0 #переменная для подсчёта выстрелов

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and not rel_time:
                    num_fire += 1
                    fire_sound.play()
                    ship.fire()
                if num_fire >= 5 and not rel_time:
                    last_time = timer()
                    rel_time = True


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
        asteroids.update()

        '''обновляем спрайты в новом местоположении при каждой итерации цикла'''
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        asteroids.draw(window)


        '''перезарядка'''
        if rel_time:
            now_time = timer()

            if now_time - last_time < 3:
                '''пока не прошло 3 секунды, выводим информацию о перезарядке'''
                reload = font2.render('Подождите, перезарядка...', 1, (150, 0, 0))
                window.blit(reload, (200, 460))
            else:
                '''обнуляем счётчик пуль, сбрасываем флаг перезарядки'''
                num_fire = 0
                rel_time = False

        '''фиксируем касания монстров и пуль'''
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        '''текст поражения должен постоянно обновлять значение score'''
        lose = font1.render(f'ПОРАЖЕНИЕ! Сбито {str(score)} кораблей', True, (187, 30, 0))


        if sprite.spritecollide(ship, monsters, True) or sprite.spritecollide(ship, asteroids, True):
            life -= 1

        '''условие поражения'''
        if life == 0 or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))


        '''условие победы'''
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))


        '''задаём разный цвет в зависимости от кол-ва жизней'''
        if life == 3:
            life_color = (0, 150, 0)
        if life == 2:
            life_color = (150, 150, 0)
        if life == 1:
            life_color = (150, 0, 0)

        text_life = font3.render(str(life), 1, life_color)
        window.blit(text_life, (600, 20))

        display.update()

    time.delay(50)

