#определение функции
def hello():
    print('hello')

#вызов функции
hello()


#функция с аргументами
age = 28

def hello(name,age):
    print(f'Привет {name}, ты уже старый тебе {age} лет')

hello('Erik',age)


#Если мы хотим использовать результат выполнения функции мы прибегаем к ключевому слову return. Если функция не имеет оператора return то мы будет получать None

def minus(a,b):
    return a - b

a = minus(5,3)


#Сделайте калькулятор, у пользователя спрашиваете действие и спрашиваете 2 аргумента, затем реализуйте 4 функции на подсчет +-*/  и 1 функцию на сам калькулятор.

def sum_m(a,b):
    return a+b

def dig(a,b):
    return a-b

def mul(a,b):
    return a*b

def deg(a,b):
    if b == 0:
        return 'У тебя деление на 0, клоун'
    return a/b

def calc():
    d = input('1,2,3,4:')

    if d not in ['1','2','3','4']:
        print('Неверное действие')
        return
   
    a = int(input('число1'))
    b = int(input('число2'))

    if d == '1':
        result = sum_m(a,b)
    elif d == '2':
        result = dig(a,b)
    elif d == '3':
        result = mul(a,b)
    elif d == '4':
        result = deg(a,b)

    print(f'действие {d} : результат = {result}')

calc()


# Задача: Анализ трафика сайта
#Описание: вам необходимо проанализировать данные о посещении сайта за неделю. Вам дан список словарей, где каждый словарь представляет собой информацию о посетителе за один день:
#Напишите код на Python, который:
# Рассчитает общее количество посетителей за неделю.
# Рассчитает общее количество заказов за неделю.
# Определит день с наибольшим количеством посетителей.
# Определит день с наибольшим количеством заказов.
# Рассчитает среднее количество заказов на одного посетителя за неделю.

visits = [
{'date': '2024-10-27', 'visitors': 1500, 'orders': 50},
{'date': '2024-10-28', 'visitors': 1200, 'orders': 40},
{'date': '2024-10-29', 'visitors': 1800, 'orders': 60},
{'date': '2024-10-30', 'visitors': 1000, 'orders': 30},
{'date': '2024-10-31', 'visitors': 1600, 'orders': 55},
{'date': '2024-11-01', 'visitors': 2000, 'orders': 70},
{'date': '2024-11-02', 'visitors': 1400, 'orders': 45},
]

total_visits =  0
total_orders = 0
max_visit_day = None
max_order_day = None
max_visitors = 0
max_orders = 0

for i in visits:
    total_visits += i['visitors']
    total_orders += i['orders']

    if i['visitors'] > max_visitors:
        max_visit_day = i['date']
        max_visitors = i['visitors']

    if i['orders'] > max_orders:
        max_order_day = i['date']
        max_orders = i['orders']

avg_per = total_orders / total_visits

print(f'общее за неделю{total_visits}')
print(f'общее заказов за неделю {total_orders}')
print(f'день с > посетителей {max_visit_day}')
print(f'день с > заказов {max_order_day}')
print(f'{avg_per}')