import pytest

import data
from main import BooksCollector

@pytest.fixture(scope='function')
def books_collector_with_books_genre():
    collector = BooksCollector()
    collector.books_genre[data.book_names[0]] = collector.genre[0]
    collector.books_genre[data.book_names[1]] = collector.genre[1]
    collector.books_genre[data.book_names[2]] = collector.genre[1]
    collector.books_genre[data.book_names[3]] = ''
    return collector

