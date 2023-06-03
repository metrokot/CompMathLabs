import math

def parasha(m,n):
    p, h, t = int((3 * 26 + 1) / (26 + 2)), 1 / 5, 1 / 5
    u1, u2 = [[0.0] * (n + 1)] * (m + 1), [[0.0] * 2] * (m + 1)
    u2[m - 1][1] = 1
    for i in range(m+1):
        for j in range(n + 1):
            if j==0 and i>0 and i<m: u1[i][j] = p*math.sin(math.pi*(i*h))
            else: u1[i][j] = 0
    for i in range(1,m):
        for j in range(1,n + 1):
            u1[i][j] = (u1[i-1][j-1] - 2*u1[i][j-1]+u1[i+1][j-1])*t/(h*h) + u1[i][j-1]
            if (j*t)==0.2: u2[i][0],u2[i][1] = u2[i][j],i*h
    for i in range(m):
        print(f'''
        {u2[i][0]:-f}\t{u2[i][1]:-f}
        тут не понимаю вывод 
    ''')
parasha(5,80)
parasha(10,80)
parasha(10,250)
