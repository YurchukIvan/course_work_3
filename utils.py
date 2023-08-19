import json
import os

PATH = os.path.join('data', 'operations.json')


def load_json(file_name):
    """
    Получаем массив операций
    :param file_name: путь к json файлу
    :return: массив не пустых словарей
    """
    with open(file_name, encoding='utf-8') as file:
        dict_json = json.load(file)

    new_dict = []
    for dict in dict_json:
        if dict:
            new_dict.append(dict)

    return new_dict
