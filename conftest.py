import pytest

from main import BooksCollector


@pytest.fixture
def book_name():
    book_name = BooksCollector(name='Кэрри')
    return book_name

@pytest.fixture
def book_genre():
    book_genre = BooksCollector(name = 'Винни Пух и все-все-все', genre = 'Мультфильмы')
    return book_genre
