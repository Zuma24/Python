# -*- coding: utf-8 -*-
"""10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19zmqrZ3xMghbUbrIzMJBJmyOj7tO7BLQ
"""

import pandas as pd

import seaborn as sns

df = pd.read_csv('sample_data/california_housing_test.csv')

"""1. Изобразите отношение households к population с
помощью точечного графика


"""

sns.scatterplot(data=df, x="households", y="population")

"""2. Визуализировать longitude по отношения к
median_house_value, используя линейный график

"""

sns.lineplot(x="latitude", y="median_house_value", data=df)

sns.relplot(x="latitude", y="median_house_value", kind="line", data=df)

"""3. Представить гистограмму по housing_median_age"""

sns.histplot(data = df, x = 'housing_median_age')

"""
4. Изобразить гистограмму по median_house_value с
оттенком housing_median_age"""

sns.displot(df, x= "median_house_value", hue="housing_median_age")

"""Написать EDA для датасета про пингвинов

Необходимо:

Использовать 2-3 точечных графика
Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
Использовать PairGrid с типом графика на ваш выбор
Использовать 2-3 гистограммы

"""

penguins = sns.load_dataset('penguins')
penguins.head()
some_list = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']
g = sns.PairGrid(penguins[some_list], hue = 'sex')
g.map(sns.scatterplot)

"""1. Создать новый столбец в таблице с
пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)

"""

penguins.loc[penguins['bill_length_mm'] >= 42, 'height_group'] = 'high'
penguins.loc[(penguins['bill_length_mm'] >= 35) & (penguins['bill_length_mm'] < 45),'height_group'] = 'middle'
penguins.loc[penguins['bill_length_mm'] < 35, 'height_group'] = 'low'
penguins

"""1. Изобразить гистограмму по flipper_length_mm
с оттенком height_group. Сделать анализ
"""

sns.histplot(data = penguins, x ='flipper_length_mm', hue = 'height_group')

"""Задание 44 В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random lst = ['robot'] * 10 lst += ['human'] * 10 random.shuffle(lst) data = pd.DataFrame({'whoAmI': lst}) data.head() |

В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head() |
"""

import random
from sklearn.preprocessing import OneHotEncoder
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
pd.get_dummies(data, columns=['whoAmI'], drop_first= True)

import pandas as pd
d = pd.DataFrame(random.sample(['1', '0']*10, 20) ,columns={'whoAmI'})
d

import random as rn
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
rn.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
# pd.drop(['whoAmI'],axis=1, inplace=True)