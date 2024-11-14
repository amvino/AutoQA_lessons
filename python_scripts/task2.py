sklad = [1,2,3]
lst = [4,5,6]

for i in lst:
    if i is not None and i != '' and i not in sklad :
        sklad.extend(lst)

sklad.sort()

for i in sklad:
    print(f'{i}')


