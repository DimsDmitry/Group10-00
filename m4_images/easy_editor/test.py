import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PIL import Image
from PIL import ImageFilter
from PIL.ImageFilter import *

app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Мини редактор')

lb_imaje = QLabel('картинка')
but_papk = QPushButton('Папка')
spis_file = QListWidget()

'''Кнопки редактирования'''

but_left = QPushButton('Лево')
but_rite = QPushButton('Право')
but_zerk = QPushButton('Зеркально')
but_rezk = QPushButton('Резкость')
but_bl_wi = QPushButton('Ч/Б')

'''Размещение'''
row = QHBoxLayout()
kol1 = QVBoxLayout()
kol2 = QVBoxLayout()
line_but = QHBoxLayout()

line_but.addWidget(but_left)
line_but.addWidget(but_rite)
line_but.addWidget(but_zerk)
line_but.addWidget(but_rezk)
line_but.addWidget(but_bl_wi)
kol1.addWidget(but_papk)
kol1.addWidget(spis_file)
kol2.addWidget(lb_imaje, 95)
kol2.addLayout(line_but)
row.addLayout(kol1, 20)
row.addLayout(kol2, 80)
win.setLayout(row)

win.show()

workdir = ''


def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.andswith(ext):
                result.append(filename)
    return result


def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.JPG']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    spis_file.clear()
    for filename in filenames:
        spis_file.addItem(filename)


but_papk.clicked.connect(showFilenamesList)


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'

    def LoadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def shavImage(self, path):
        lb_imaje.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_imaje.width(), lb_imaje.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_imaje.setPixmap(pixmapimage)
        lb_imaje.show()

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def wi_bl(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.shavImage(image_path)

    def do_zerk(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.shavImage(image_path)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.shavImage(image_path)

    def do_rite(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.shavImage(image_path)

    def do_rezk(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.shavImage(image_path)


def shawCoosenImage():
    if spis_file.currentRow() >= 0:
        filename = spis_file.currentItem().text()
        workimage.LoadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.shavImage(image_path)


workimage = ImageProcessor()
spis_file.currentRowChanged.connect(shawCoosenImage)

but_bl_wi.clicked.connect(workimage.wi_bl)
but_rezk.clicked.connect(workimage.do_rezk)
but_left.clicked.connect(workimage.do_left)
but_rite.clicked.connect(workimage.do_rite)
but_zerk.clicked.connect(workimage.do_zerk)

app.exec()