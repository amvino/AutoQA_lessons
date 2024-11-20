#Основные функции модуля re:

# re.match(pattern,string) (В НАЧАЛЕ СТРОКИ) Проверяет, подходит ли строка string под шаблон pattern. Возвращает объект Match при совпадении в начале строки и None в противном случае.

import re

result = re.match(r'\d+','123abc')

if result:
    print(result.group()) #123


# re.search(pattern, string) Находит первое совпадение pattern в строке string ( в любом месте строки, а не только в начале) Возвращает объект Match или None

import re

result = re.search(r'\d+','123abc')

if result:
    print(result.group()) #123


#  re.findall(pattern, string) Возвращает все совпадения pattern в строке string и возвращает их в виде списка.

import re

result = re.findall(r'\d+','abc123def456')

print(result) #['123','456']


# re.finditer(pattern, string) Возвращает итератор  с объектами Match для всех совпадений

import re

result = re.finditer(r'\d+','abc123def456')

for match in result:
    print(match.group()) #'123','456'


# re.sub(pattern, repl, string) Заменяет все совпадения pattern в строке string на repl

import re

result = re.sub(r'\d+','#','abc123def456')

print(result)


#Специальные символы и метасимволы

# . - любой символ, кроме новой строки
# ^ - начало строки.
# $ - конец строки
# \d - любая цифра[0-9]
# \D - любой символ кроме цифры.
# \w - любой алфавитно-цифровой символ (буквы, цифры,_)
# \W - любой символ, кроме алфавитно-цифрового
# \s - любой пробельный символ (пробел, табуляция, новая строка)
# \S - любой символ кроме пробельного


#Квантификаторы 

# *  - 0 или более повторений
# + - 1 или более повторений
# ? - 0 или 1 повторение
# {n} - ровно n повторений
# {n,} - n или более повторений
# {n,m} от n до m повторений


#Группы и обратные ссылки:

#Группы позволяют нам захватывать части совпадений, которые затем можно использовать или обрабатывать

# (...) - захватывающая группа. Результат можно получить через group()
# (?: …) - не захваченная группа. Используется для группировки без сохранения.



#Примеры регулярных выражений:

#Проверка email 

import re

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
result   = re.match(pattern,'example@mail.ru')

print(bool(result)) #true



# re.compile() - для удобства и повышения некой производительности, регулярные выражения можно компилировать через compile() чтобы использовать один и тот же шаблон несколько раз.

import re

pattern = re.compile(r'\d+')
result1 = pattern.search('abs123')
result2 = pattern.search('def456')

print(result1,result2)
print(result1.group(),result2.group())



#Решение задачи для email через регулярные выражения:

import re

def valid_email(email):

    pattern = r'^[A-Za-z0-9](?!.*\.\.)[A-Za-z0-9._%+-]*[A-Za-z0-9]@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+$'

    return bool(re.match(pattern,email))

print(valid_email('example@marin.ru')) #ture
print(valid_email('example@marinru')) #False
print(valid_email('examplemarin.ru')) #False
print(valid_email('@marin.ru')) #False
print(valid_email('asdasdsa@.marin.ru')) #FAlse
print(valid_email('asdasdsa.@marin.ru')) #False
print(valid_email('.asdasdsa@marin.ru')) #False


# ^[A-Za-z0-9] - локальная часть начинается с буквы или цифры
# (?!.*\.\.) - запрет на две точки подряд
# [A-Za-z0-9._%+-]*[A-Za-z0-9] - локальная часть может содержать буквы, цифры и разрешенные символы, но не может начинаться и заканчиваться точкой.
# @[A-Za-z0-9-]+ - домен начинается с буквы или цифры, но не с точки.
# (\.[A-Za-z]{2,})+$ - домен верхнего уровня, состоит из точки, за которой следует минимум две буквы.



#Задача на телефон с тире через регулярки:

import re

def validate_phone(phone):

    pattern = r'^(?!-)(?!.*--)[0-9-]+(?<!-)$'

    return bool(re.match(pattern,phone))


print(validate_phone('123-456-7890'))
print(validate_phone('1234567890'))
print(validate_phone('123-456-7890-'))
print(validate_phone('-123-456-7890'))
print(validate_phone('123-456--7890'))



# ^(?!-) - строка не должна начинаться с дефиса
# (?!.*--) - строка не должна содержать два дефиса подряд
# [0-9-]+ - строка должна содержать только цифры и дефисы.
# (?<!-)$ - строка не должна заканчиваться дефисом.



#Разница в re.search vs re.match

import re

text = 'The price is 100 dollars'
match_result = re.match(r'\d+',text)

print(match_result) #выдает None потому что цифры не в начале строки


serch_resul = re.search(r'\d+', text)

print(serch_resul.group()) #100 так как находит по всему.




# Написать программу
# Спросит у пользователя жанр сказки, который он хочет прочитать.
# Найдет все сказки данного жанра.
# Отсортирует сказки по рейтингу (от самого высокого к самому низкому).
# Выведет список названий сказок, отсортированных по рейтингу, в формате:

fairy_tales = [
 {'title': 'Красная Шапочка', 'author': 'Шарль Перро', 'genre': 'Народная', 'year': 1697, 'rating': 4.5},
 {'title': 'Спящая Красавица', 'author': 'Шарль Перро', 'genre': 'Народная', 'year': 1697, 'rating': 4.0},
 {'title': 'Золушка', 'author': 'Шарль Перро', 'genre': 'Народная', 'year': 1697, 'rating': 4.8},
 {'title': 'Принцесса на горошине', 'author': 'Ганс Христиан Андерсен', 'genre': 'Народная', 'year': 1835, 'rating': 4.2},
 {'title': 'Русалочка', 'author': 'Ганс Христиан Андерсен', 'genre': 'Фантастика', 'year': 1837, 'rating': 4.9},
 {'title': 'Дюймовочка', 'author': 'Ганс Христиан Андерсен', 'genre': 'Фантастика', 'year': 1835, 'rating': 4.7},
]

des_gen = input('Введите жанр:')
filter_tales = []

for i in fairy_tales:
    if i['genre'].lower() == des_gen.lower():
        filter_tales.append(i)

for i in range(len(filter_tales)):
    for j in range(i+1,len(filter_tales)):
        if filter_tales[i]['rating'] < filter_tales[j]['rating']:
            filter_tales[i], filter_tales[j] = filter_tales[j], filter_tales[i]

for i in filter_tales:
    print(f'-{i['title']} рейтинг {i['rating']}')
