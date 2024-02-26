import pickle


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

    def addBlock(self, position):
        # создание блока, установка его координат и цвета
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color)
        self.block.setTag("at", str(position))
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
                        self.addBlock((x, y, z0))
                    x += 1
                y += 1
        return x, y

    def clear(self):
        # обнулить карту
        self.land.removeNode()
        self.startNew()

    def isEmpty(self, pos):
        # проверяет, пусто ли перед нами
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        return True

    def findBlocks(self, pos):
        # находит блоки перед нами
        result = self.land.findAllMatches("=at=" + str(pos))
        return result

    def findHighestEmpty(self, pos):
        # поиск высоты блока перед игроком
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return x, y, z

    def build_block(self, pos):
        # ставим блок с учётом гравитации
        x, y, z = pos
        cords_new = self.findHighestEmpty(pos)
        if cords_new[2] <= z + 1:
            self.addBlock(cords_new)

    def delBlock(self, pos):
        # удаляет блоки в указанной позиции
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()

    def delBlockFrom(self, pos):
        # удаляет блоки в основном режиме
        x, y, z = self.findHighestEmpty(pos)
        pos = x, y, z - 1
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()

    def saveMap(self):
        """сохраняет все блоки, включая постройки, в бинарный файл"""
        # возвращает коллекцию NodePath для всех существующих блоков
        blocks = self.land.getChildren()
        # открываем бинарный файл на запись
        with open('my_map.dat', 'wb') as file:
            # сначала сохраняем количество блоков
            pickle.dump(len(blocks), file)
            # затем итерируем все блоки циклом for
            for block in blocks:
                # сохраняем позицию
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, file)