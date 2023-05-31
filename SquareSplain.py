import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# определяем функцию для вычисления значения кубического сплайна
def S(x_):
    i = 0
    while i < Lenght - 1 and x_ > x[i + 1]:
        i += 1
    if i == Lenght - 1:
        i -= 1
    t = x_ - x[i]
    return y[i] + b[i] * t + c[i] * t ** 2 + d[i] * t ** 3

x = [4.302, 4.381, 4.626, 4.886, 4.808, 4.872, 4.382, 4.181, 4.483, 4.418]
y = [5.861, 6.212, 2.868, 2.647, 6.198, 3.499, 3.529, 6.511, 5.955, 4.185]

Lenght = len(x)

# Сортируем значения x и y
sorted_indices = np.argsort(x)
x = [x[i] for i in sorted_indices]
y = [y[i] for i in sorted_indices]
N = 6

d = {'x': x, 'f(x)':y}
df = pd.DataFrame(data=d)
df.to_string(index=False)
print(df)

h = np.zeros(Lenght - 1)
alpha = np.zeros(Lenght - 1)
InterK1 = np.zeros(Lenght)
InterK2 = np.zeros(Lenght)
InterK3 = np.zeros(Lenght)
c = np.zeros(Lenght)
b = np.zeros(Lenght - 1)
d = np.zeros(Lenght - 1)

for i in range(Lenght - 1):
    h[i] = x[i + 1] - x[i]

for i in range(1, Lenght - 1):
    alpha[i] = (3 / h[i]) * (y[i + 1] - y[i]) - (3 / h[i - 1]) * (y[i] - y[i - 1])

# Метод прогонки
InterK1[0] = 1
InterK2[0] = 0
InterK3[0] = 0

# прямой ход
for i in range(1, Lenght - 1):
    InterK1[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * InterK2[i - 1]
    InterK2[i] = h[i] / InterK1[i]
    InterK3[i] = (alpha[i] - h[i - 1] * InterK3[i - 1]) / InterK1[i]

InterK1[Lenght - 1] = 1
InterK3[Lenght - 1] = 0
c[Lenght - 1] = 0

# обратный ход
for j in range(Lenght - 2, -1, -1):
    c[j] = InterK3[j] - InterK2[j] * c[j + 1]
    b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
    d[j] = (c[j + 1] - c[j]) / (3 * h[j])


print("Матрица:")

# создаем диагональную матрицу
dM = np.diag(np.round(InterK1, 3))

# создаем матрицы с смещением от главной диагонали
upp = np.diagflat(np.round(InterK3[:-1], 3), 1)
down = np.diagflat(np.round(InterK2[1:], 3), -1)

# складываем 3 матрицы
matrix = dM + upp + down

df = pd.DataFrame(matrix)

# задаем столбцы и строки
df.columns = [f'col{i + 1}' for i in range(df.shape[1])]
df.index = [f'row{i + 1}' for i in range(df.shape[0])]

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
# выводим dataframe
print(df)
print("Коэффициенты кубического сплайна:")
for i in range(Lenght - 1):print(
       "S{6}(x) = {0:.3f} + {1:.3f}(x - {2:.3f}) + {3:.3f} (x - {2})^2 + {4:.3f} (x - {2:.3f})^3 = {5:.3f}".format(y[i],b[i],x[i],c[i],d[i],S(x[i]),i+1))

# задаем интервал для построения графика
x_vals = np.linspace(min(x), max(x), 1000)
# строим график точек и кубического сплайна
plt.scatter(x, y, color='red', label='Заданные точки')
plt.plot(x_vals, list(map(S,x_vals)), label='Кубический сплайн')
plt.xlabel('x')
plt.ylabel('y')

# выводим график
plt.show()