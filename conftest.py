import pytest

from main import BooksCollector


@pytest.fixture(scope="session")
def collector():
    return BooksCollector()


@pytest.fixture
def add_book(collector):
    name = 'Американский пирог'
    collector.add_new_book(name)
    return name


@pytest.fixture
def set_comedy_genre_for_book(collector, add_book):
    genre = 'Комедии'
    collector.set_book_genre(add_book, genre)
    return genre


@pytest.fixture
def add_book_for_adults(collector):
    name = 'Убийство в восточном экспрессе'
    collector.add_new_book(name)
    collector.set_book_genre(name, 'Детективы')
    return name
