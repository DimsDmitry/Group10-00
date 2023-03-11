from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from random import randint

app = QApplication([])

'''Главное окно:'''
my_win = QWidget()
my_win.setWindowTitle('Определитель победителя')
my_win.move(100, 100)
my_win.resize(400, 200)

'''Виджеты окна: кнопка, надписи'''
button = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')

'''Расположение виджетов'''
line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
my_win.setLayout(line)

def show_winner():
    '''метод, генерирующий рандомное число'''
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Победитель:')

'''Обработка нажатия на кнопку'''
button.clicked.connect(show_winner)

my_win.show()
app.exec()