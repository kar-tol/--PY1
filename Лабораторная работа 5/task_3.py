from random import randint  # Из модуля random импортируем функцию randint


start = -10  # Начало диапазона значений
stop = 10  # Конец диапазона значений
count = 15  # Размер списка
list_numbers = []  # Список, который будем заполнять значениями


def get_unique_list_numbers() -> list[int]:  # Создаем функцию, которая возвращает список, заполненный случайными целыми числами
    while len(list_numbers) != count:
        num = randint(start, stop)
        while num not in list_numbers:
            list_numbers.append(num)

    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
