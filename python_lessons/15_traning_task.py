#Генератор паролей
#Создайте функцию, которая генерирует случайный пароль заданной длины. Пароль должен содержать буквы (верхний и нижний регистр), цифры и специальные символы.

import random

def generate_pw(lenght):

    #определяю наборы
    low_let = 'abcdefghijklmnopqrstuvwxyz'
    up_let = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    digits = '0123456789'
    spec_chars = '!@#$%^&*'

    #объеденить все в 1 строку
    all_chars = low_let +up_let + digits + spec_chars

    #создам пустую строку для пароля
    pw = ''

    #генерирую пароль, добавляя случаные символы из all_chrs
    #если вам нужно сделать перебор циклом for при это вам не нужен сам i элемент, тогда вы можете поставить прокладку, пустое значеие через нижний _
    for _ in range(lenght):
        pw += random.choice(all_chars)

    return pw

print(generate_pw(12))



# Сортировка слов по длине
#Напишите функцию, которая принимает список слов и возвращает список слов, отсортированных по их длине.

def sort_words(words):
    sorted_words = sorted(words, key=len)
    return sorted_words

words = ['banana','eretik','asdhsujfiu','hjaheaha','123']

print(sort_words(words))



# Подсчет частоты слов
#Создайте функцию, которая принимает строку и возвращает словарь, где ключи — это слова, а значения — количество их вхождений в строке.

def count_word_freq(text):
    words = text.split()
    word_freq = {}

    for i in words:
        i = i.strip('.,!')
        i = i.lower()

        if i in word_freq:
            word_freq[i] +=1
        else:
            word_freq[i]  = 1
    return  word_freq

text = 'Это пример текста. Это текст, который мы будем анализировать! Это текст.'
print(count_word_freq(text))



# Проверка на палиндром
#Напишите функцию, которая проверяет, является ли строка палиндромом (читается одинаково слева направо и справа налево).

def is_palindrome(text):

    #удаляем пробелы и приводим строку к нижему регистру
    clean_text = text.replace(" ",'').lower()

    return clean_text == clean_text[::-1]

text1 = 'Привет, мир!'
text2 = 'А роза упала на лапу Азора'

print(is_palindrome(text1))
print(is_palindrome(text2))



# расчет стоимости доставки
#Задача: Напишите функцию, которая принимает вес посылки и расстояние доставки, а затем возвращает стоимость доставки. Стоимость доставки зависит от веса и расстояния:
#До 1 кг: 50 рублей за километр.
#От 1 до 5 кг: 70 рублей за километр.
#Более 5 кг: 100 рублей за километр.

def calculate_cost_shipping(weight,distance):
    if weight <=1:
        cost_per_km = 50
    elif weight <= 5:
        cost_per_km = 70
    else:
        cost_per_km = 100

    total_cost = cost_per_km * distance

    return total_cost

weight = 6
distance = 100

print(calculate_cost_shipping(weight,distance))



# Определение возраста по дате рождения
#Задача: Напишите функцию, которая принимает дату рождения (в формате YYYY-MM-DD) и возвращает возраст человека.

from datetime import datetime

def calc_age(birtdate):

    birtdate = datetime.strptime(birtdate, '%Y-%m-%d')
    totay = datetime.today()
    age = totay.year - birtdate.year

    if (totay.month, totay.day) < (birtdate.month, birtdate.day):
        age -=1
    return age

birtdate = '1996-08-22'

print(calc_age(birtdate))



# Подсчет гласных:
#Напишите функцию count_vowels(text), которая принимает на вход строку и возвращает количество гласных букв в ней

def count_volws(text):
    voluws = 'aeiouAEIOU'
    vowel_count = 0

    for i in text:
        if i in voluws:
            vowel_count+=1

    return vowel_count

text = 'hello world'
print(count_volws(text))


# Конвертер валют:
#Напишите программу, которая конвертирует валюту по заданному курсу. Пользователь должен вводить сумму, исходную валюту и целевую валюту, а программа должна выводить конвертированную сумму.
# Сумма: 100
# Исходная валюта: USD
# Целевая валюта: EUR
# Курс: 0.85
# Конвертированная сумма: 85 EUR

def convert_curr(amount,from_curr,to_curr,ex_rate):
    converter = amount * ex_rate

    return converter

amount = 100
from_curr = 'USD'
to_curr = 'RUB'
ex_rate = 0.85

print(convert_curr(amount,from_curr,to_curr,ex_rate))


# Счетчик времени:
#Напишите программу, которая позволяет пользователю установить таймер на определенное количество минут. По истечении времени программа должна выводить сообщение.

import time

def timer_set(minutes):
    seconds = minutes * 60

    print(f'таймер {minutes}')

    time.sleep(seconds)

    print('время вышло')

timer_set(1)



#Задача:
#Клиент пришел в ваш магазин и хочет купить товары на определенную сумму. Напишите код на Python, который:
# Спросит у клиента желаемую сумму для покупки.
# Предложит клиенту наиболее подходящий набор товаров, учитывая его бюджет и наличие товаров на складе.
# Выведет на экран список товаров из набора с их ценой и магическим эффектом.
# Рассчитает остаток денег у клиента после покупки.
# Если клиент не может купить ничего из-за недостатка денег или отсутствия товара на складе, выведите сообщение об этом.
#Дополнительные условия:
# Клиент может купить несколько единиц одного товара, если это возможно.
# Клиент может купить товары с разным магическим эффектом.
# Программа должна быть гибкой и учитывать разные цены и количество товаров на складе.

items = [
   {'name': 'Чародейский  Жезл', 'price': 1000, 'magic': 'Огненный  шар', 'stock': 3},
   {'name': 'Магический  Меч', 'price': 1500, 'magic': 'Ледяной  удар', 'stock': 2},
   {'name': 'Амулет  Невидимости', 'price': 500, 'magic': 'Невидимость', 'stock': 1},
   {'name': 'Книга  Заклинаний', 'price': 200, 'magic': 'Телепортация', 'stock': 5},
   {'name': 'Зелье  Силы', 'price': 300, 'magic': 'Увеличение  силы', 'stock': 10}, ]

budget = int(input('скок бабла у тебя ?'))
cart = []
remaning_buget = budget

while remaning_buget > 0:
    best_item = None

    for i in items:
        if i['stock'] >0 and i['price'] <= remaning_buget and (best_item is None or i['price'] > best_item['price']):
            best_item = i
   
    if best_item:
        cart.append(best_item)
        remaning_buget -= best_item['price']
        best_item['stock'] -= 1
    else:
        break

if cart:
    for i in cart:
        print(f'{i['name']}: {i['price']} золотых, {i['magic']}')
    print(f'осталось бабла {remaning_buget} ')
else:
    print('Сори но для тебя нет товаров.')




#Задачи:
#Проверка правильности email. Напишите функцию, которая проверяет правильность email-адреса.
#Email:
# Содержать только 1 @ 
# Иметь хотя бы 1 точку после @ 
# Содержать хотя бы одну букву до символа @ и хотя бы 1 букву после точки.

def valid_email(email):

    if email.count('@') != 1:

        return False

    local, domain = email.split('@')

    if len(local) == 0:
        return False

    if '.' not in domain:
        return False
   
    lst_dot_index = domain.rfind('.')

    if lst_dot_index == -1 or lst_dot_index == len(domain) -1:
        return False
   
    return True

print(valid_email('example@marin.ru')) #ture
print(valid_email('example@marinru')) #False
print(valid_email('examplemarin.ru')) #False
print(valid_email('@marin.ru')) #False
print(valid_email('asdasdsa@.marin.ru')) #True

# Если вставить точку сразу после знака собаки, то наша проверка провалится, потому что у нас есть 2 пункт проверки, который гласит что точка должна быть, после собаки, но не говорит, что она должна быть, после n к-во символов которые должны идти сразу за собакой.
#Фикс решение:

def valid_email(email):

    if email.count('@') != 1:
        return False

    local, domain = email.split('@')

    if len(local) == 0:
        return False

    if '.' not in domain or len(domain.split('.')[0]) == 0:
        return False
   
    lst_dot_index = domain.rfind('.')

    if lst_dot_index == -1 or lst_dot_index == len(domain) -1:
        return False
   
    return True

print(valid_email('example@marin.ru')) #ture
print(valid_email('example@marinru')) #False
print(valid_email('examplemarin.ru')) #False
print(valid_email('@marin.ru')) #False
print(valid_email('asdasdsa@.marin.ru')) #FAlse
print(valid_email('asdasdsa.@marin.ru')) #True


# Еще 1 фикс, при котором, у нас локал не может начинаться с точки и не может заканчиваться точкой

def valid_email(email):

    if email.count('@') != 1:
        return False

    local, domain = email.split('@')

    if len(local) == 0 or local[0] =='.' or local[-1] =='.':
        return False

    if '.' not in domain or len(domain.split('.')[0]) == 0:
        return False
   
    lst_dot_index = domain.rfind('.')

    if lst_dot_index == -1 or lst_dot_index == len(domain) -1:
        return False
   
    return True

print(valid_email('example@marin.ru')) #ture
print(valid_email('example@marinru')) #False
print(valid_email('examplemarin.ru')) #False
print(valid_email('@marin.ru')) #False
print(valid_email('asdasdsa@.marin.ru')) #FAlse
print(valid_email('asdasdsa.@marin.ru')) #False
print(valid_email('.asdasdsa@marin.ru')) #False



#Проверка что строка содержит только цифры и дефисы. Напишите функцию, которая проверяет что строка корректный номер телефона.
#Строка:
# Содержит только цифры и дефисы - 
# Не начинается и не заканчивается дефисом
# Дефисы не могут идти подряд
# дефис может быть а может и не быть 

def validate_phone(phone):
    if phone[0] == '-' or phone[-1] == '-':
        return False

    for i in range(len(phone)):
        char  = phone[i]

        # Проверяю что символ - это либо цифра либо дифис
        if not (char.isdigit() or char == '-'):
            return False
       
        #проверяю что дефисы не идут друг за другом
        if char == '-' and i > 0 and phone[i-1] == '-':
            return False
       
    return True

print(validate_phone('123-456-7890'))
print(validate_phone('1234567890'))
print(validate_phone('123-456-7890-'))
print(validate_phone('-123-456-7890'))
print(validate_phone('123-456--7890'))
print(validate_phone('123-456-789qwewq'))
