import matplotlib.pyplot as plt
import Gauss
from numpy import linspace


linear_dependence = lambda x,y: [[[sum(map(lambda x:x**2, x)), sum(x)], [sum(x), len(x)]], [sum(map(lambda x,y:x*y, x,y)), sum(y)]]


def quadratic_dependence(x, y):
    A = [[sum(map(lambda x:x**2,x)), sum(x), len(x)],
         [sum(map(lambda x: x ** 3, x)), sum(map(lambda x, y: x ** 2 * y, x, y)), sum(x)],
         [sum(map(lambda x: x ** 4, x)), sum(map(lambda x: x ** 3, x)), sum(map(lambda x:x**2,x))]]
    B = [sum(y), sum(map(lambda x,y: x *y, x,y)), sum(map(lambda x, y: x ** 2 * y, x, y))]
    return A, B


def graphic(_x, _y, c1, c2):
    x = linspace(min(_x),max(_x),100)
    plt.scatter(_x, _y, color='blue')
    plt.plot(x, list(map(lambda x:c1[0] * x + c1[1], x)), color='red')
    plt.plot(x, list(map(lambda x:c2[0] * x ** 2 + c2[1] * x + c2[2], x)), color='green')
    plt.title('Метод наименьших квадратов')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


#сумма квадратов отклонений исходных данных от линий
def result(_x, _y, c1, c2):
    print(f"погрешность от f1(x) = {(usl1:=sum(map(lambda x,y: (y - (x * c1[0] + c1[1])) ** 2, _x,_y)))} | погрешность от f2(x) = {(usl2:=sum(map(lambda x, y: (y - (x ** 2 * c2[0] + c2[1] * x + c2[2])) ** 2, _x, _y)))}")
    if usl1 > usl2:
        print(f'''Так как погрешность f2(x) < f1(x), то прямая y = a1*x^2 + a2*x + a3 лучше приближает исходные данные
        Среднеквадратичная погрешность равна: {usl2 / len(_x)}''')
    else:
        print(f'''Так как погрешность f1(x) < f2(x), то прямая y = a*x + b лучше приближает исходные данные
        Среднеквадратичная погрешность равна: {usl1 / len(_x)}''')

# исходные данные
x = [2.358, 2.787, 2.738, 2.758, 2.315, 2.728, 2.426, 2.958, 2.178, 2.006]
y = [1.026, 1.823, 1.888, 1.957, 1.126, 1.990, 1.069, 2.569, 1.028, 0.908]

A1, B1 = linear_dependence(x, y)
A2, B2 = quadratic_dependence(x, y)

print("Линейная функция")
c_1 = Gauss.Gauss(A1, B1).GaussMethod()
print(dict(zip(['a1','a2'], c_1)))

print("\nКвадратичная функция")
c_2 = Gauss.Gauss(A2, B2).GaussMethod()
print(dict(zip(['a1','a2','a3'], c_2)))
graphic(x, y, c_1, c_2)
result(x, y, c_1, c_2)