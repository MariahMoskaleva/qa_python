import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def add_book(collector):
    name = 'Американский пирог'
    collector.add_new_book(name)
    return name
