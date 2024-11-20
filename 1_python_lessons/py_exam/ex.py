#Задание 1:
#Есть список людей, тебе надо найти избранного. Вы — детектив в крупной компании и вам поручили найти "избранного" сотрудника, которого компания хочет наградить за выдающиеся достижения. У вас есть некоторые намеки, которые помогут отыскать этого человека. Каждый сотрудник компании описан в виде словаря со следующими параметрами: name, age, city, profession, skill_level.
#Подсказки:
# Этот человек работает в крупном городе, но точно не в Чикаго и не в Лос-Анджелесе.
# Он(а) — инженер с высоким уровнем мастерства, но не старше 30 лет.
# Возраст сотрудника совпадает с количеством дней, которое требуется для доставки посылки из Нью-Йорка в Сан-Франциско. (там не так много данных,  по этому эту подсказку я записал просто так , а может и не просто так, а может и…)

#Решение:



#Задание 2:
#Представьте, что вы работаете в отделе управления складом, и ваша задача — объединить два списка товаров. Однако, при объединении есть несколько условий, которые необходимо соблюдать, чтобы списки корректно объединились.
#У вас есть два списка:
# Список_А — содержит названия товаров, которые уже находятся на складе.
# Список_Б — содержит названия товаров, которые поступят на склад.
#Требования и условия объединения:
# Удаление дубликатов: Если товар есть в обоих списках, он должен быть записан только один раз.
# Проверка пустых значений: Товары с пустым названием (например, пустые строки "" или значения None) не должны быть добавлены в итоговый список.
# Сортировка: В конце объединённый список нужно отсортировать в алфавитном порядке для удобства.
#Итоговый список: После объединения всех товаров, выведите итоговый список товаров на складе.

#Решение:



#Задание 3:
#Вы — сотрудник отдела контроля качества в интернет-магазине. Ваша задача — проверить, что все заказы в системе соответствуют определённым критериям. Заказы представлены в виде списка словарей, и каждый заказ должен соответствовать следующим условиям:
# ID заказа должен быть уникальным числом больше 0.
# Статус заказа должен быть “оплачен”, “в обработке”, или “отменен”.
# Сумма заказа должна быть больше 0.
# Покупатель — имя покупателя (строка), не может быть пустым.
# Если хотя бы одно из этих условий нарушено, такой заказ считается не прошедшим проверку.
#Написать функцию validate_orders(orders), которая принимает список заказов и проверяет каждый из них на соответствие условиям.
#Если заказ не прошел проверку, выводить сообщение с описанием проблемы и ID заказа.
#Вернуть список всех заказов, которые прошли проверку.

#Решение:



#Задание 4 
#Создать программу, которая генерирует тестовые данные для регистрации пользователей. Необходимо сгенерировать список из 20 пользователей с различными комбинациями полей, которые могут быть использованы для тестирования:
# Имя (Name) — строка длиной от 3 до 20 символов, состоящая из букв и пробелов.
# Электронная почта (Email) — строка, которая соответствует формату электронной почты (например, "user@example.com").
# Пароль (Password) — строка, длина которой от 8 до 16 символов, должна содержать хотя бы одну цифру, одну заглавную и одну строчную букву.
# Дата рождения (Date of Birth) — случайная дата в пределах с 01.01.1980 по 31.12.2000.
# Статус (Status) — случайное значение из списка: ["active", "inactive", "banned"].
# Адрес (Address) — случайная строка длиной от 10 до 40 символов, содержащая буквы и цифры.

#Решение:

import random
from datetime import datetime, timedelta

statused = ['active','inactive','banned']


def generate_name():
    first_name = ['Олег','Никита','Эрик','Клоун']
    last_name = ['Амазингович','Человекович','Нечеловекович']

    return random.choice(first_name) + " " + random.choice(last_name)


def generate_dob():
    start_date = datetime(1980,1,1)
    end_date = datetime(2000,12,31)
    delta = end_date - start_date
    random_date = start_date + timedelta(days=random.randint(0,delta.days))

    return random_date.strftime('%Y-%m-%d')


def generate_email(name):
    domains = ['example.com','test.com','mail.ru','yahoo.com']
    name_part = name.replace(' ','').lower()
    domain = random.choice(domains)

    return f'{name_part}@{domain}'


def generate_pw():
    while True:
        pw = ''.join(random.choices('asdasdajdhejrhewjkfweuwfwrptreQWUIEHQWJRHWEJIFHSIUHFEWUFJH1231273812', k=random.randint(8,16)))

        if any(c.isdigit() for c in pw) and any(c.islower() for c in pw) and any(c.isupper() for c in pw):

            return pw


def generate_adres():
    streets = ['Ул Ленина','Ул моя','ул дарта вейдера']
    house_number = [str(random.randint(1,100)),str(random.randint(101,999))]
    
    return f'{random.choice(streets)}{random.choice(house_number)}'


def generate_user_dataset(num_user=20):
    users = []

    for _ in range(num_user):
        name = generate_name()
        email = generate_email(name)
        pw = generate_pw()
        dob = generate_dob()
        status = random.choice(statused)
        address = generate_adres()
        user = {
            'name': name,
            'email': email,
            'pw': pw,
            'dob': dob,
            'status': status,
            'address': address }
        users.append(user)

    return users

user_data = generate_user_dataset(20)

for i in user_data:
    print(i)



#Решение с помощью 2 модулей 

import random
import string
from faker import Faker

fake = Faker('ru_RU')


def generate_pw():
    while True:
        pw = ''.join(random.choices(string.ascii_letters+ string.digits, k=random.randint(8,16)))

        if any(c.isdigit() for c in pw) and any(c.islower() for c in pw) and any(c.isupper() for c in pw):

            return pw


def generate_user_dataset(num_users=20):
    users = []
    for _ in range(num_users):
        name = fake.name()
        email = fake.email()
        pw = generate_pw()
        dob = fake.date_of_birth(minimum_age=18,maximum_age=44).strftime('%Y-%m-%d')
        status = random.choice(['active','inactive','banned'])
        address = fake.address().replace('\n',' ')
        user = {
            'name': name,
            'email': email,
            'pw': pw,
            'dob': dob,
            'status': status,
            'address': address }
        users.append(user)

    return users

user_d = generate_user_dataset(20)

for i in user_d:
    print(i)
