import requests
import json
from task1_1 import Book


class Role(Book):
    def __init__(self, title='', author='', name='', type='', level=0):     # создаем список параметров
        super().__init__(title, author)
        self.title = title
        self.author = author
        self.name = name
        self.type = type
        self.level = level
        self.roles_url = 'http://pulse-rest-testing.herokuapp.com/roles/'
        self.role = None
        self.url_role = None
        self.headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

    def add_role(self):
        """
        Добавляем роль, внутри функции преобразуем методом json,
        отдельно указываем формат данных заголовка, отдельно наследуем ссылку на книгу от предыдущего класса
        """
        role = json.dumps({'name': self.name, 'type': self.type, 'level': self.level, 'book': self.url_book})
        resp = requests.post(self.roles_url, role, headers=self.headers)
        self.role = resp.json()
        self.url_role = self.roles_url + str(self.role['id'])
        return self.role

    def check_url_role(self):
        """
        Проверяем доступность по ссылке, ожидаем положительный ответ от сервера
        """
        if requests.get(self.roles_url + str(self.role['id'])).status_code == 200:
            return 'Роль доступна по ссылке!'
        else:
            return 'Роли не существует!'

    def edit_role(self, name='', type='', level=0):
        """
        Редактируем роль, функция требует ввода новых переменных
        :param name: str
        :param type: str
        :param level: int
        """
        role = json.dumps({'name': name, 'type': type, 'level': level, 'book': self.url_book})
        resp = requests.put(self.roles_url + str(self.role["id"]), role, headers=self.headers)
        self.role = resp.json()
        self.name = name
        self.type = type
        self.level = level
        return self.role

    def check_data_role(self):
        """
        Проверяем наличие роли в списке, загружаем список всех ролей, преобразуем в список
        """
        all_data = requests.get(self.roles_url)
        all_data = all_data.json()
        if self.role in all_data:
            return 'Роль в списке!'
        else:
            return 'Роли нет в списке!'

    def del_role(self):
        """
        Делаем запрос на удаление, проверяем наличие роли в списке
        """
        requests.delete(self.roles_url + str(self.role["id"]))
        all_data = requests.get(self.roles_url)
        all_data = all_data.json()
        if self.role not in all_data:
            return 'Роль удалена!'

    def __str__(self):
        return f"Имя: '{self.name}', Тип: '{self.type}', Уровень: {self.level}, Ссылка: '{self.url_role}'"


if __name__ == "__main__":
    r = Role('Book2', 'Martin', 'Emilia Clark', 'SuperType', 20)
    print(r.add_role())
    print(r)
    print(r.edit_role('Jhon', 'LowType', 99))
    print(r.check_url_role())
    print(r.check_data_role())
    print(r.del_role())
