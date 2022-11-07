from random import sample  # Из модуля random импортируем функцию sample
from string import ascii_uppercase, ascii_lowercase, digits  # Из модуля string импортируем функции ascii_uppercase, ascii_lowercase, digits


DEFAULT_LENGTH = 8  # Длина пароля по умолчанию


def get_random_password(n=DEFAULT_LENGTH) -> str:  # Создаем функцию для генерации случайных паролей заданной длины
    symbols_list = [s for s in str(ascii_uppercase + ascii_lowercase + digits)]  # Создаем список символов
    password = "".join(sample(symbols_list, n))  # Из списка формируем пароль
    return password


print(get_random_password())
