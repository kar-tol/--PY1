from pprint import pprint  # Импортируем из модуля pprint функцию pprint


COUNT = 16  # Количество словарей в списке
list_dict = [{'bin': bin(n), 'dec': n, 'hex': hex(n), 'oct': oct(n)} for n in range(COUNT)]  # Создаем список словарей

pprint(list_dict)
