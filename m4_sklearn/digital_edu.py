import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

import sklearn

from sklearn.model_selection import *
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Открытие CSV файла по пути
df = pd.read_csv('train.csv')
print(df.info())

# Убираем пропуски
df.dropna(inplace=True)
print(df.info())

# данные которые не рассматриваются - убираем
df = df.drop(
    ['life_main', 'people_main', 'city', 'last_seen', 'occupation_name',
     'has_photo', 'has_mobile', 'life_main', 'people_main'],
    axis=1)


def change_bd(row):
    # вычитаем из текущего года год рождения, получаем возраст
    birthday = row['bdate'].split('.')
    if len(birthday) == 3:
        row['bdate'] = 2023 - int(birthday[2])
    else:
        row['bdate'] = 0
    return row


df = df.apply(change_bd, axis=1)

print(df['education_form'].value_counts())


def change_ef(row):
    # заменяем форму образования кодовым числом
    row = row.replace('Full-time', 2)
    row = row.replace('Distance Learning', 1)
    row = row.replace('Part-time', 0)
    return row


df = df.apply(change_ef, axis=1)
print(df['education_form'])
