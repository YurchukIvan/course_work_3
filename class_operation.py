from datetime import datetime


class Operation:
    def __init__(self, date, description, operation_to, amount, currency, operation_from=None):
        """
        инициализация класса
        :param date: дата перевода
        :param description: описание перевода
        :param operation_to: куда
        :param amount: сумма перевода
        :param currency: валюта
        :param operation_from: откуда
        """
        self.operation_from = operation_from
        self.currency = currency
        self.amount = amount
        self.operation_to = operation_to
        self.description = description
        self.date = date

    def __repr__(self):
        """
        Вывод полей класса
        :return: поля класса
        """
        return f'Operation: дата перевода - {self.date}\n' \
               f'описание перевода - {self.description}\n' \
               f'откуда - {self.operation_from}\n' \
               f'куда - {self.operation_to}\n' \
               f'сумма перевода - {self.amount}\n' \
               f'валюта - {self.currency}\n'

    def formate_date(self):
        """
        Форматирует дату в понятный вид
        :return: дату в удобном формате
        """
        old_date = datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f')
        new_date = old_date.strftime('%d.%m.%Y')
        return new_date

    def mask_from(self):
        """
        Маскирует номер карты или счета отправителя
        :return: возвращает маскированный номер
        """
        name = ''
        numbers = ''
        # цикл, чтобы разделить карту\счет от номера
        if self.operation_from is not None:
            for letter in self.operation_from:
                if letter.isdigit():
                    numbers += letter
                elif letter.isalpha():
                    name += letter

            if len(numbers) == 16:
                return f'{name} {numbers[0:4]} {numbers[4:6]}** **** {numbers[-4:]}'
            elif len(numbers) > 16:
                return f'{name} **{numbers[-4:]}'
        else:
            return ''

    def mask_to(self):
        """
        Маскирует номер карты или счета получателя
        :return: возвращает маскированный номер
        """
        name = ''
        numbers = ''
        # цикл, чтобы разделить карту\счет от номера
        for letter in self.operation_to:
            if letter.isdigit():
                numbers += letter
            elif letter.isalpha():
                name += letter

        if len(numbers) == 16:
            return f'{name} {numbers[0:4]} {numbers[4:6]}** **** {numbers[-4:]}'
        elif len(numbers) > 16:
            return f'{name} **{numbers[-4:]}'