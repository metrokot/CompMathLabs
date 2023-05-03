import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
def getNumber02(x, type):  # проверка на ввод числа
    while True:
        if type == 'int':
            try:
                getNumber = int(input('Введите ' + x))
                return getNumber
            except ValueError:
                print('Введите запись типа: ' + str(type))
        elif type == 'float':
            try:
                getNumber = float(input('Введите ' + x))
                return getNumber
            except ValueError:
                print('Введите запись типа: ' + str(type))
def dotsInput():# это уйдёт в грид ввод
   xy = []
   for i in range(getNumber02('количество точек','int')):
       xy.append((getNumber02(f'x_{i}','float'),getNumber02(f'y_{i}','float')))
   return xy

class MinSquares:
    dictMS = {'x': [], 'y': []}
    a, b = None, None # дописать
    def gauss(self): #как для матрицы 3/2 так и для 4/3
        pass
    def graphics(self,func):#возвращает график
        pass
    def lineMethod(self):#return lambda x: a*x+b
        pass
    def squareMethod(self):#return lambda x: a*(x**2)+a1*x+a2
        pass
    def __init__(self):# в будущем переделать на грид ввод
        self.dictMS['x'], self.dictMS['y'] = zip(*dotsInput())

