
# coding: utf-8

# In[ ]:

#Исследовать функционал одного из модулей стандартной библиотеки (string, re, datetime, math, random, os, и т.д.).

Модуль math – один из наиважнейших в Python. Этот модуль предоставляет обширный функционал для работы с числами.

math.ceil(X) – округление до ближайшего большего числа.

math.copysign(X, Y) - возвращает число, имеющее модуль такой же, как и у числа X, а знак - как у числа Y.

math.fabs(X) - модуль X.

math.factorial(X) - факториал числа X.

math.floor(X) - округление вниз.

math.fmod(X, Y) - остаток от деления X на Y.

math.frexp(X) - возвращает мантиссу и экспоненту числа.

math.ldexp(X, I) - X * 2i. Функция, обратная функции math.frexp().

math.fsum(последовательность) - сумма всех членов последовательности. Эквивалент встроенной функции sum(), но math.fsum() более точна для чисел с плавающей точкой.

math.isfinite(X) - является ли X числом.

math.isinf(X) - является ли X бесконечностью.

math.isnan(X) - является ли X NaN (Not a Number - не число).

math.modf(X) - возвращает дробную и целую часть числа X. Оба числа имеют тот же знак, что и X.

math.trunc(X) - усекает значение X до целого.

math.exp(X) - eX.

math.expm1(X) - eX - 1. При X → 0 точнее, чем math.exp(X)-1.

math.log(X, [base]) - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм.

math.log1p(X) - натуральный логарифм (1 + X). При X → 0 точнее, чем math.log(1+X).

math.log10(X) - логарифм X по основанию 10.

math.log2(X) - логарифм X по основанию 2. Новое в Python 3.3.

math.pow(X, Y) - XY.

math.sqrt(X) - квадратный корень из X.

math.acos(X) - арккосинус X. В радианах.

math.asin(X) - арксинус X. В радианах.

math.atan(X) - арктангенс X. В радианах.

math.atan2(Y, X) - арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка (X, Y).

math.cos(X) - косинус X (X указывается в радианах).

math.sin(X) - синус X (X указывается в радианах).

math.tan(X) - тангенс X (X указывается в радианах).

math.hypot(X, Y) - вычисляет гипотенузу треугольника с катетами X и Y (math.sqrt(x * x + y * y)).

math.degrees(X) - конвертирует радианы в градусы.

math.radians(X) - конвертирует градусы в радианы.

math.cosh(X) - вычисляет гиперболический косинус.

math.sinh(X) - вычисляет гиперболический синус.

math.tanh(X) - вычисляет гиперболический тангенс.

math.acosh(X) - вычисляет обратный гиперболический косинус.

math.asinh(X) - вычисляет обратный гиперболический синус.

math.atanh(X) - вычисляет обратный гиперболический тангенс.

math.erf(X) - функция ошибок.

math.erfc(X) - дополнительная функция ошибок (1 - math.erf(X)).

math.gamma(X) - гамма-функция X.

math.lgamma(X) - натуральный логарифм гамма-функции X.

math.pi - pi = 3,1415926...

math.e - e = 2,718281...


# In[3]:

#Рассмотрим наиболее часто используемые функции.

import math #Для работы с данным модулем его предварительно нужно импортировать.


math.ceil(3.2) #Возвращает ближайшее целое число большее, чем x.


# In[4]:

math.fabs(-7) #Возвращает абсолютное значение числа.


# In[5]:

math.factorial(5) #Возвращает ближайшее целое число меньшее, чем x.


# In[6]:

math.floor(3.2) #Возвращает ближайшее целое число меньшее, чем x.


# In[7]:

math.exp(3) #Вычисляет e**x.


# In[12]:

math.log2(8) #По умолчанию вычисляет логарифм по основанию e, дополнительно можно указать основание логарифма.


# In[11]:

math.log(4, 8)


# In[13]:

math.pow(3, 4) #Вычисляет значение x в степени y.


# In[14]:

math.sqrt(25) #Корень квадратный от x.


# In[ ]:




# In[15]:

#Создание пользовательского пакета для приложения «Гостевая книга» с прототипами методов,
#позволяющих взаимодействовать с JSON-файлом (создание, удаление, переименование, чтение, запись). 


class GuestBook():

    def __init__(self):
        self.guests = list()


    def add(self, name, surname, age, country): #добавляем человечка с нужными нам параметрами(имя,фамилия,возраст,страна)
        self.guests.append({"guests_name": name,"guests_surname": surname, "guests_age": age, "guests_country": country})
    
    def udal(self, name): #тут удаляем человечка по нужному нам параметру, в данном случае у нас страна
        for guests in self.guests:
            if guests.get("guests_country") == country: 
                self.guests.remove(guests) 

    def zapis(self): #записываем всё в файлик
        import json
        with open("file1.json", 'a') as file:
            json_data = { "Guests": self.guests }
            file.write(json.dumps(json_data, indent=4))
            
if __name__ == "__main__":
    GuestBook = GuestBook()
    GuestBook.add("Ksenia", "Selivanova", 20, "Russia")
    GuestBook.add("Ktoto", "Esho", 25, "Russia")
    
    GuestBook.zapis()


# In[ ]:



