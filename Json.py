import json

class Json_Input_Output:

    def output_from_json(filename):
        try:  # Обработка встроенной ошибки
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"math_books": [], "psychology_books": [], "literature_books": [], "science_books": []}

    def input_to_json(inf, filename):
        try:  # Обработка встроенной ошибки
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(inf, f, ensure_ascii=False, indent=4)
            print(f"Все книги сохранены в файл с именем {filename}")
        except IOError as e:
            print(f"Ошибка при записи данных в файл: {str(e)}")

    # Добавление книг

    def add_math_books(inf, math_book):
        inf['math_books'].append(math_book.__add__())

    def add_psychology_books(inf, psychology_book):
        inf['psychology_books'].append(psychology_book.__add__())

    def add_literature_books(inf, literature_book):
        inf['literature_books'].append(literature_book.__add__())

    def add_science_books(inf, science_book):
        inf['science_books'].append(science_book.__add__())