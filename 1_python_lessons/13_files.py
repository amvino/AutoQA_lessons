 #Для работы с файлом его нужно открыть. Делается это с помощью функции open(). После завершения работы с файлом его надо обязательно закрыть close()

#Для чтения файла
#read() считывает весь файл в одну строку
#readline() считывает только одну строку за раз
#readlines() считывает все строки из файла и возвращает их в виде списка.

#Для записи используйте write()
#Ключи для работы с файлами:
#r- (только чтение)
#w- (запись)
#a-(добавление)
#x-(создание но только если файл существует)

file = open('exm.txt','r')
content = file.read()
print(content)
file.close()

#Для автоматического закрытия файла можно использовать конструкцию with

with open('exm.txt','r') as file:
    data = file.read()
    print(data)



#Задача:
#Есть файл с текстом. Мне надо найти все Рэдрик в этом тексте и выпить их в список.
#Ошибка:
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 1761: character maps to <undefined>

with open('exm.txt','r') as file:
    content = file.read()
    matches = []
    index = content.find('Рэдрик')
    
    while index != -1:
        matches.append(content[index:index+len("Рэдрик")])
        index = content.find('Рэдрик', index+len("Рэдрик"))

    if matches:
        for i in matches:
            print(i)

#Ошибка была в кодировке
with open('exm.txt','r',encoding='utf-8') as file:
    content = file.read()
    matches = []
    index = content.find('Рэдрик')

    while index != -1:
        matches.append(content[index:index+len("Рэдрик")])
        index = content.find('Рэдрик', index+len("Рэдрик"))

    if matches:
        for i in matches:
            print(i)
