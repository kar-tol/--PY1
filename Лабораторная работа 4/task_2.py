def get_count_char(str_):  # Создаем функцию, которая будет принимать строку, а возвращать словарь
    list_letters = list(str_.lower())  # Из строки создаем список символов, приводя все символы к нижнему регистру
    count_letters_dict = {}  # Создаем пустой словарь, который будет заполнять цикл
    DEFAULT_COUNT = 0  # Количество каждого символа в начале

    for letter in list_letters: # Создаем цикл, формирующий словарь из буквенного символа и его количества повторений
        if letter.isalpha():
            count_letters_dict[letter] = count_letters_dict.get(letter, DEFAULT_COUNT) + 1

    return count_letters_dict
    #return get_count_percent_letter_dict(count_letters_dict)  # Данная строка нужна для определения частоты повторения символа в процентах

def get_count_percent_letter_dict(dict_):  # Создаем функцию, которая принимает словарь символов
    sum_of_letters = sum(dict_.values())  # Общее количество буквенных символов
    for letter in dict_:  # Создаем цикл, который заменяет в словаре количество каждого элемента на процентное отношение ко всем символам
        dict_[letter] = round(dict_[letter] / sum_of_letters * 100, 2)
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
