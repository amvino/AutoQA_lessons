#При работе с циклом while нам всегда нужен какой-то счетчик, или оператор break, иначе наш цикл всегда будет выполняться. Тут в качестве счетчика используется переменная i чтобы выйти из цикла.

i = 0
while i <= 5:
    print(i)
    i+=1


#Если у вас, по логике вашей программы, не предусмотрен выход по счетчику, или же есть вариант выхода при условии каком-то, вы также можете использовать оператор break

i = 0
while i <= 5:
    print(i)
    i+=1
    if i == 3:
        break


#Также как и в цикле for мы можем использовать continue для пропуска итерации.

i = 0
while i < 5:
    i+=1
    if i == 3:
        continue
    print(i)


#Если зачем-то вам нужен else то тоже можете его добавить по аналогии  с for. Блок else - выполняется, когда условие цикла становится ложным.

i = 0
while i < 5:
    i+=1
    if i == 3:
        continue
    print(i)
else:
    print('конец')


#Пример использования цикла while и удаление дубликатов

my_lst = [1,1,1,2,2,2,3,3,3,3,3]
seen = set()
i = 0
while i < len(my_lst):
    if my_lst[i] in seen:
        del my_lst[i]
    else:
        seen.add(my_lst[i])
        i+=1
print(my_lst)


#Посчитайте к-во дней до того как я умру. У вас есть n сумма и вы хотите знать, сколько дней, мне надо есть доширак пока не получу зарплату.Каждый день, вы тратите определенную сумму на доширак, и хотите узнать, когда закончатся деньги. Вывод на экран к-во дней , через которое закончатся деньги.

money = 1000
minus_cash = 50
days = 0

while money > 0:
    money -= minus_cash
    days+=1
print(days)


#Создать игру угадать число, от 1 до 100. Число которое загадывает компьютер вы записываете ручками. И также нужно ограничить к-во попыток пользователю до 6. При этом при каждом ответе пользователя говорить ему, число которое он записал, больше или меньше числа которое загадал компьютер.

secret_num = 55
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


#Посчитайте среднее значение скидочных позиций. Нужно посчитать средний скидочный элемент, на основе тех скидок на товары которые вы вводите, ввод будет до тех пор пока не введете специальную команду для выхода и подсчета. -1

discounts = []
while True:
    discount = int(input())
    if discount == -1:
        break
    discounts.append(discount)

if len(discounts) == 0:
    print('не ввел скидки')

else:
    avg_disc = sum(discounts) / len(discounts)
    print(avg_disc)

#вариант 2

sum_disc = 0
count_disc = 0

while True:
    discount = int(input())
    if discount == -1:
        break
    sum_disc += discount
    count_disc +=1

if count_disc == 0:
    print('не ввел скидки')

else:
    avg_disc = sum_disc / count_disc
    print(avg_disc)


#Вам требуется создать программу управления бюджетом на месяц. Вы будете вводить расходы, доходы, а затем будет программа подсчитывать остаток денег на конец месяца. Вы можете вводить доходы и расходы до тех пор пока не напишите команду  завершить. В конец еще сделать проверку на положительный остаток 

poluchil = []
potratil = []

while True:
    action = input('доход,расход,завершить')
    if action == 'завершить':
        break
    sums = int(input('сумма:'))

    if action == 'доход':
        poluchil.append(sums)   
    elif action == 'расход':
        potratil.append(sums)
    else:
        print('неккоректное действие')

all_do = sum(poluchil)
all_ra = sum(potratil)
ost = all_do - all_ra

print(all_do)
print(all_ra)
print(ost)

if ost > 0:
    print('У ва есьт деньги')
elif ost <0:
    print('ты без бабла')
else:
    print('Этебя ровно 0')