from flask import *
from db_scripts import *


def start_quiz(quiz_id):
    """создаёт нужные значения в словаре session"""
    session['quiz'] = quiz_id
    session['last_question'] = 0


def end_quiz():
    """закончить викторину"""
    session.clear()


def quiz_form():
    """ функция получает список викторин из базы и формирует форму с выпадающим списком"""
    html_beg = '''<html><body><h2>Выберите викторину:</h2><form method="post" action="index"><select name="quiz">'''
    frm_submit = '''<p><input type="submit" value="Выбрать"> </p>'''

    html_end = '''</select>''' + frm_submit + '''</form></body></html>'''
    options = ''' '''
    q_list = get_quises()
    for id, name in q_list:
        option_line = ('''<option value="''' +
                       str(id) + '''">''' +
                       str(name) + '''</option>
                      ''')
        options = options + option_line
    return html_beg + options + html_end


def index():
    """ Первая страница: если пришли запросом GET, то выбрать викторину,
    если POST - то запомнить id викторины и отправлять на вопросы"""
    if request.method == 'GET':
        # викторина не выбрана, сбрасываем id викторины и показываем форму выбора
        start_quiz(-1)
        return quiz_form()
    else:
        # получили дополнительные данные в запросе! Используем их:
        quest_id = request.form.get('quiz')  # выбранный номер викторины
        start_quiz(quest_id)
        return redirect(url_for('test'))


def test():
    """возвращает страницу вопроса"""
    # если пользователь не выбрал викторину и сразу перешёл на адрес /test,
    # перенаправляем его обратно на главную страницу
    if not ('quiz' in session) or int(session['quiz']) < 0:
        return redirect(url_for('index'))
    else:
        # старая часть функции
        result = get_question_after(session['last_question'], session['quiz'])
        if result is None or len(result) == 0:
            return redirect(url_for('result'))
        else:
            session['last_question'] = result[0]
            text = '<h1>' + str(session["quiz"]) + '<br>' + str(result) + '</h1>'
            return text


def result():
    end_quiz()
    return 'Это все вопросы!'


# создаём приложение
app = Flask(__name__)
# привязываем к нему страницы
app.add_url_rule('/', 'index', index)  # создаёт правило для URL '/'
app.add_url_rule('/index', 'index', index, methods=['post', 'get'])  # правило для '/index'
app.add_url_rule('/test', 'test', test)  # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result)  # создаёт правило для URL '/result'

app.config['SECRET_KEY'] = 'ThisisSecretSecretSecretKey'

if __name__ == '__main__':
    # запускаем веб-сервер
    app.run()
