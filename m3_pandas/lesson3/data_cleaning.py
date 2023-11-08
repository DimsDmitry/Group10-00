import pandas as pd

df = pd.read_csv('GooglePlayStore_wild.csv')
# Выведи информацию о всем DataFrame, чтобы узнать какие столбцы нуждаются в очистке
print(df.info())
print(100 * '#', '\n')

# Сколько в датасете приложений, у которых не указан ('NaN') рейтинг ('Rating')?
result = df[pd.isnull(df['Rating'])]
print('Количество приложений:', len(result))
print(100 * '*', '\n')

# Замени пустое значение ('NaN') рейтинга ('Rating') для таких приложений на -1.
df['Rating'].fillna(-1, inplace=True)

# Определи, какое ещё значение размера ('Size') хранится в датасете помимо Килобайтов и Мегабайтов, замени его на -1.
# Преобразуй размеры приложений ('Size') в числовой формат (float). Размер всех приложений должен измеряться в Мегабайтах.
print(df['Size'].value_counts())


def set_size(size):
    if size[-1] == 'M':
        return float(size[:-1])
    if size[-1] == 'k':
        return float(size[:-1]) / 1024
    return -1


df['Size'] = df['Size'].apply(set_size)
print(100 * '*', '\n')
# Чему равен максимальный размер ('Size') приложений из категории ('Category') 'TOOLS'?
result = df[df['Category'] == 'TOOLS']['Size'].max()
print(result)


# Бонусные задания
# Замени тип данных на целочисленный (int) для количества установок ('Installs').
# В записи количества установок ('Installs') знак "+" необходимо игнорировать.
# Т.е. если в датасете количество установок равно 1,000,000+, то необходимо изменить значение на 1000000
def set_installs(installs):
    if installs == '0':
        return 0
    return int(installs[:-1].replace(',', ''))


df['Installs'] = df['Installs'].apply(set_installs)
print(100 * '*', '\n')
# Сгруппируй данные по типу ('Type') и целевой аудитории ('Content Rating'), посчитай среднее количество
# установок ('Installs') в каждой группе. Результат округли до десятых.
# В полученной таблице найди ячейку с самым большим значением. К какой возрастной группе и типу приложений относятся
# данные из этой ячейки?

result = df.pivot_table(index='Content Rating', columns='Type', values='Installs', aggfunc='mean')
result = round(result, 1)
print(result)
print(100 * '#', '\n')
# У какого приложения не указан тип ('Type')? Какой тип там необходимо записать в зависимости от цены?
result = df[pd.isnull(df['Type'])]
print(result.iloc[0])
print(100 * '#', '\n')
# Выведи информацию о всем DataFrame, чтобы убедиться, что очистка прошла успешно
print(df.info())
