import requests
import json
from task1_2 import Role


class BadReq(Role):
    def __init__(self, *args, **kwargs):     # создаем список параметров
        super().__init__(*args, **kwargs)

    def check_bad(self, url):
        """
        Проверяем доступность по ссылке, ожидаем положительный ответ от сервера
        """
        resp = requests.get(url + str(self.role['id'])).status_code
        if resp == 200:                                                     # ошибка 403
            return 'Роль доступна по ссылке!'
        else:
            return f'{resp}!'

    def edit_bad_role(self, name='', type='', level=0):
        """
        Редактируем роль, функция требует ввода новых переменных
        :param name: str
        :param type: str
        :param level: int
        """
        role = json.dumps({'name': name, 'type': type, 'level': level, 'book': self.url_book})
        resp = requests.put(self.roles_url + str(self.role["id"]), role)    # убрал тип ожидаемых данных для заголовка, получаем ошибку 415
        self.role = resp
        self.name = name
        self.type = type
        self.level = level
        return self.role

#     def __str__(self):
#        return f"Имя: '{self.name}', Тип: '{self.type}', Уровень: {self.level}, Ссылка: '{self.url_role}'"


if __name__ == "__main__":
    r = BadReq(4, 'Martin', 56, 'SuperType', 20)
    print(r.add_role())
    print(r.check_bad('http://pulse-rest-testing.herokuapp.com/chooks/'))
    print(r.edit_bad_role('Jhon', 'LowType', 99))


