import doctest


class Alarm:
    """
    Документация на класс.
    Класс описывает модель будильника.
    """
    def __init__(self, seconds: int, minutes: int, hours: int):
        """
        Создание и подготовка к работе объекта "Будильник"
        :param seconds: Секунды будильника
        :param minutes: Минуты будильника
        :param hours: Часы будильника
        Примеры:
        >>> alarm1 = Alarm(00, 30, 8)  # инициализация экземпляра класса
        """

        if not isinstance(seconds, int):
            raise TypeError('Параметр "seconds" должен быть типа int')
        if not isinstance(minutes, int):
            raise TypeError('Параметр "minutes" должен быть типа int')
        if not isinstance(hours, int):
            raise TypeError('Параметр "hours" должен быть типа int')
        if seconds < 0:
            raise ValueError('Параметр "seconds" должен положительным')
        if minutes < 0:
            raise ValueError('Параметр "minutes" должен положительным')
        if hours < 0:
            raise ValueError('Параметр "hours" должен положительным')

        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def alarm_off(self) -> None:
        """
        Метод, который выключает будильник
        Примеры:
        >>> alarm1 = Alarm(0, 30, 8)
        >>> alarm1.alarm_off()
        """

        seconds = None
        minutes = None
        hours = None

    def time_transfer(self, new_seconds: int, new_minutes: int, new_hours: int) -> None:
        """
        Метод, который переносит время будильника
        :param new_seconds: Новые секунды
        :param new_minutes: Новые минуты
        :param new_hours: Новые часы
        :raise ValueError: Если секунды, минуты или часы отрицательны, вызываем ошибку
        Примеры:
        >>> alarm1 = Alarm(0, 30, 8)
        >>> alarm1.time_transfer(0, 30, 9)
        """

        if not isinstance(new_seconds, int):
            raise TypeError('Параметр "new_seconds" должен быть типа int')
        if not isinstance(new_minutes, int):
            raise TypeError('Параметр "new_minutes" должен быть типа int')
        if not isinstance(new_hours, int):
            raise TypeError('Параметр "new_hours" должен быть типа int')
        if new_seconds < 0:
            raise ValueError('Параметр "new_seconds" должен положительным')
        if new_minutes < 0:
            raise ValueError('Параметр "new_minutes" должен положительным')
        if new_hours < 0:
            raise ValueError('Параметр "new_hours" должен положительным')

        seconds = new_seconds
        minutes = new_minutes
        hours = new_hours


class Chartholder:
    """
    Документация на класс.
    Класс описывает модель картхолдера.
    """
    def __init__(self, number_of_cards: int):
        """
        Создание и подготовка к работе объекта "Картхолдер"
        :param number_of_cards: Кол-во карт в картхолдере
        Примеры:
        >>> chartholder1 = Chartholder(5)  # инициализация экземпляра класса
        """

        if not isinstance(number_of_cards, int):
            raise TypeError('Параметр "number_of_cards" должен быть типа int')
        if number_of_cards < 0:
            raise ValueError('Параметр "number_of_cards" должен положительным')
        self.number_of_cards = number_of_cards

    def add_cards(self, new_cards: int) -> None:
        """
        Метод, который добавляет карты в картхолдер
        :param new_cards: Кол-во добавляемых карт
        :raise ValueError: Если кол-во добавленных карт отрицательно, вызываем ошибку
        Примеры:
        >>> chartholder1 = Chartholder(5)
        >>> chartholder1.add_cards(2)
        """

        if not isinstance(new_cards, int):
            raise TypeError('Параметр "new_cards" должен быть типа int')
        if new_cards < 0:
            raise ValueError('Параметр "new_cards" должен положительным')
        ...

    def remove_cards(self, remove_cards) -> None:
        """
        Метод, который убирает карты из картхолдера
        :param remove_cards: Кол-во убираемых карт
        :raise ValueError: Если кол-во убираемых карт отрицательно, вызываем ошибку
        Примеры:
        >>> chartholder1 = Chartholder(8)
        >>> chartholder1.add_cards(4)
        """

        if not isinstance(remove_cards, int):
            raise TypeError('Параметр "remove_cards" должен быть типа int')
        if remove_cards < 0:
            raise ValueError('Параметр "remove_cards" должен положительным')
        ...

class Flamethrower:
    """
    Документация на класс.
    Класс описывает модель огнемета.
    """
    def __init__(self, power: int, fuel_reserve: int):
        """
        Создание и подготовка к работе объекта "Огнемёт"
        :param power: Мощность огнемёта
        :param fuel_reserve: Запас топлива в огнемёте
        Примеры:
        >>> flamethrower1 = Flamethrower(50, 2)  # инициализация экземпляра класса
        """

        if not isinstance(power, int):
            raise TypeError('Параметр "power" должен быть типа int')
        if power < 0:
            raise ValueError('Параметр "power" должен положительным')
        if not isinstance(fuel_reserve, int):
            raise TypeError('Параметр "fuel_reserve" должен быть типа int')
        if fuel_reserve < 0:
            raise ValueError('Параметр "fuel_reserve" должен положительным')

    def refill(self, new_fuel: int) -> None:
        """
        Метод, который дозаправляет огнемёт
        :param new_fuel: Добавляемое топливо
        :raise ValueError: Если добавляемое топливо отрицательно, вызываем ошибку
        Примеры:
        >>> flamethrower1 = Flamethrower(50, 1)
        >>> flamethrower1.refill(1)
        """

        if not isinstance(new_fuel, int):
            raise TypeError('Параметр "new_fuel" должен быть типа int')
        if new_fuel < 0:
            raise ValueError('Параметр "new_fuel" должен положительным')
        ...

    def change_power(self, delta_power: int) -> None:
        """
        Метод, который меняет мощность огнемёта
        :param delta_power: Насколько меняется мощность
        Примеры:
        >>> flamethrower1 = Flamethrower(50, 2)
        >>> flamethrower1.refill(10)
        """

        if not isinstance(delta_power, int):
            raise TypeError('Параметр "new_fuel" должен быть типа int')
        ...


if __name__ == "__main__":
    doctest.testmod()