import class_operation


def test_repr():
    assert type(
        class_operation.Operation('date', 'description', 'to_op', 'amount', 'currency')) is class_operation.Operation


def test_date():
    fix_class = class_operation.Operation("2019-09-07T07:20:13.889610", "Перевод с карты на карту",
                                          "МИР 1582474475547301", "18536.73", "RUB",
                                          "Maestro 4284341727554246")
    assert fix_class.formate_date() == "07.09.2019"


def test_mask():
    fix_class = class_operation.Operation("2019-09-07T07:20:13.889610", "Перевод с карты на карту",
                                          "Счет 12189246980267075758", "18536.73", "RUB",
                                          "Maestro 4284341727554246")
    assert fix_class.mask_from() == "Maestro 4284 34** **** 4246"
    assert fix_class.mask_to() == "Счет **5758"