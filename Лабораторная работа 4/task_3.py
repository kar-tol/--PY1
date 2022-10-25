def delete(list_, index=None):  # Создаем функцию, удаляющую значение из списка по указанному индексу
    if index is None:  # Условие, если индекс не задан
        list_ = list_[:-1]
    elif index > (len(list_)-1):  # Условие, если задан индекс, которого нет в списке
        list_ = list_[:-1]
    elif index is not None:  # Условие, если индекс указан
        list_1 = list_[:index]
        list_2 = list_[index+1:]
        list_ = list_1 + list_2
    return list_

print(delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]
