from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from random import shuffle

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(600, 300)

'''Интерфейс приложения'''
lb_Question = QLabel('Какой-то вопрос')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Ответ1')
rbtn_2 = QRadioButton('Ответ2')
rbtn_3 = QRadioButton('Ответ3')
rbtn_4 = QRadioButton('Ответ4')

btn_OK = QPushButton('Ответить')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

'''размещение линий'''
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()

layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) #два ответа в левый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) #два ответа в правый столбец
layout_ans3.addWidget(rbtn_4)
'''разместим столбцы в одной строке'''
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
'''панель с вариантами ответов'''
RadioGroupBox.setLayout(layout_ans1)

'''Создадим панель результата'''
AnsGroupBox = QGroupBox('Результат')
lb_Result = QLabel('Прав ты или нет?') #здесь расместится надпись "правильно" или "неправильно"
lb_Correct = QLabel('Правильно/неправильно') #здесь будет написан правильный ответ

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignRight | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() #вопрос
layout_line2 = QHBoxLayout() #варианты ответов
layout_line3 = QHBoxLayout() #кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignCenter | Qt.AlignVCenter))
'''разместим две панели в одной строке - одна будет скрываться, другая будет показываться'''


layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) #чтобы кнопка была большой
layout_line3.addStretch(1)

'''теперь созданные строки разместим друг под другом'''
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


def show_result():
    '''показать панель ответов'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    '''показать панель вопросов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) #снять ограничение на выбор только одной кнопки
    rbtn_1.setChecked(False) #сброс выбора кнопки
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    '''вернуть ограничение, теперь только
     одна радиокнопка может быть выбрана'''




answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(question, right_answer, wrong1, wrong2, wrong3):
    '''метод записывает значения вопроса и ответа в нужные виджеты,
    при этом варианты ответа рандомно перемешиваются'''
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_Question.setText(question)
    lb_Correct.setText(right_answer)

def show_correct(res):
    '''показать результат - установим текст в надпись "результат"
    и переключим панель'''
    lb_Result.setText(res)
    show_result()

def check_answer():
    '''если выбран вариант ответа, надо проверить его
    и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Правильно!')
    elif answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
        show_correct('Неверно!')


btn_OK.clicked.connect(check_answer)


window.setLayout(layout_card)
ask('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
window.show()
app.exec()