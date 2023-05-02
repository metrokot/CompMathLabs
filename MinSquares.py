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
def dotsInput():
   x,y = [],[]
   for i in range(getNumber02('количество точек','int')):
       x,y = getNumber02(f'x_{i}','float'),getNumber02(f'y_{i}','float')
   return x, y

class MinSquares:
    def graphics(self):
        pass
    def gaussMethod(self):
        pass
    def __init__(self):
        x,y = input()
