from main import BooksCollector
import pytest


@pytest.fixture()
def book():
    book = BooksCollector()

    return book


