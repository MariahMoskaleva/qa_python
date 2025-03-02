import pytest

from main import BooksCollector


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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('genre_name, expected_result', [
        ('Комедии', True),
        ('Романтика', False)
    ], ids=['Valid genre', 'Invalid genre'])
    def test_set_book_genre(self, collector, add_book, genre_name, expected_result):
        collector.set_book_genre(add_book, genre_name)
        actual_result = collector.get_books_genre().get(add_book) == genre_name
        assert expected_result == actual_result

    @pytest.mark.parametrize('genre_name, expected_result', [
        ('Комедии', True),
        ('Ужасы', False)
    ], ids=['Genre of existing book', 'Genre of nonexistent book'])
    def test_get_book_genre(self, collector, add_book, set_comedy_genre_for_book, genre_name, expected_result):
        actual_result = collector.get_book_genre(add_book) == genre_name
        assert actual_result == expected_result

    @pytest.mark.parametrize('genre_name, expected_result', [
        ('Комедии', ['Американский пирог']),
        ('Ужасы', [])
    ], ids=['Added books of given genre', 'Did not add books of given genre'])
    def test_get_books_with_specific_genre(self, collector, add_book, set_comedy_genre_for_book, genre_name,
                                           expected_result):
        actual_result = collector.get_books_with_specific_genre(genre_name)
        assert actual_result == expected_result

    @pytest.mark.parametrize('book_name, expected_result', [
        ('Американский пирог', True),
        ('Заклятие', False)
    ], ids=['Added book with given name', 'Did not add book with given name'])
    def test_get_books_genre(self, collector, add_book, set_comedy_genre_for_book, book_name, expected_result):
        actual_result = book_name in collector.get_books_genre()
        assert actual_result == expected_result

    def test_get_books_for_children_one_comedy_book(self, collector, add_book, set_comedy_genre_for_book,
                                                    add_book_for_adults):
        assert add_book in collector.get_books_for_children() and add_book_for_adults not in collector.get_books_for_children()

    @pytest.mark.parametrize('name, expected_result', [
        ('Американский пирог', True),
        ('Заклятие', False)
    ], ids=['Book with given name exists', 'Book with given name doesnt exist'])
    def test_add_book_in_favorites(self, collector, add_book, set_comedy_genre_for_book, name, expected_result):
        collector.add_book_in_favorites(add_book)
        actual_result = name in collector.get_list_of_favorites_books()
        assert actual_result == expected_result

    def test_add_book_in_favorites_double_book_adds_once(self, collector, add_book, set_comedy_genre_for_book):
        collector.add_book_in_favorites(add_book)
        collector.add_book_in_favorites(add_book)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_book_deletes(self, collector, add_book, set_comedy_genre_for_book):
        collector.add_book_in_favorites(add_book)
        collector.delete_book_from_favorites(add_book)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books(self, collector, add_book, set_comedy_genre_for_book):
        collector.add_book_in_favorites(add_book)
        assert len(collector.get_list_of_favorites_books()) == 1 and add_book in collector.get_list_of_favorites_books()