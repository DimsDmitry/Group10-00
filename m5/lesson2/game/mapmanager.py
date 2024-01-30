class Mapmanager():
    # управление картой
    def __init__(self):
        self.model = 'block'  # файл block.egg в котором лежит модель кубика
        self.texture = 'block.png'
        self.colors = [
            (0.5, 0.3, 0.0, 1),
            (0.2, 0.2, 0.3, 1),
            (0.5, 0.5, 0.2, 1),
            (0.0, 0.6, 0.0, 1)
        ]  # rgba
        # создаём основной узел карты
        self.startNew()

    def getColor(self, z):
        # получаем цвет для нужного уровня блоков
        if z < len(self.colors):
            return self.colors[z]
        return self.colors[len(self.colors) - 1]


    def startNew(self):
        # создание основы для новой карты
        self.land = render.attachNewNode('Land')

    def addBLock(self, position):
        # создание блока, установка его координат и цвета
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def loadLand(self, filename):
        # создаёт карту из текстового файла
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z) + 1):
                        self.addBLock((x, y, z0))
                    x += 1
                y += 1

    def clear(self):
        # обнулить карту
        self.land.removeNode()
        self.startNew()

