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
df = df.drop(['life_main', 'people_main', 'city', 'last_seen', 'occupation_name', 'has_photo', 'has_mobile'], axis=1)
