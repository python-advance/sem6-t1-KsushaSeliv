
# coding: utf-8

# In[ ]:

#Исследовать функционал одного модуля не из стандартной библиотеки (например, joblib) и создать фрагмент ЭОР
#с описанием и примерами его использования при работе в Jupyter Notebook и в скриптах. 


Pandas – это библиотека, которая предоставляет очень удобные с точки зрения использования инструменты
для хранения данных и работе с ними. Если вы занимаетесь анализом данных или машинным обучением и при этом
используете язык Python, то вы просто обязаны знать и уметь работать с pandas.

Чтобы эффективно работать с pandas, необходимо освоить самые главные структуры данных библиотеки: DataFrame и Series. 


# In[ ]:

Series представляет из себя объект, похожий на одномерный массив (питоновский список, например),
но отличительной его чертой является наличие ассоциированных меток, т.н. индексов, вдоль каждого элемента из списка.
Такая особенность превращает его в ассоциативный массив или словарь в Python.


# In[3]:

import pandas as pd #импортируем модуль

my_series = pd.Series([5, 6, 7, 8, 9, 10])
print(my_series)


# In[ ]:

В строковом представлении объекта Series, индекс находится слева, а сам элемент справа. Если индекс явно не задан,
то pandas автоматически создаёт RangeIndex от 0 до N-1, где N общее количество элементов. Также стоит обратить,
что у Series есть тип хранимых элементов, в нашем случае это int64, т.к. мы передали целочисленные значения.



# In[5]:

#У объекта Series есть атрибуты через которые можно получить список элементов и индексы, это values и index соответственно.
print(my_series.index)
print(my_series.values)


# In[7]:

#Доступ к элементам объекта Series возможны по их индексу (вспоминается аналогия со словарем и доступом по ключу).
print(my_series[4])


# In[8]:

#Индексы можно задавать явно:
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(my_series2['f'])


# In[9]:

#Делать выборку по нескольким индексам и осуществлять групповое присваивание:
my_series2[['a', 'b', 'f']]
my_series2[['a', 'b', 'f']] = 0
print(my_series2)


# In[10]:

#Фильтровать Series как душе заблагорассудится, а также применять математические операции и многое другое:
print(my_series2[my_series2 > 0])


# In[11]:

print(my_series2[my_series2 > 0] * 2)


# In[12]:

#Если Series напоминает нам словарь, где ключом является индекс, а значением сам элемент, то можно сделать так:
my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
print('d' in my_series3)


# In[13]:

#У объекта Series и его индекса есть атрибут name, задающий имя объекту и индексу соответственно.
my_series3.name = 'numbers'
my_series3.index.name = 'letters'
print(my_series3)


# In[14]:

#Индекс можно поменять "на лету", присвоив список атрибуту index объекта Series
my_series3.index = ['A', 'B', 'C', 'D']
print(my_series3)


# In[ ]:




# In[ ]:

Объект DataFrame лучше всего представлять себе в виде обычной таблицы и это правильно, ведь DataFrame является
табличной структурой данных. В любой таблице всегда присутствуют строки и столбцы. Столбцами в объекте DataFrame выступают
объекты Series, строки которых являются их непосредственными элементами.


# In[18]:

#DataFrame проще всего сконструировать на примере питоновского словаря:
df = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],'population': [17.04, 143.5, 9.5, 45.5],
                   'square': [2724902, 17125191, 207600, 603628]})
print(df)


# In[19]:

#Чтобы убедиться, что столбец в DataFrame это Series, извлекаем любой:
print(df['country'])


# In[20]:

#Объект DataFrame имеет 2 индекса: по строкам и по столбцам. Если индекс по строкам явно не задан
#(например, колонка по которой нужно их строить), то pandas задаёт целочисленный индекс RangeIndex от 0 до N-1,
#где N это количество строк в таблице.
print(df.columns)
print(df.index)


# In[23]:

#В таблице у нас 4 элемента от 0 до 3. 
#Индекс по строкам можно задать разными способами, например, при формировании самого объекта DataFrame или "на лету":
df = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
                   'population': [17.04, 143.5, 9.5, 45.5],
                   'square': [2724902, 17125191, 207600, 603628]}, index=['KZ', 'RU', 'BY', 'UA'])
print(df)


# In[24]:

df.index = ['KZ', 'RU', 'BY', 'UA']
df.index.name = 'Country Code'
print(df)


# In[25]:

#Как видно, индексу было задано имя - Country Code. Отмечу, что объекты Series из DataFrame будут иметь те же индексы,
#что и объект DataFrame:
print(df['country'])


# In[26]:

#Доступ к строкам по индексу возможен несколькими способами:
#.loc - используется для доступа по строковой метке
#.iloc - используется для доступа по числовому значению (начиная от 0)
print(df.loc['KZ'])


# In[27]:

print(df.iloc[0])


# In[28]:

#Можно делать выборку по индексу и интересующим колонкам:
print(df.loc[['KZ', 'RU'], 'population'])


# In[29]:

#Как можно заметить, .loc в квадратных скобках принимает 2 аргумента: интересующий индекс, в том числе поддерживается
#слайсинг и колонки.
print(df.loc['KZ':'BY', :])


# In[30]:

#Фильтровать DataFrame с помощью т.н. булевых массивов:
print(df[df.population > 10][['country', 'square']])


# In[31]:

#Сбросить индексы можно вот так:
print(df.reset_index())


# In[32]:

#Добавим новый столбец, в котором население (в миллионах) поделим на площадь страны, получив тем самым плотность:
df['density'] = df['population'] / df['square'] * 1000000
print(df)


# In[35]:

#Не нравится новый столбец? Не проблема, удалим его:
print(df.drop(['density'], axis='columns'))


# In[ ]:




# In[ ]:



