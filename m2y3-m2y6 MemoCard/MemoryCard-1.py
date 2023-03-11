from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

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
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() #вопрос
layout_line2 = QHBoxLayout() #варианты ответов
layout_line3 = QHBoxLayout() #кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignCenter | Qt.AlignVCenter))
'''разместим две панели в одной строке - одна будет скрываться, другая будет показываться'''


layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

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

window.setLayout(layout_card)
window.show()
app.exec()