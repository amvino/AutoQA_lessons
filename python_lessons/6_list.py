#Метод append(x) - добавляет элемент x в список.

lst = [1,2,3]
lst.append(5)
print(lst) #1,2,3,5

#Метод extend(x) - добавляет элементы объекта в конец списка.

lst = [1,2,3]
lst2 = [4,5,6]
lst.extend(lst2)
print(lst) #[1,2,3,4,5,6]

#Метод insert(i, x) - Вставляет элемент x на позицию i (index)

lst  = [1,2,3]
lst.insert(2,10)
print(lst) # [1,2,10,3]

#Метод remove(x) - удаляет первый элемент равный x. Если элемент не найден, вызовет исключение(ошибка) valueError

lst  = [1,2,3]
lst.remove(2)
print(lst) #[1,3]

#Метод pop(i) - удаляет и возвращает элемент на позиции i(по умолчанию последний)

lst  = [1,2,3]
lst.pop()
print(lst) #[1,2]
lst.pop(0)
print(lst) #[2]

#Метод clear() - метод удаляет все элементы списка

lst  = [1,2,3]
lst.clear()
print(lst) #[]

#Метод index(x[start,end]) - возвращает индекс первого вхождения элемента x в диапазоне. Если элемент не найден исключение valueError

lst  = [1,2,3,2]
print(lst.index(2)) #результат 1
print(lst.index(2,2)) #результат 3

#Метод count(x) - общее к-во элементов x в списке

lst  = [1,2,3,2]
print(lst.count(2)) #2

#Метод sort() - сортирует список, можно добавить ключ reverse чтобы выполнить сортировку . По умолчанию сортировка идёт по возрастанию

lst  = [3,5,10,15,1,9,2]
lst.sort()
print(lst) #[1,2,3,9,10,15]
lst.sort(reverse=True)
print(lst) #[15, 10, 9, 5, 3, 2, 1]

#Метод reverse() - переворачивает список на месте

lst  = [3,5,10,15,1,9,2]
lst.reverse()
print(lst) #[2, 9, 1, 15, 10, 5, 3]

#Метод copy() - возвращает поверхностный вариант копии списка

lst  = [3,5,10,15,1,9,2]
b = lst.copy()
b.append(4)
print(lst)
print(b)


#Функция len(list)  - вернет длину списка

lst  = [3,5,10,15,1,9,2]
print(len(lst))

#Функция max(list),min(list) - вернет максимальное и минимальное значение в списке

lst  = [3,5,10,15,1,9,2]
print(max(lst)) #15
print(min(lst)) #1

#Функция sum(list) - вернет сумму элемента списка

lst  = [3,5,10,15,1,9,2]
print(sum(lst)) #45

#Функция sorted() - вернет новый отсортированный список из элементов. Есть параметры reverse аналогичные методу sort

lst  = [3,5,10,15,1,9,2]
b = sorted(lst)
print(b)
c = sorted(lst, reverse=True)
print(c)

#Функция  list() преобразует объект в список

a = (1,2,3)
b = list(a)
print(b)


#Задачи
#Объедините 2 строки. s1 = ‘произвольный текст’ s2 = ‘произвольный текст’ 

s1 = 'произвольный текст'
s2 = 'произвольный текст'
result = s1+' '+s2
print(result)


#Извлеките подстроку is  из строки ‘python is awesome’

s1 = 'python is awesome'
print(s1[7:9])


#Объедините 2 списка (произвольных)

lst = [1,2,3]
lst2 = [4,5,6]
print(lst+lst2)


#Извлеките из списка (произвольного) все элементы с 4 по 8(не включительно)

lst = [1,2,3,1,2,3,1,2,3,1,2,3]
print(lst[4:8])


#Вам надо создать систему управления библиотекой.Система должна позволять добавлять книги, удалять, искать по названию и выводить список всех книг. Каждая книга представлена в виде строки, содержащей название книги.
#Требования:
#Используйте списки для хранения книг
#Используйте методы строк для обработки
#Используйте методы списков для управления
#Используйте if-elif-else для обработки команд.
#Команды:
#add <название книги> - добавить книгу
#remove <название книги> - удалить книгу
#find <название книги> - найти книгу
#list - вывести все книги
#exit - вывести сообщение о выходе из системы.
#add python programming

#Решение:

library = ['pytthon prog','google prog','ozon prog']
command = input('Введите команду: ').strip()
parts = command.split(maxsplit=1)
action = parts[0]

if action == 'add':
    if len(parts) <2:
        print('не укзано название книги')
    else:
        book_title = parts[1].strip()
        if book_title in library:
            print(f'Книга {book_title} уже есть в библиотеке')
        else:
            library.append(book_title)
            print(f'Книга {book_title} добавлена библиотеке')
            print(library)
elif action == 'remove':
    if len(parts) < 2:
        print('Не указано название книги.')
    else:
        book_title = parts[1].strip()
        if book_title in library:
            library.remove(book_title)
            print(f'Книга {book_title} удалена')
            print(library)
        else:
            print('книга не найдена')
elif action == 'find':
    if len(parts) < 2:
        print('Не указано название книги.')
    else:
        book_title = parts[1].strip()
        if book_title in library:
            print(f'Книга {book_title} найдена ')
        else:
            print('книга не найдена')
elif action == 'list':
    if len(library) == 0:
        print('билбиотека пустая')
    else:
        print('списко книг')
        print(library)

        # затравка наперед,красивый вывод
        for i, book in enumerate(library,start=1):
            print(f'{i}. {book}')
elif action == 'exit':
    print('выход из системы')
else:
    print('неизвестаня комана')  
