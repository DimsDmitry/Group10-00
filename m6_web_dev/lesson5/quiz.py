from flask import *
from db_scripts import *
from random import randint


def index():
    # рандомно выбирается викторина. Её номер добавляется в словарь session
    max_quiz = 3
    session['quiz'] = randint(1, max_quiz)
    session['last_question'] = 0
    return '<a href="/test">Тест</a>'


def test():
    result = get_question_after(session['last_question'], session['quiz'])
    if result is None or len(result) == 0:
        return redirect(url_for('result'))
    else:
        session['last_question'] = result[0]
        text = '<h1>' + str(session["quiz"]) + '<br>' + str(result) + '</h1>'
        return text


def result():
    return 'Это все вопросы!'


app = Flask(__name__)
app.add_url_rule('/', 'index', index)  # создаёт правило для URL '/'
app.add_url_rule('/test', 'test', test)  # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result)  # создаёт правило для URL '/result'

app.config['SECRET_KEY'] = 'ThisisSecretSecretSecretKey'

if __name__ == '__main__':
    # запускаем веб-сервер
    app.run()
