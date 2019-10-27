import requests
import json


class Book:
    def __init__(self, title='', author=''):     # создаем список параметров
        self.title = title
        self.author = author

    def add_book(self):
        return json.dumps({'title': self.title, 'author': self.author})

    def __str__(self):
        return f'{self.book}'
#        for k in self.book:
#            return f"Книга: '{self.book['title']}', Автор: '{self.book['author']}'"


if __name__ == "__main__":
    b = Book('Book 1', 'Oliver Just')
    print(b.add_book())
    url = 'http://pulse-rest-testing.herokuapp.com/books/'
    response = requests.post(url, b.add_book())             # создаем книгу
    book_data = response.json()
    print(book_data)
    response = requests.get(url + str(book_data['id']))     # проверяем наличие книги
    print(response.json())
    all_data_book = requests.get(url)                       # получаем список всех существующих книг
    all_data_book = all_data_book.json()
    if book_data in all_data_book:
        print('Книга в списке!')
    else:
        print('Книга не существует!')
    b2 = Book('Just Book 2', 'Oliver Junior Just')
    response = requests.put(url + str(book_data["id"]), b2.add_book())
    book_data = response.json()
    response = requests.get(url + str(book_data["id"]))          # проверяем наличие книги
    print(response.json())
    all_data_book = requests.get(url)                            # получаем список всех существующих книг
    all_data_book = all_data_book.json()
    if book_data in all_data_book:
        print('Книга в списке!')
    else:
        print('Книга не существует!')
    response = requests.delete(url + str(book_data["id"]))
    all_data_book = requests.get(url)
    all_data_book = all_data_book.json()
    if book_data not in all_data_book:
        print('Книга удалена')
