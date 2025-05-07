import pytest

import data
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_default_value_books_genre(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_default_value_favorites(self):
        collector = BooksCollector()
        assert collector.favorites == []

    def test_default_value_genre(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_default_value_genre_age_rating(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_success(self):
        collector = BooksCollector()
        collector.add_new_book(data.book_names[0])
        assert collector.books_genre[data.book_names[0]] == ''

    @pytest.mark.parametrize('name', ['Длинноватое название книги из 41 символа!',''])
    def test_add_new_book_characters_len_exceeded(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre == {}

    def test_set_book_genre_success(self, books_collector_with_books_genre):
        genre = books_collector_with_books_genre.genre[0]
        name = data.book_names[3]
        books_collector_with_books_genre.set_book_genre(name, genre)
        assert books_collector_with_books_genre.books_genre[name] == genre

    def test_get_book_genre_success(self, books_collector_with_books_genre):
        assert books_collector_with_books_genre.get_book_genre(data.book_names[0]) == books_collector_with_books_genre.genre[0]

    def test_get_books_with_specific_genre_success(self,books_collector_with_books_genre):
        genre = books_collector_with_books_genre.genre[1]
        books_list = books_collector_with_books_genre.get_books_with_specific_genre(genre)
        assert books_list == [data.book_names[1], data.book_names[2]]

    def test_get_books_genre_with_books_and_genre(self,books_collector_with_books_genre):
        assert books_collector_with_books_genre.get_books_genre() == books_collector_with_books_genre.books_genre

    def test_get_books_for_children_success(self, books_collector_with_books_genre):
        assert books_collector_with_books_genre.get_books_for_children() == [data.book_names[0]]

    def test_add_book_in_favorites_one_book_success(self, books_collector_with_books_genre):
        books_collector_with_books_genre.add_book_in_favorites(data.book_names[0])
        assert books_collector_with_books_genre.favorites == [data.book_names[0]]

    def test_delete_book_from_favorites_one_book_success(self, books_collector_with_books_genre):
        books_collector_with_books_genre.favorites = [data.book_names[0]]
        books_collector_with_books_genre.delete_book_from_favorites(data.book_names[0])
        assert books_collector_with_books_genre.favorites == []

    def test_get_list_of_favorites_books_success(self, books_collector_with_books_genre):
        books_collector_with_books_genre.favorites = [data.book_names[0], data.book_names[1]]
        actual_list = books_collector_with_books_genre.get_list_of_favorites_books()
        assert actual_list == [data.book_names[0], data.book_names[1]]

    def test_get_list_of_favorites_books_zero_books(self, books_collector_with_books_genre):
        actual_list = books_collector_with_books_genre.get_list_of_favorites_books()
        assert actual_list == []