import os
import utils

# путь к json файлу
PATH = os.path.join('data', 'operations.json')


def main():
    """
    Основная функция
    :return: результат
    """
    # переменная для массива данных
    operation_list = utils.load_json(PATH)

    # переменная для массива 5 последних выполненных операций
    executed_list = utils.get_list_executed(operation_list)

    # переменная для массива экземпляров класса
    class_list = utils.get_list_class(executed_list)

    # цикл на вывод операций
    for operation in class_list:
        print(f'\033[35mОперация:\033[00m\n'
              f'{operation.formate_date()} {operation.description}\n'
              f'{operation.mask_from()} -> {operation.mask_to()}\n'
              f'{operation.amount} {operation.currency}\n'
              f'')


if __name__ == '__main__':
    main()