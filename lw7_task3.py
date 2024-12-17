n = input('Введите количество учеников - ')
while True:
    try:
        if n[0] == '-' or n[0] == '0':
            raise Exception
        n = int(n)
    except Exception:
        n = input('Введенное число некорректно. Введите целое положительное число n  - ')
    else:
        break
dict = {}
for i in range(n):
    average = 0
    sname = input('Введите фамилию ученика - ')
    while True:
        try:
            if sname.isalpha() == False:
                raise Exception
        except Exception:
            sname = input('Введенные данные не корректны. Введите верно фамилию ученика - ')
        else:
            break
    M = input('Введите результат первого теста - ')
    while True:
        try:
            int(M)
            if 0 > int(M) or int(M) > 100 or '00' in M[:2] or '-00' in M[:3]:
                raise Exception
        except Exception:
            M = input('Введенное число некорректно. Введите результата теста в диапазоне от 0 до 100 - ')
        else:
            M = int(M)
            break
    N = input('Введите результат второго теста - ')
    while True:
        try:
            int(N)
            if 0 > int(N) or int(N) > 100 or '00' in N[:2] or '-00' in N[:3]:
                raise Exception
        except Exception:
            N = input('Введенное число некорректно. Введите результата теста в диапазоне от 0 до 100 - ')
        else:
            N = int(N)
            break
    K = input('Введите результат третьего теста - ')
    while True:
        try:
            int(K)
            if 0 > int(K) or int(K) > 100 or '00' in K[:2] or '-00' in K[:3]:
                raise Exception
        except Exception:
            K = input('Введенное число некорректно. Введите результата теста в диапазоне от 0 до 100 - ')
        else:
            K = int(K)
            break
    average = (M+N+K)/3
    dict[sname] = average
dict = sorted(dict.items(), key= lambda item: item[1], reverse=True)
print (*dict, sep='\n')