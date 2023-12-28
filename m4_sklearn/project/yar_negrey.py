import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

import sklearn

from sklearn.model_selection import *
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('train.csv')
df.dropna(inplace=True)

# Подготовка данных и удаление ненужного

df = df.drop(['people_main', 'last_seen', 'city', 'occupation_name', 'has_photo', 'has_mobile', 'life_main'], axis=1)


def change_ef(row):
    row = row.replace('Full-time', 2)
    row = row.replace('Distance Learning', 1)
    row = row.replace('Part-time', 0)
    return row


df = df.apply(change_ef, axis=1)

df['education_status'] = df['education_status'].astype('category')
df['education_status'] = df['education_status'].cat.codes

df['occupation_type'] = df['occupation_type'].astype('category')
df['occupation_type'] = df['occupation_type'].cat.codes

df['sex'] = df['sex'].astype('category')
df['sex'] = df['sex'].cat.codes

df['langs'] = df['langs'].astype('category')
df['langs'] = df['langs'].cat.codes

df['occupation_type'] = df['occupation_type'].astype('category')
df['occupation_type'] = df['occupation_type'].cat.codes

df['career_start'] = df['career_start'].astype('category')
df['career_start'] = df['career_start'].cat.codes

df['career_end'] = df['career_end'].astype('category')
df['career_end'] = df['career_end'].cat.codes


def change_bd(row):
    birthday = row['bdate'].split('.')
    if len(birthday) == 3:
        row['bdate'] = 2023 - int(birthday[2])
    else:
        row['bdate'] = 0
    return row


df = df.apply(change_bd, axis=1)

print(df.info())
print(100 * '#')

# Теперь модель, создадим подборки X, y

scaler = StandardScaler()
result = df.drop('result', axis=1)

scaler.fit(result)
scaled = scaler.transform(result)
scaled_df = pd.DataFrame(scaled, columns=result.columns)

X = scaled_df
y = df['result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Буду использовать метод k-ближайших соседей
# Подберём нужное k

errors = []
for i in np.arange(1, 101):
    new_model = KNeighborsClassifier(n_neighbors=i)
    new_model.fit(X_train, y_train)
    new_pred = new_model.predict(X_test)
    errors.append(np.mean(new_pred != y_test))

plt.plot(errors)

# График покажется в конце программы
# По графику видно, что например, 85 будет очень маленьким (ну у меня по крайней мере), так что возьмём его.

model = KNeighborsClassifier(n_neighbors=85)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print(y_test)
print(pred)

# Проверяем предсказания модели

print(100 * '#')
print(confusion_matrix(y_test, pred))  # матрица ошибок
print(100 * '#')
print(accuracy_score(y_test, pred))  # процент

plt.show()
