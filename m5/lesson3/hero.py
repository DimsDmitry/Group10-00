key_switch_camera = 'c'  # отвязка/привязка камеры к игроку
key_turn_left = 'n'  # поворот влево
key_turn_right = 'm'  # поворот вправо


class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.mode = True  # режим прохождения сквозь всё
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        # привязать камеру к персонажу
        base.disableMouse()
        base.camera.setH(180)
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

    def accept_events(self):
        # обработка событий
        base.accept(key_switch_camera, self.changeView)
        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_right, self.turn_right)

        base.accept(key_turn_left + '-repeat', self.turn_left)
        base.accept(key_turn_right + '-repeat', self.turn_right)
