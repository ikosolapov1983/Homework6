from la_song import la

with open("la.txt", 'w') as f:
    p = la(s=3, count=3, z=0)
    f.write(p)

with open(r"C:\Git\Homework5\task1_1.py", 'r', encoding='utf8') as f:
    r = f.read()
    print(r)

with open(r"C:\Git\Homework5\task1_1.py", 'r', encoding='utf8') as f:
    f2 = open("f2.txt", 'w')
    number = 0
    for line in f:
        number += 1
        f2.write(f"{number}: {line.rstrip()}, \n")

with open("update.txt", 'r', encoding='utf8') as f:
    r = f.read().split()
    print(r)
    for i in r:
        try:
            i = int(i)
        except Exception:
            pass
        else:
            print(f"Я сделал это! ==> {i}")
        finally:
            f.close()
