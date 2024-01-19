class Mapmanager():
    # управление картой
    def __init__(self):
        self.model = 'block'  # файл block.egg в котором лежит модель кубика
        self.texture = 'block.png'
        self.color = (0.2, 0.2, 0.35, 1)  # rgba

        # создаём основной узел карты
        self.startNew()
        # создаём строительные блоки
        self.addBLock((0, 10, 0))

    def startNew(self):
        # создание основы для новой карты
        self.land = render.attachNewNode('Land')

    def addBLock(self, position):
        # создание блока, установка его координат и цвета
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)