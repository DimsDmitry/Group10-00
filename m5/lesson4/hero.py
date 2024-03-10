key_switch_camera = 'c'  # отвязка/привязка камеры к игроку
key_turn_left = 'n'  # поворот влево
key_turn_right = 'm'  # поворот вправо

key_forward = 'w'  # шаг вперёд
key_back = 's'  # шаг назад
key_left = 'a'  # шаг влево
key_right = 'd'  # шаг вправо
key_up = 'e'  # шаг вверх
key_down = 'q'  # шаг вниз

key_switch_mode = 'z'  # смена игрового режима (можно проходить сквозь блоки или нет)

key_build = 'b'  # построить блок перед собой
key_destroy = 'v'  # разрушить блок перед собой

key_savemap = 'k'  # сохранить карту
key_loadmap = 'l'  # загрузить карту


class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.mode = True  # режим прохождения сквозь всё
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setH(180)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        # привязать камеру к персонажу
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        # отвязать камеру от персонажа
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_left(self):
        # поворот влево
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        # поворот вправо
        self.hero.setH((self.hero.getH() - 5) % 360)

    def look_at(self, angle):
        """возвращает координаты, в которые переместится персонаж, стоящий точке (x, y),
        если он делает шаг в направлении angle"""
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from

    def just_move(self, angle):
        # перемещается в нужные координаты в любом случае
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def try_move(self, angle):
        # перемещаемся, если можем
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            # перед нами свободно. Можно упасть вниз
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            # перед нами занято. Попробуем забраться вверх
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)
                # если не получилось забраться - стоим на месте

    def changeMode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True
        print('режим изменён')

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def check_dir(self, angle):
        """возвращает изменения координат x и y при перемещении в направлении угла поворота игрока.
        Если угол поворота больше нуля, но меньше 20 градусов, координату y уменьшаем на 1.
        И так далее по кругу.
        угол 0-20 -> Y - 1
        угол 20-65 -> X + 1, Y - 1
        угол 65-110 -> X + 1
        угол 110-155 -> X + 1, Y + 1
        угол 155-200 -> Y + 1
        угол 200-245 -> X - 1, Y + 1
        угол 245-290 -> X - 1
        угол 290-335 -> X - 1, Y - 1
        угол от 340 -> Y - 1
        """
        if 0 <= angle <= 20:
            return 0, -1
        elif angle <= 65:
            return 1, -1
        elif angle <= 110:
            return 1, 0
        elif angle <= 155:
            return 1, 1
        elif angle <= 200:
            return 0, 1
        elif angle <= 245:
            return -1, 1
        elif angle <= 290:
            return -1, 0
        elif angle <= 335:
            return -1, -1
        return 0, -1

    def forward(self):
        # вперёд
        angle = (self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        # назад
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def left(self):
        # влево
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        # вправо
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    def up(self):
        # вверх
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        # вниз
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)

    def build(self):
        # смотрим, какой сейчас режим игры, вызываем нужный метод для строительства блоков
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.build_block(pos)

    def destroy(self):
        # смотрим, какой сейчас режим игры, вызываем нужный метод для удаления блоков
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)

    def accept_events(self):
        # обработка событий
        base.accept(key_switch_camera, self.changeView)
        base.accept(key_switch_mode, self.changeMode)
        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_right, self.turn_right)

        base.accept(key_turn_left + '-repeat', self.turn_left)
        base.accept(key_turn_right + '-repeat', self.turn_right)

        base.accept(key_forward, self.forward)
        base.accept(key_forward + '-repeat', self.forward)

        base.accept(key_back, self.back)
        base.accept(key_back + '-repeat', self.back)

        base.accept(key_left, self.left)
        base.accept(key_left + '-repeat', self.left)

        base.accept(key_right, self.right)
        base.accept(key_right + '-repeat', self.right)

        base.accept(key_up, self.up)
        base.accept(key_up + '-repeat', self.up)

        base.accept(key_down, self.down)
        base.accept(key_down + '-repeat', self.down)

        base.accept(key_build, self.build)
        base.accept(key_destroy, self.destroy)

        base.accept(key_savemap, self.land.saveMap)
        base.accept(key_loadmap, self.land.loadMap)
