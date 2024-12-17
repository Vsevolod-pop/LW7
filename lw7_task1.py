from random import *
M = input('Введите число М для генерациии матрицы MxM - ')
while True:
    try:
        if M[0] == '-' or M[0] == '0':
            raise Exception
        M = int(M)
    except Exception:
        M = input('Введенное число некорректно. Введите целое положительное число М для генерациии матрицы MxM - ')
    else:
        break
a=[]
for i in range(M):
    a.append([])
    for j in range(M):
        a[i].append(0)
for i in range(M):
    for j in range(M):
        a[i][j] = randint(-9999999999999, 9999999999999)
min = 99999999999999
if M == 1:
    print('Матрица имеет вид 1х1. У нее не существует никаких диагоналей, соответсвенно наименьший элемент ниже побочной диагонали не существует.')
else:
    for i in range(1,len(a)):
        A = len(a)-1-i
        for j in range(A+1,len(a)):
            if a[i][j] < min:
                min = a[i][j]
    print(*a, sep ='\n')
    print(min)