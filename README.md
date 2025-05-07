# qa_python

`test_default_value_books_genre` - проверка дефолтного значения словаря books_genre

`test_default_value_favorites` - проверка дефолтного значения списка favorites

`test_default_value_genre` - проверка дефолтного значения списка genre

`test_default_value_genre_age_rating` - проверка дефолтного значения списка genre_age_rating

`test_add_new_book_success` - проверка на добавление новой книги в словарь, при валидном количестве символов в названии

`test_add_new_book_characters_len_exceeded` - проверка на добавление новой книги в словарь, при невалидном количестве символов в названии

`test_set_book_genre_success` - проверка на добавление жанра в словарь books_genre, при условии, что книга содержится в book_genre  и жанр содержится в genre

`test_get_book_genre_success` - проверка на получение жанра по названию книги

`test_get_books_with_specific_genre_success` - проверка на получение всех книг указанного жанра из словаря

`test_get_books_genre_with_books_and_genre` - проверка на получение текущего состояния словаря books_genre

`test_get_books_for_children_success` - проверка на получение списка книг без возрастных ограничений

`test_add_book_in_favorites_one_book_success` - проверка на добавление книги в избранное

`test_delete_book_from_favorites_one_book_success` - проверка на удаление книги из избранного

`test_get_list_of_favorites_books_success` - проверка на получение списка избранных книг

`test_get_list_of_favorites_books_zero_books` - проверка на получение списка избранных книг, если в список пустой
