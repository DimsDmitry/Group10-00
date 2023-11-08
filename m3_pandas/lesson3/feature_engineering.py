import pandas as pd

df = pd.read_csv('GooglePlayStore_wild.csv')

# Очистка данных из первого задания
df['Rating'].fillna(-1, inplace=True)


def set_size(size):
    if size[-1] == 'M':
        return float(size[:-1])
    if size[-1] == 'k':
        return float(size[:-1]) / 1024
    return -1


df['Size'] = df['Size'].apply(set_size)


def set_installs(installs):
    if installs == '0':
        return 0
    return int(installs[:-1].replace(',', ''))


df['Installs'] = df['Installs'].apply(set_installs)

df['Type'].fillna('Free', inplace=True)


# Замени тип данных на дробное число (float) для цен приложений ('Price')
def make_price(price):
    if price[0] == '$':
        return float(price[1:])
    return 0


df['Price'] = df['Price'].apply(make_price)
# Вычисли, сколько долларов разработчики заработали на каждом платном приложении
df['Profit'] = df['Installs'] * df['Price']

# Чему равен максимальный доход ('Profit') среди платных приложений (Type == 'Paid')?
result = df[df['Type'] == 'Paid']['Profit'].max()
print(result)


# Создай новый столбец, в котором будет храниться количество жанров. Назови его 'Number of genres'
def split_genres(genres):
    return genres.split(';')


df['Genres'] = df['Genres'].apply(split_genres)
df['Number of genres'] = df['Genres'].apply(len)
# Какое максимальное количество жанров ('Number of genres') хранится в датасете?
print(df['Number of genres'].max())


# Бонусное задание
# Создай новый столбец, хранящий сезон, в котором было произведено последнее обновление ('Last Updated') приложения. Назови его 'Season'

# Выведи на экран сезоны и их количество в датасете


def set_season(date):
    month = date.split()[0]
    seasons = {
        'Зима': ['December', 'January', 'February'],
        'Весна': ['March', 'April', 'May'],
        'Лето': ['June', 'July', 'August'],
        'Осень': ['September', 'October', 'November']
    }
    for season in seasons:
        if month in seasons[season]:
            return season
    return 'Сезон не установлен'


df['Season'] = df['Last Updated'].apply(set_season)
print(df['Season'].value_counts())
