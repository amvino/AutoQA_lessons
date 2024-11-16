#Допустим, У нас есть игра, угадай число, нам надо сделать так, чтобы число задумывалось случайным образом в диапазоне.
#Для этого используем модуль random

import random

secret_num = random.randint(1,100)
count = 0
suc_yep = False

while not (suc_yep):
    count +=1
    p = int(input('Тут пиши число:'))

    if p == secret_num:
        suc_yep =True
    elif p < secret_num:
        print('Друг число больше')
    else:
        print('друг число меньше')

print(f'вы угадал {secret_num} за {count} попыток')


#Задачи:
#Выведите на экран текущую дату и время, а также количество дней до нового года.

import datetime

now = datetime.datetime.now()
next_year = now.year +1
new_year = datetime.datetime(next_year,1,1)
time_to_new_yaer = new_year - now

print(now)
print(time_to_new_yaer)