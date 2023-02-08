import doctest


class LightSource:
    def __init__(self, power: float, distance: float, durability: float, status: int):
        """
        Создание и подготовка к работе объекта "Источник света"
        :param power: Мощность источника света
        :param distance: Дальность освещения источника света
        :param durability: Долговечность источника света
        :param status: Состояние источника света (вкл/выкл)
        Примеры:
        >>> light = LightSource(15.5, 10.5, 2, 0)  # инициализация экземпляра класса
        """

        if not isinstance(power, float) and not isinstance(power, int):
            raise TypeError("Мощность источника света должна быть числом")
        if power <= 0:
            raise ValueError("Мощность источника света должна быть положительна")
        self.power = power

        if not isinstance(distance, float) and not isinstance(distance, int):
            raise TypeError("Дальность освещения источника света должна быть числом")
        if distance <= 0:
            raise ValueError("Дальность освещения источника света должна быть положительна")
        self.distance = distance

        if not isinstance(durability, float) and not isinstance(durability, int):
            raise TypeError("Долговечность источника света должна быть числом")
        if durability <= 0:
            raise ValueError("Долговечность источника света должна быть положительна")
        self.durability = durability

        if not isinstance(status, int):
            raise TypeError("Источник света либо включен (1), либо выключен (0)")
        if not (status == 1 or status == 0):
            raise ValueError("Источник света либо включен (1), либо выключен (0)")
        self.status = status

    def __str__(self) -> str:
        return f"Характеристики источника света: Мощность: {self.power} Вт, " \
               f"Дальность: {self.distance} м, " \
               f"Долговечность: {self.durability} год(а)/лет"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(power={self.power}, " \
               f"distance={self.distance}, durability={self.durability})"

    def on(self) -> None:
        """
        Функция, к-ая включает источник света

        Примеры:
        >>> light = LightSource(15.5, 10.5, 2, 0)
        >>> light.on()
        """
        self.status = 1

    def off(self) -> None:
        """
        Функция, к-ая выключает источник света

        Примеры:
        >>> light = LightSource(15.5, 10.5, 2, 1)
        >>> light.off()
        """
        self.status = 0


class RailwayLantern(LightSource):
    def __init__(self, power: float, distance: float, durability: float, status: int, mode: str):
        """
        Создание и подготовка к работе объекта "Железнодорожный фонарь",
        являющегося дочерним классом объекта "Источник света"
        :param power: Мощность ж/д фонаря
        :param distance: Дальность ж/д фонаря
        :param durability: Долговечность ж/д фонаря
        :param status: Состояние ж/д фонаря (вкл/выкл)
        :param mode: Режим работы ж/д фонаря. Предусматривает четыре
        режима в зависимости от ситуации на железной дороге. Используется
        в экстренных случаях (например, торможение локомотива), поэтому
        является защищенным атрибутом.
        Примеры:
        >>> r_light = RailwayLantern(300, 50, 5, 0, 'normal')
        """

        super().__init__(power, distance, durability, status)  # наследуем базовый конструктор
        if not isinstance(mode, str):  # и расширяем его
            raise TypeError("Режим работы фонарика должен быть строкой")
        if not (mode == "red" or mode == "yellow"
                or mode == "green" or mode == "normal"):
            raise ValueError("Допустимые режимы работы фонаря: red, yellow, green, normal")
        self._mode = mode

    def __str__(self) -> str:  # наследуем метод __str__
        return super().__str__()

    def __repr__(self) -> str:  # наследуем метод __repr__
        return super().__repr__()

    def on(self) -> None:  # наследуем метод on
        super().on()

    def off(self) -> None:  # наследуем метод off
        super().off()

    @property
    def mode(self) -> str:
        """
        Геттер для атрибута mode; получение значения атрибута mode

        Примеры:
        >>> r_light = RailwayLantern(300, 50, 5, 0, 'normal')
        >>> mode_railway = r_light.mode
        """
        return self._mode

    @mode.setter
    def mode(self, new_mode: str):
        """
        Сеттер для атрибута mode; установка значения атрибута mode
        :param new_mode: Режим, на который переключают фонарь

        Примеры:
        >>> r_light = RailwayLantern(300, 50, 5, 0, 'normal')
        >>> r_light.mode = "red"
        """
        if not isinstance(new_mode, str):
            raise TypeError("Режим работы фонарика должен быть строкой")
        if not (new_mode == "red" or new_mode == "yellow"
                or new_mode == "green" or new_mode == "normal"):
            raise ValueError("Допустимые режимы работы фонаря: red, yellow, green, normal")
        self._mode = new_mode


class OilLamp(LightSource):
    def __init__(self, power: float, distance: float, durability: float, status: int, oil: float):
        """
        Создание и подготовка к работе объекта "Масляная лампа",
        являющегося дочерним классом объекта "Источник света"
        :param power: Мощность лампы
        :param distance: Дальность лампы
        :param durability: Долговечность лампы
        :param status: Состояние лампы (вкл/выкл)
        :param oil: Количество масла в лампе. Без масла лампа не будет работать.
        Примеры:
        >>> o_light = OilLamp(15, 10, 1, 0, 250)
        """
        self.max_oil = 500
        super().__init__(power, distance, durability, status)  # наследуем базовый конструктор
        if not isinstance(oil, float) and not isinstance(oil, int):  # и расширяем его
            raise TypeError("Кол-во масла в лампе должно быть числом")
        if oil < 0:
            raise ValueError("Кол-во масла в лампе должно быть положительным")
        if oil > self.max_oil:
            raise ValueError(f"Кол-во масла в лампе не может превысить {self.max_oil} мл")
        self.oil = oil

    def __str__(self) -> str:  # наследуем метод __str__
        return super().__str__()

    def __repr__(self) -> str:  # наследуем метод __repr__
        return super().__repr__()

    def on(self) -> None:  # наследуем метод on и перегружаем его
        """
        Функция, включающая масляную лампу. В случае отсутствия масла лампа не
        заработает.

        Примеры:
        >>> o_light = OilLamp(15, 10, 1, 0, 250)
        >>> o_light.on()
        """

        if self.oil == 0:
            raise ValueError("Лампу не включить: в ней нет масла")
        super().on()

    def off(self) -> None:  # наследуем метод off
        super().off()

    def change_oil(self, new_oil: float):
        """
        Функция, меняющая кол-во масла в лампе на величину new_oil
        :param new_oil: Кол-во добавляемого/убавляемого масла

        Примеры:
        >>> o_light = OilLamp(15, 10, 1, 0, 250)
        >>> o_light.change_oil(150)
        """
        if new_oil > self.max_oil or (self.oil + new_oil) > self.max_oil:
            difference_oil = self.oil + new_oil - self.max_oil
            self.oil = self.max_oil
            print(f"{self.oil}, но вы потратили {difference_oil} масла впустую.")

        if self.oil + new_oil < 0:
            raise ValueError("Вы не можете слить столько масла: в лампе меньше масла")

    def is_empty_oillamp(self):
        """
        Функция, проверяющая пуста ли лампа

        Примеры:
        >>> o_light = OilLamp(15, 10, 1, 0, 250)
        >>> fullnes_oil = o_light.is_empty_oillamp()
        """
        if self.oil == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    doctest.testmod()

    """
    Проверка работоспособности классов:
    
    print("Базовый класс источника света")

    light = LightSource(15.5, 10.5, 2, 0)
    print(light.__str__())
    print(light.__repr__())
    print("\n")
    print(light.status)
    light.off()
    print(light.status)

    print("\nКласс железнодорожного фонаря")

    r_light = RailwayLantern(300, 50, 5, 0, 'normal')
    print(r_light.__str__())
    print(r_light.__repr__())
    print(r_light.mode)

    r_light.mode = "red"
    # r_light.mode = "jjj"  выдает ошибку
    # r_light.mode = -100  выдает ошибку
    print(r_light.mode)

    r_light.on()
    print(r_light.status)

    print("\nКласс масляной лампы")

    o_light = OilLamp(15, 10, 1, 0, 250)
    print(o_light.__str__())
    print(o_light.__repr__())

    o_light.change_oil(550)

    print(o_light.oil)
"""
