#Создание кортежей
my_tuple = ()
my_tuple = (1,2,3)
print(my_tuple)
my_tuple = 1,2,3
print(my_tuple)
my_tuple = (1,) #если 1 элемент обязательно запятая.
print(my_tuple)


#Методы:
my_tuple.count(2) # возвращает количество вхождений элементов x в кортеже
my_tuple.index(2) # возвращает индекс первого вхождения элемента в кортеже


#Функции:
len(my_tuple) # вернет количество элементов
min(my_tuple) # вернет минимальное
max(my_tuple) # вернет максимальное
sum(my_tuple) # вернет сумму
