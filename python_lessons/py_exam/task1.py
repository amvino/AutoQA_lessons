people = [
   {"name": "Alice", "age": 28, "city": "New York", "profession": "Engineer", "skill_level": "Advanced"},
   {"name": "Bob", "age": 32, "city": "San Francisco", "profession": "Designer", "skill_level": "Intermediate"},
   {"name": "Charlie", "age": 25, "city": "Chicago", "profession": "Developer", "skill_level": "Beginner"},
   {"name": "David", "age": 30, "city": "Los Angeles", "profession": "Data Scientist", "skill_level": "Advanced"},
   {"name": "Eve", "age": 27, "city": "Seattle", "profession": "Product Manager", "skill_level": "Intermediate"},
   {"name": "Frank", "age": 40, "city": "Boston", "profession": "Engineer", "skill_level": "Advanced"},
   {"name": "Grace", "age": 35, "city": "Austin", "profession": "Designer", "skill_level": "Beginner"},
   {"name": "Hannah", "age": 29, "city": "Chicago", "profession": "Developer", "skill_level": "Intermediate"},
   {"name": "Ivan", "age": 26, "city": "Denver", "profession": "Engineer", "skill_level": "Beginner"},
   {"name": "Jack", "age": 33, "city": "San Diego", "profession": "Product Manager", "skill_level": "Advanced"},
   {"name": "Kim", "age": 31, "city": "Miami", "profession": "Data Scientist", "skill_level": "Intermediate"},
   {"name": "Liam", "age": 24, "city": "Houston", "profession": "Developer", "skill_level": "Beginner"},
   {"name": "Mia", "age": 29, "city": "Phoenix", "profession": "Engineer", "skill_level": "Intermediate"},
   {"name": "Noah", "age": 28, "city": "Philadelphia", "profession": "Designer", "skill_level": "Advanced"},
   {"name": "Olivia", "age": 27, "city": "Dallas", "profession": "Product Manager", "skill_level": "Beginner"}
]


neo = []

for human in people:
    if human['city'] != "Chicago" and human['city'] != "Los Angeles" and human['profession'] == "Engineer" and human["skill_level"] == "Advanced" and human["age"] <= 30:
        neo.append(human)

if len(neo) == 1:    
    print(f'Избранный: {neo}')
elif len(neo) > 1:
    print(f'Под условия подходит несколько сотрудников:')
    for i in neo:
        print(f' {i}')
else:
    print(f'Нет такого человека')



