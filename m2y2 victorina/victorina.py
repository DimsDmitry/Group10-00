from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

def show_win():
    '''при выборе правильного ответа отображаем выигрыш'''
    victory_win = QMessageBox()
    victory_win.setText('Верно!\nВы выиграли MacBook!')
    victory_win.exec_()

def show_lose():
    '''при выборе неправильного ответа отображаем утешительный приз'''
    victory_win = QMessageBox()
    victory_win.setText('Нет, это Iphone 9!\nВы выиграли чехол')
    victory_win.exec_()


'''создаём приложение, окно, заголовок, указываем размер'''
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от Алгоритмики')
main_win.resize(400, 200)

'''создаём виджеты'''
question = QLabel('Какого айфона не существует?')
btn_answer1 = QRadioButton('Iphone 2g')
btn_answer2 = QRadioButton('Iphone 14')
btn_answer3 = QRadioButton('Iphone 9')
btn_answer4 = QRadioButton('Iphone XS')

'''размещаем виджеты по линиям'''
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(question, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment=Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)

main_win.setLayout(layout_main)

'''подключаем кнопки к методам'''
btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_win)
btn_answer4.clicked.connect(show_lose)

main_win.show()
app.exec_()