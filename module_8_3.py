class IncorrectVinNumber(Exception):
    def __init__(self, vin):
        if not isinstance(vin,int):
            self.message = 'Некорректный тип vin номер'
        elif not 1_000_000 <= vin <= 9_999_999:
            self.message = 'Неверный диапазон для vin номера'


class IncorrectCarNumbers(Exception):
    def __init__(self, numbers):
        if not isinstance(numbers,str):
            self.message = 'Некорректный тип данных для номеров'
        elif not len(numbers) == 6:
            self.message = 'Неверная длина номера'


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__bin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin):
        if isinstance(vin, int) and 1_000_000<=vin <= 9_999_999:
            return True
        raise IncorrectVinNumber(vin)

    def __is_valid_numbers(self,numbers):
        if isinstance(numbers,str) and len(numbers) == 6:
            return True
        raise IncorrectCarNumbers(numbers)


if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')
    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')
    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')