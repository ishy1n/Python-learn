#задачи ТГУ
def get_day(i):
    return [31,28,31,30,31,30,31,31,30,31,30,31] [int(i)-1]
st = input()
n = []
n.append(st[9])
if st[9] in "1234567890":
    n.append(st[10])
    m = n[0]+n[1]
    print(get_day(m))
else:
    m = n[0]
    print(get_day(m))

#Игра накорми кота
k_sleep, k_eat, k_play, k_purr = 10, 10, 10, 10
while choice != 'q':
    print(f'Настроение: {k_purr}')
    print(f'Еда: {k_eat}')
    print(f'Сон: {k_sleep}')
    print(f'Игра: {k_play}')
    print('Выберите действие:')
    print('1 - Покормить')
    print('2 - Поиграть')
    print('3 - Поспать')
    print('4 - Погладить')
    print('q - Выход')
    choice = input()
    if choice == '1':
        k_eat += 10
        k_sleep -= 5
        k_play -= 5
        k_purr -= 5
    elif choice == '2':
        k_eat -= 5
        k_sleep -= 5
        k_play += 10
        k_purr -= 5
    elif choice == '3':
        k_eat -= 5
        k_sleep += 10
        k_play -= 5
        k_purr -= 5
    elif choice == '4':
        k_eat -= 5
        k_sleep -= 5
        k_play -= 5
        k_purr += 10


#Работа с файлами, палиндром
with open('lines.txt', encoding='UTF-8') as files:
    words = files.read().split()
    words = list(filter(lambda x: x.isalpha(), words))
    filter_result = list(filter(lambda name: name == name[::-1], words))
    print(len(filter_result))


#умножение матриц
import numpy as np
A = np.array([[3, 4, 5],
    [1, 2, 3],
    [8, 9, 3]])
B = np.array([[2, 5, 9],
    [8, 0, 4],
    [12, 0, 3]])
C = np.dot(A, B)
print(A)
print(B)
print(C)
#вывод времяни каждую минуту
import time
import datetime

now_minute = datetime.datetime.now().minute
while True:
    now = datetime.datetime.now()
    if now.minute != now_minute:
        print(now.strftime('%H:%M'))
        now_minute = now.minute
    time.sleep(1)
