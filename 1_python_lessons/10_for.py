fruits = ['Банан','Апельсин','груша']
for fruit in fruits:
    print(fruit)

fruits = 'фрукты'
for fruit in fruits:
    print(fruit)

person = {'name':'erik','age':25,'city':'NYC'}

#итерация по ключам
for key in person:
    print(key)

#терация по значению
for value in person.values():
    print(value)

#итерация по парам
for key, value in person.items():
    print(f'{key}: {value}')


#Функция range() - генерирует последовательность чисел, которую можно использовать в цикле ‘for’ Функция range позволяет указать не только конец, но и начало и шаг. range(start,stop,step)

for i in range(10):
    print(i)

for i in range(0,10,2):
    print(i)


#Циклы как условия могут быть вложенными, для обработки более сложных структур данных.

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9] ]

for i in matrix:
    for j in i:
        print(j)


#Функция zip() объединяет элементы из нескольких итерируемых объектов в кортежи.

names = ['erik','alice','blick']
ages = [28,25,29]

for name,age in zip(names,ages):   
    print(f'{name} is {age} years old')


#Оператор break используется для прерывания цикла досрочно.

for i in range(10):
    if i == 5:
        break
    print(i)


#Оператор continue используется для пропуска текущей итерации и перехода к следующей

for i in range(10):
    if i == 5:
       continue
    print(i)


#У цикла for есть возможность выполнить блок else если он вам нужен. Сработает ( только если вы не использовали break) и если цикл завершился нормально.

for i in range(10):
    print(i)
else:
    print("Цикл завершен")


#Решение задач:
#Сумма элементов списка (функцию sum использовать нельзя)

nums = [1,2,3,4,5]
total = 0

for i in nums:
    total +=i
print(total)


#Напишите программу которая посчитает количество гласных букв в строке.

text = 'Hello World'
volwes = 'aeiouAEIOU'
count  = 0

for i in text:
    if i in volwes:
        count +=1
print(count)


#Напечатайте таблицу умножения в формате 1 * 1 = 1……..

for i in range(1,11):
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')
    print()


#Поиск максимального элемента в списке (без функции MAX) чисто перебором

nums = [3,6,8,9,4,6,12]
max_nums = nums[0]

for i in nums:
    if i > max_nums:
        max_nums = i
print(max_nums)


#Создать произвольный список и написать программу, которая фильтрует список, оставляя только четные числа.

nums = [3,6,8,9,4,6,12]
even_nums = []

for i in nums:
    if i % 2 ==0:
        even_nums.append(i)
print(even_nums)
 

# Объединить 2 списка в словарь.

st1 = ['ale','mole','tole']
st2 = [1,2,3]
st3 = {}

for name,age in zip(st1,st2):
    st3[name] = age
print(st3)


#Преобразовать строку в список и подсчитать частоту каждого слова (знаки препинания удалять при обработке строки)

str1 = 'Python is a powerful programming language. Python is also easy to learn.'
words = str1.split()
word_count = {}

for i in words:
    i = i.strip('.,!').lower()

for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
print(word_count)


#Преобразовать список кортежей в словарь.

a = [('elik','belik'),('net','da')]
dcitr = dict(a)
print(dcitr)


# Уникальные символы в строках. Есть список строк, надо найти все уникальные символы которые есть во всех строчках.

strings = ['hello','word','world','python','programming']
uniq_chars = set(strings[0])

for i in strings[1:]:
    uniq_chars.intersection_update(i)
print(uniq_chars)


#Группировка слов по первой букве. У вас есть список слов, надо написать программу, которая группирует их по первой букве и возвращает словарь, где ключами являются первые буквы а значениями список слов, начинающихся с этой буквы.

words = ['apple','banana','dragon','cherry','avocado','blueberry']
words_group = {}
#группировка символов
for i in words:
    first_letter = i[0]
    if first_letter in words_group:
        words_group[first_letter].append(i)
    else:
        words_group[first_letter] = [i]
print(words_group)


#Посчитать сумму всех нечетных элементов.
#считаем у цифр

nums = [1,2,3,4,5,6] #9
sum_odd = 0

for i in nums:
    if i % 2 != 0:
        sum_odd += i
print(sum_odd)
#считаем нечетные индексы
nums = [1,2,3,4,5,6] #12
sum_odd = 0

for i in range(1,len(nums),2):
    sum_odd +=nums[i]
print(sum_odd)


#Удалить дубликаты из списка (сделать 2 решения, 1 через if 2 через сами догадаетесь что ))

#Без удаления - создавая новый список:
nums = [1,1,2,2,3,3,4,5,6,7,8,9,9,9,9,9]
uniq_el = []

for i in nums:
    if i not in uniq_el:
        uniq_el.append(i)
print(uniq_el)

#Через set()
nums = [1,1,2,2,3,3,4,5,6,7,8,9,9,9,9,9]
like = set(nums)
print(like)

#Прямо удаляем дубликаты используя цикл for
my_lst = [1,1,1,2,2,2,3,3,3,3,3]
seen = set()

for i in range(len(my_lst) - 1,-1,-1):
    if my_lst[i] in seen:
        del my_lst[i]
    else:
        seen.add(my_lst[i])
print(my_lst)


#len(my_lst) -1  - это начало последовательности - последний индекс списка (потому что у нас индексация начинается с 0)
#-1 - это конец последовательности - индекс до первого элемента (не включительно)
#-1 - это шаг последовательности - уменьшение на 1 при каждом шаге.


#Посчитать сумму элементов в матрице используя только циклы и условия без встроенных функций	

a = [
[1,2,3],
[4,5,6],
[7,8,9]
]
sum_total = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        sum_total += a[i][j]
print(sum_total)


#НАписать программу которая проверяет надежность пароля. Пароль считается надежным, если: 
#Его длина больше 8 символов
#Если содержит хотя бы 1 заглавную,1 строчную , 1 цифру .
#Решение:

pw = input()
h_upper = False
h_lower = False
h_digit = False

if len(pw) <8:
    print('пароль короткий')
else:
    for i in pw:
        if i.isupper():
            h_upper = True
        elif i.islower():
            h_lower = True
        elif i.isdigit():
            h_digit = True
       
    if h_digit and h_lower and h_upper:
        print('надежный')
    else:
        print('Пароль недостаточно надежный')
