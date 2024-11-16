#Создание множеств

my_set = set() #пустое множество
print(my_set)
my_set = {1,2,3} #множество с элементами
print(my_set)
my_set = set([1,2,3]) #множество из списка
print(my_set)


#Методы:

#add(element) -  добавляет элемент в множество.
my_set.add(6)
print(my_set)

#remove(element) - удаляет элемент из множества. Если не найдет, выдаст ошибку keYError
my_set.remove(3)
print(my_set)

#discard(element) - удаляет элемент, если элемент не найден, то ничего не происходит.
my_set.discard(10)
print(my_set)

#pop() - удаляет и возвращает произвольный элемент из множества, если множество пустое, вернет keyError
pop_el = my_set.pop()
print(pop_el) #выведет произвольный элемент
print(my_set) #множество без этого элемента

#clear() - удаляет все элементы
my_set.clear()
print(my_set)

#union(other_set) - вернет новое множество, содержащее в себе все элементы из обоих множеств.
set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
print(union_set)

#intersection(other_set) - вернет новое множество, содержащее элементы общие обоих множеств.

#difference(other_set) - вернет новое множество, содержащее элементы первого, которых нет во 2.

#symetric_difference(other_set) - вернет новое множество, содержащее элементы которые есть в одном, но не в обоих.

#issubset(other_set) - вернет True если все элементы первого множества есть во 2.

#issuperset(other_set) - вернет True Если все элементы второго множества содержатся в первом.


#Функция:
len(my_set) # вернет к-во элементов в множестве.
my_set = {1,2,3,4,5}