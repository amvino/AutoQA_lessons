
#Индексация

a = 'world'
print(a[0]) #выведет w
print(a[4]) #выведет d

s = 'Hello, World!'
print(s[1:4]) #ваш ответ ell
print(s[:5]) #Hello
print(s[7:]) #World!
print(s[::2]) #Hlo ol!
print(s[::-1]) #!dlroW ,olleH
print(s[2:8:2]) #lo


#Конкатенация и повторение

s = 'Hello'
s2 = 'world'
print(s + s2) #Helloworld
print(s*5) #HelloHelloHelloHelloHello
# print(s * s2) #будет ошибка


#Методы lower() и upper()

s = 'Team Spirit'
print(s.lower()) #team spirit
print(s.upper()) #TEAM SPIRIT


#Методы strip(), lstrip(), rstrip()

s = '      Team Spirit--------'
print(s)
print(s.strip()) #удаляет пробелы указанные в начале и в конце строки.
print(s.lstrip()) #удаляет пробелы указанные в начале строки
print(s.rstrip()) #удаляет пробелы указанные в конце строки.
print(s.strip('-')) #удаляет символы "-"


#Методы split(sep, maxsplit)

s = 'apple,banana,yabloko'
print(s.split()) #['apple,banana,yabloko']
print(s.split(',')) #['apple', 'banana', 'yabloko']
print(s.split(',',maxsplit=1)) #['apple', 'banana,yabloko']


#Метод join (iterable)

words = ['hello','world']
print(''.join(words)) # 'hello world'
print('-'.join(words)) # 'hello-world'


#Методы find() , index()

s = 'Hello, World!'
print(s.find('o')) #вернет 4
print(s.find('я')) #вернет -1
print(s.index('o')) #вернет 4
#print(s.index('я')) #упадет с ошибкой valueError


#Метод replace()

words = 'Hello, World!'
words.replace('W','E')
print(words) #выведет 'Hello, World!' потому что неизменяемая строка
print(words.replace('W','E')) #тут заменит W на E потому что я не изменяю строку, а меняю вывод. Сама строка без изменний.


#Методы isalpha(), isdigit(), isalnum(), isspace()

print('Hello'.isalpha()) #True если все символы - буквы
print('123'.isdigit()) #True если все символы - цифры
print('123qwe'.isalnum()) #True если все символы - буквы или цифры
print('      '.isspace()) #True если все символы - пробелы


#Функция len()

a = '123456789'
print(len(a))
