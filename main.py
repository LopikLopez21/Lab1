from Json import Json_Input_Output
from Books import Library, Psychology_books, Math_books, Literature_books, Science_books


def input_number(n):  # Валидация + обработка своей ошибки
    while True:
        try:
            count = int(input(n))
            if count <= 0:
                raise ValueError
            return count
            break
        except ValueError:
            print("Пожалуйста, введите положительное число.")
# Вывод информации
def output_inf(inf):
    print("\nДанные из JSON:")

    print("\nКниги по математике:")
    for book in inf['math_books']:
        print(f"Название: {book['name']}, Количество: {book['count']} шт., Автор: {book['author']}")

    print("\nКниги по психологии:")
    for book in inf['psychology_books']:
        print(f"Название: {book['name']}, Количество: {book['count']} шт., Автор: {book['author']}")

    print("\nКниги по литературе:")
    for book in inf['literature_books']:
        print(f"Название: {book['name']}, Количество: {book['count']} шт., Автор: {book['author']}")

    print("\nКниги по науке:")
    for book in inf['science_books']:
        print(f"Название: {book['name']}, Количество: {book['count']} шт., Автор: {book['author']}")


def main():
    books_from_json = Json_Input_Output.output_from_json("books.json")  # читаем и закидываем туда данные

    while True:

        choice = input("\nВыберите действие:\n"
                       "1. Добавить книги по математике\n"
                       "2. Добавить книги по литературе\n"
                       "3. Добавить книги по науке\n"
                       "4. Добавить книги по психологии\n"
                       "5. Сохранить в JSON\n"
                       "6. Читать из JSON\n"
                       "7. Выход\n")

        if choice == '1':
            name = input("Введите название книги: ")
            count = input_number("Введите количество: ")
            author = input("Введите имя автора книги: ")
            math_book = Math_books(name, count, author)
            Json_Input_Output.add_math_books(books_from_json, math_book)

        elif choice == '2':
            name = input("Введите название книги: ")
            count = input_number("Введите количество: ")
            author = input("Введите имя автора книги: ")
            literature_book = Literature_books(name, count, author)
            Json_Input_Output.add_math_books(books_from_json, literature_book)

        elif choice == '3':
            name = input("Введите название книги: ")
            count = input_number("Введите количество: ")
            author = input("Введите имя автора книги: ")
            science_book = Science_books(name, count, author)
            Json_Input_Output.add_math_books(books_from_json, science_book)

        elif choice == '4':
            name = input("Введите название книги: ")
            count = input_number("Введите количество: ")
            author = input("Введите имя автора книги: ")
            psychology_book = Psychology_books(name, count, author)
            Json_Input_Output.add_math_books(books_from_json, psychology_book)

        elif choice == '5':
            Json_Input_Output.input_to_json(books_from_json, "books.json")
            print(f"Данные сохранены в books.json ")

        elif choice == '6':
            output_inf(books_from_json)

        elif choice == '7':
            break


if __name__ == '__main__':
    main()