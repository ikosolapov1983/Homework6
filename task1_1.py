import requests
import json


class Book:
    def __init__(self, title='', author=''):     # создаем список параметров
        self.title = title
        self.author = author
        self.books_url = 'http://pulse-rest-testing.herokuapp.com/books/'
        self.book = None
        self.url_book = None
        self.headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        self.add_book()

    def add_book(self):
        """
        Добавляем книгу, внутри функции преобразуем методом json,
        отдельно указываем формат данных заголовка
        """
        book = json.dumps({'title': self.title, 'author': self.author})
        resp = requests.post(self.books_url, book, headers=self.headers)
        self.book = resp.json()
        self.url_book = self.books_url + str(self.book['id'])
        return self.book

    def check_url_book(self):
        """
        Проверяем доступность по ссылке, ожидаем положительный ответ от сервера
        """
        if requests.get(self.books_url + str(self.book['id'])).status_code == 200:
            return 'Книга доступна по ссылке!'
        else:
            return 'Книга не существует!'

    def edit_book(self, title='', author=''):
        """
        Редактируем книгу, функция требует ввода новых переменных
        :param title: str
        :param author: str
        """
        book = json.dumps({'title': title, 'author': author})
        resp = requests.put(self.books_url + str(self.book["id"]), book, headers=self.headers)
        self.book = resp.json()
        self.title = title
        self.author = author
        return self.book

    def check_data_book(self):
        """
        Проверяем наличие книги в списке, загружаем список всех книг, преобразуем в список
        """
        all_data = requests.get(self.books_url)
        all_data = all_data.json()
        if self.book in all_data:
            return 'Книга в списке!'
        else:
            return 'Книги нет в списке!'

    def del_book(self):
        """
        Делаем запрос на удаление, проверяем наличие книги в списке
        """
        requests.delete(self.books_url + str(self.book["id"]))
        all_data = requests.get(self.books_url)
        all_data = all_data.json()
        if self.book not in all_data:
            return 'Книга удалена!'

    def __str__(self):
        return f"Книга: '{self.title}', Автор: '{self.author}, Ссылка: '{self.url_book}'"


if __name__ == "__main__":
    b = Book('Book 1', 'Oliver Just')
    print(b.add_book())
    print(b)
    print(b.edit_book('Book2', 'Oliver Mr'))
    print(b.del_book())
    print(b.check_url_book())
    print(b.check_data_book())
