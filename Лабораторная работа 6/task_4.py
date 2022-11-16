import json  # Импортируем модуль json

INPUT_FILE = "input_1.csv"  # Файл, из которого берем данные


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:  # Создаем функцию, которая принимает 3 аргумента
    with open(filename, encoding="utf-8") as f:  # Открываем файл для чтения
        file_data = f.read()  # Считываем данные из файла
        headers_list = file_data.split(new_line)[0].split(delimiter)  # Создаем список заголовков
        list_dict = []  # Создаем пустой список словарей, который цикл будет заполнять
        for i in range(1, len(file_data.split(new_line))-1):
            list_dict.append(dict(zip(headers_list, file_data.split(new_line)[i].split(delimiter))))  # Заполняем список словарями
        return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
