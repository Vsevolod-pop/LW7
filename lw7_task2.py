from random import *
M = input('Введите число строк М - ')
while True:
    try:
        if M[0] == '-' or M[0] == '0':
            raise Exception
        M = int(M)
    except Exception:
        M = input('Введенное число некорректно. Введите целое положительное число М - ')
    else:
        break
N = input('Введите число столбцов N - ')
while True:
    try:
        if N[0] == '-' or N[0] == '0':
            raise Exception
        N = int(N)
    except Exception:
        N = input('Введенное число некорректно. Введите целое положительное число N - ')
    else:
        break
a=[]
for i in range(M):
    a.append([])
    for j in range(N):
        a[i].append(0)
        a[i][j] = randint(-100, 100)
b=[]
count = 0
for i in range(0, N, 2):
    b.append([])
    for y in range(M):
        b[count].append(a[y][i])
    count += 1
print(*a, sep='\n')
print()
print(*b, sep='\n')