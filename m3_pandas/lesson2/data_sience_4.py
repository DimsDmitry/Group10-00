import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Выведи на экран минимальный, средний и максимальный рейтинг ('Rating') платных и бесплатных приложений ('Type') с точностью до десятых.
result = df.groupby(by='Type')['Rating'].agg(['min', 'mean', 'max'])
result = round(result, 1)
print(result)
print(100 * '#', '\n')

# 2 Выведи на экран минимальную, медианную (median) и максимальную цену ('Price') платных приложений (Type == 'Paid') для 
# разных целевых аудиторий ('Content Rating')
result = df[df['Type'] == 'Paid'].groupby('Content Rating')['Price'].agg(['min', 'median', 'max'])
print(result)
print(100 * '#', '\n')

# 3 Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом
# посчитай максимальное количество отзывов ('Reviews') в каждой группе.
# Сравни результаты для категорий 'EDUCATION', 'FAMILY' и 'GAME':
# В какой возрастной группе больше всего отзывов получило приложение из категории 'EDUCATION'? 'FAMILY'? 'GAME'?
# Подсказка: ты можешь выбрать из DataFrame несколько столбцов одновременно с помощью такого синтаксиса:
# df[[<столбец 1>, <столбец 2>, <столбец 3>]]
result = df.pivot_table(columns='Category', index='Content Rating', values='Reviews', aggfunc='max')
print(type(result))
print(result[['EDUCATION', 'FAMILY', 'GAME']])
print(100 * '#', '\n')



# 4 Сгруппируй платные (Type == 'Paid') приложения по категории ('Category') и целевой аудитории ('Content Rating')
# Посчитай среднее количество отзывов ('Reviews') в каждой группе
# Обрати внимание, что в некоторых ячейках полученной таблицы отражается не число, а значение "NaN" - Not a Number
# Эта запись означает, что в данной группе нет ни одного приложения.
# Выбери названия категорий, в которых есть платные приложения для всех возрастных групп и расположи их в алфавитном порядке.
result = df[df['Type'] == 'Paid'].pivot_table(columns='Content Rating', index='Category', values='Reviews', aggfunc='mean')
print(result)
print(100 * '#', '\n')

# Бонусная задача. Найди категории бесплатных (Type == 'Free') приложений,
# в которых приложения разработаны не для всех возрастных групп ('Content Rating')
result = df[df['Type'] == 'Free'].pivot_table(columns='Content Rating', index='Category', values='Reviews', aggfunc='mean')
print(result)
print(100 * '#', '\n')
