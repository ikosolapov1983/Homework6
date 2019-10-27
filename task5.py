f = open("table.txt", 'r', encoding='utf8')
r = [line.split() for line in f]                                # создаем список из строк
d = dict.fromkeys([r[0][0], r[0][1], r[0][2], r[0][3]])         # используем первую строку для создания ключей
# Заполняем базу данных
data = []
for i in range(len(r)):
    if i > 0:
        d['Фамилия'] = r[i][0]
        d['Имя'] = r[i][1]
        d['Отдел'] = r[i][2]
        d['Зарплата'] = int(r[i][3])
        data.append(d.copy())
# подсчитываем количество отделов
department = []
for i in data:
    if i['Отдел'] not in department:
        department.append(i['Отдел'])
print('Количество отделов:', len(department))
# находим максимальную зарплату
org_salary = []
for i in data:
    org_salary.append(i['Зарплата'])
print('Максимальная зарплата в организации:', max(org_salary))
# ищем максимальную зарплату в каждом отделе
data_salary = dict.fromkeys(department, 0)
for i in data:
    for j in data_salary:
        if j == i['Отдел'] and data_salary[j] < i['Зарплата']:
            data_salary[j] = i['Зарплата']
for k, v in data_salary.items():
    print(f'Максимальная зарплата в отделе "{k}": {v}')
# выводим человека с максимальной зарплатой в файл
f2 = open("MAX_SALARY.txt", 'w', encoding='utf8')
for i in data:
    if i['Зарплата'] == max(org_salary):
        f2.write(f"Отдел: {i['Отдел']}, Зарплата: {i['Зарплата']}, Фамилия: {i['Фамилия']}")
f2 = open("MAX_SALARY.txt", 'r', encoding='utf8')
r = f2.read()
print(r)
f.close()
f2.close()
