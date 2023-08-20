import json
from operator import itemgetter
from class_operation import Operation

def load_json(file_name):
    """
    Получаем массив операций
    :param file_name: путь к json файлу
    :return: массив не пустых словарей
    """
    with open(file_name, encoding='utf-8') as file:
        dict_json = json.load(file)

    # создаем массив без пустых элементов
    new_dict = []
    for dict in dict_json:
        if dict:
            new_dict.append(dict)

    return new_dict


def get_list_executed(operation_list):
    """
    Получаем последние 5 выполненных операций
    :param operation_list: массив операций из load_json
    :return: последние 5 выполненных операций
    """
    # записываем только операции со значением "EXECUTED"
    executed_list = []
    for operation in operation_list:
        if operation['state'] == "EXECUTED":
            executed_list.append(operation)

    # сортируем массив в порядке убывания(свежие операции вначале)
    newlist = sorted(executed_list, key=itemgetter('date'), reverse=True)

    return newlist[0: 5]


def get_list_class(executed_list):
    """
    Создаем массив экземпляров класса
    :param executed_list: массив из 5 последних выполненных операций
    :return: массив экземпляров класса
    """

    # пустой список для массива экземпляров класса
    operations = []
    for operation in executed_list:
        if 'from' in operation.keys():
            date = operation['date']
            description = operation['description']
            operation_to = operation['to']
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['code']
            operation_from = operation['from']
            operations.append(Operation(date, description, operation_to, amount, currency, operation_from))
        else:
            date = operation['date']
            description = operation['description']
            operation_to = operation['to']
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['code']
            operations.append(Operation(date, description, operation_to, amount, currency))
    return operations