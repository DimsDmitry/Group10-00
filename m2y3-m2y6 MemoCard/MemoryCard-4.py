from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *


class Question:
    '''класс для создания вопросов'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


q1 = Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
q2 = Question('Какого цвета нет на флаге России?', 'Зелёный', 'Белый', 'Синий', 'Красный')
q3 = Question('Какой язык мы изучаем в нашей группе?', 'Python', 'C++', 'JavaScript', 'C#')


questions_list = []
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)


app = QApplication([])

window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(600, 300)

window.score = 0
window.total = 0

'''Интерфейс приложения'''
lb_Question = QLabel('Самый сложный вопрос в мире!')

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


def ask(q: Question):
    '''метод записывает значения вопроса и ответа в нужные виджеты,
    при этом варианты ответа рандомно перемешиваются'''
    shuffle(answers) #перемешали список вопросов
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


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
        window.score += 1
        print(f'Статистика \n Всего вопросов {window.total} \n Правильных ответов {window.score}')
        print(f'Рейтинг: {window.score / window.total * 100}%')
    elif answers[1].isChecked or answers[2].isChecked or answers[3].isChecked:
            show_correct('Неверно!')
            print(f'Рейтинг: {window.score / window.total * 100}%')


def next_question():
    '''задаёт следующий вопрос из списка'''
    window.total += 1
    print(f'Статистика \n Всего вопросов {window.total} \n Правильных ответов {window.score}')
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)


def click_OK():
    '''определяет, надо ли показывать другой вопрос или проверить ответ на этот'''
    if btn_OK.text() == 'Ответить':
        check_answer() #проверка ответа
    else:
        next_question() #следующий вопрос


btn_OK.clicked.connect(click_OK)

next_question()
window.setLayout(layout_card)
window.show()
app.exec()