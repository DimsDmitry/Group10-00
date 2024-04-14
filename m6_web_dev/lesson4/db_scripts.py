import sqlite3

db_name = 'quiz.sqlite'
conn = None
curor = None


def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close():
    cursor.close()
    conn.close()


def do(query):
    cursor.execute(query)
    conn.commit()


def clear_db():
    ''' удаляет все таблицы '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()


def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')

    do('''CREATE TABLE IF NOT EXISTS quiz (
        id INTEGER PRIMARY KEY,
        name VARCHAR)''')

    do('''CREATE TABLE IF NOT EXISTS question (
            id INTEGER PRIMARY KEY,
            question VARCHAR,
            answer VARCHAR,
            wrong1 VARCHAR,
            wrong2 VARCHAR,
            wrong3 VARCHAR)''')

    do('''CREATE TABLE IF NOT EXISTS quiz_content (
                id INTEGER PRIMARY KEY,
                quiz_id INTEGER,
                question_id INTEGER,
                FOREIGN KEY (quiz_id) REFERENCES quiz(id),
                FOREIGN KEY (question_id) REFERENCES question(id) )''')

    close()


def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()


def show_tables():
    show('question')
    show('quiz')
    show('quiz_content')


def main():
    clear_db()
    create()
    show_tables()


def add_questions():
    questions = [
        ('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один', 'Ни одного', 'Два'),
        ('Чему равно число Пи?', 'Примерно 3.14', '3', '0', 'Ровно 3.14'),
        ('Какой рукой лучше мешать чай?', 'Ложкой', 'Левой', 'Правой', 'Любой'),
        ('Что не имеет длины, ширины, высоты, а можно измерить?', 'Время', 'Глупость', 'Море', 'Воздух'),
        ('Что больше слона и ничего не весит?', 'Тень слона', 'Облако', 'Парашют', 'Облако'),
        ('Каким станет камень если упадёт в Красное море?', 'Мокрым', 'Красным', 'Розовым', 'Не изменится'),
        ('Самая высокая гора в мире?', 'Эверест', 'Эльбрус', 'Казбек', 'Аконкагуа')
    ]
    open()
    cursor.executemany(
        '''INSERT INTO question (question, answer, wrong1, wrong2, wrong3) VALUES (?, ?, ?, ?, ?)''', questions
    )
    conn.commit()
    close()


def add_quiz():
    quizes = [
        ('Своя игра',),
        ('Кто хочет стать миллионером?',),
        ('Самый',)
    ]
    open()
    cursor.executemany(
        '''INSERT INTO quiz (name) VALUES (?)''', quizes
    )
    conn.commit()
    close()


def add_links():
    # связываем таблицу вопросов и викторин
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    query = 'INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)'
    answer = input('Добавить связь? (д/н)')
    while answer != 'н':
        quiz_id = int(input('id викторины'))
        question_id = int(input('id вопроса'))
        cursor.execute(query, [quiz_id, question_id])
        conn.commit()
        answer = input('Добавить связь? (д/н)')
    close()


if __name__ == "__main__":
    main()
