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
   xy = []
   for i in range(getNumber02('количество точек','int')):
       xy.append((getNumber02(f'x_{i}','float'),getNumber02(f'y_{i}','float')))
   return xy

class MinSquares:
    dictMS = {'x': [], 'y': []}
    a, b = None, None # дописать
    def func(self,x): return self.a*x+self.b
    def graphics(self):
        pass
    def lineMethod(self):
        print(f"y = {(a:= ((y := sum(self.dictMS['y'])) - (n := len(self.dictMS['x'])) * (b := ((sum(list(map(lambda x, y: x * y, self.dictMS['x'], self.dictMS['y'])))) - ((x2 := sum(list(map(lambda x: x ** 2, self.dictMS['x'])))) * y / (x := sum(self.dictMS['x'])))) / ((x - (x2 * n / x))))) / x)}x + {b}")

    def squareMethod(self):
        pass
    def __init__(self):

        self.dictMS['x'], self.dictMS['y'] = zip(*dotsInput())

