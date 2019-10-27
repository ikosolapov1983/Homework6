from la_song import la

f = open("la.txt", 'w')                 # открываем на запись файл
p = la(s=3, count=3, z=0)
f.write(p)
f.close()

f = open(r"C:\Git\Homework5\task1_1.py", 'r', encoding='utf8')      # находим файл с кодом
r = f.read()
print(r)
f.close()

f = open(r"C:\Git\Homework5\task1_1.py", 'r', encoding='utf8')
f2 = open("f2.txt", 'w')
number = 0
for line in f:
    number += 1
    f2.write(f"{number}: {line.rstrip()}, \n")                  # из первого файла копируем строку с переносом
f.close()
f2.close()

f = open("update.txt", 'r', encoding='utf8')
r = f.read().split()
print(r)
for i in r:                                                     # пытаемся каждый элемент списка преобразовать
    try:
        i = int(i)
    except Exception:
        pass
    else:
        print(f"Я сделал это! ==> {i}")
    finally:
        f.close()





