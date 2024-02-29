from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating (Нет такого метода. Исправлен на существующий),
        # имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name, genre', [['Кэрри', 'Ужасы'], ['Винни Пух и все-все-все','Мультфильмы']])
    def test_set_book_genre_one_book_positive(self, book, name, genre):
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [['Кэрри', 'Ужасы'], ['Винни Пух и все-все-все','Мультфильмы']])
    def test_get_book_genre_one_book_positive(self, book, name, genre):
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_multiplication(self, book):
        book.add_new_book('Винни Пух и все-все-все')
        book.set_book_genre('Винни Пух и все-все-все', 'Мультфильмы')
        assert book.get_books_with_specific_genre('Мультфильмы') == ['Винни Пух и все-все-все']

    def test_get_books_for_children_book_is_for_child(self, book):
        book.add_new_book('Винни Пух и все-все-все')
        book.set_book_genre('Винни Пух и все-все-все', 'Мультфильмы')
        assert book.get_books_for_children() == ['Винни Пух и все-все-все']

    def test_get_books_for_children_book_is_adult(self,book):
        book.add_new_book('Кэрри')
        book.set_book_genre('Кэрри', 'Ужасы')
        assert book.get_books_for_children() == []

    def test_add_book_in_favorites_one_book_positive(self, book):
        book.add_new_book('Винни Пух и все-все-все')
        book.add_book_in_favorites('Винни Пух и все-все-все')
        assert book.get_list_of_favorites_books() == ['Винни Пух и все-все-все']

    def test_delete_book_from_favorites_one_book(self, book):
        book.add_new_book('Кэрри')
        book.add_book_in_favorites('Кэрри')
        book.delete_book_from_favorites('Кэрри')
        assert book.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_two_books(self, book):
        book.add_new_book('Винни Пух и все-все-все')
        book.add_new_book('Кэрри')
        book.add_book_in_favorites('Винни Пух и все-все-все')
        book.add_book_in_favorites('Кэрри')
        assert len(book.get_list_of_favorites_books()) == 2
