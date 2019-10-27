f = open("update.txt", 'r', encoding='utf8')        # открываем исходный файл с тектом
f2 = open("f2.txt", 'w', encoding='utf8')
r = f.read().split()                                # вычитываем содержимое в виде списка
r.sort()
for i in r:                                         # заполняем новый файл элементами, подсчитывая их количество
    f2.write(f"{i}, количество: {r.count(i)}, \n")
f.close()
f2.close()
