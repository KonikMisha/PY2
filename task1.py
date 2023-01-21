# TODO Написать 3 класса с документацией и аннотацией типов

class Cup:
    def __init__(self, wather_status, liquid_status, liquid_capacity):
        """"
        Создание объекта класса "Кружка"
        :param wrap_status: статус кружки (есть вода или нет).
        :param liquid_status: текущее количество жидкости в кружке
        :param liquid_capacity: вместимость кружки
        Примеры:
        >>> my_Cup = Cup(0, 10, 100) # инициализация экземпляра класса
        """


        if (wather_status != 0) and (wather_status!= 1):
            raise ValueError("the mug must be with water (1) or without water (0)")
        self.wather_status = wather_status
        if not isinstance(liquid_status, (int, float)):
            raise TypeError("Wrong type for liquid_status")
        if not isinstance(liquid_capacity, (int, float)):
            raise TypeError("Wrong type for liquid_capacity")
        if liquid_status > liquid_capacity:
            raise ValueError("Capacity must be graiter than occupied volume")
        if liquid_status < 0:
            raise ValueError("Amount of liquid must not be lesser than zero")
        if liquid_capacity < 0:
            raise ValueError("Amount of liquid must not be lesser than zero")
        self.liquid_status = liquid_status
        self.liquid_capacity = liquid_capacity
    def pour_water(self):
        """"
        Функция воду, если ее небыло,
        в случае успеха выводится сообщение (вода налита).
        :raise ValueError: вызывает ошибку, если кружка была открыта при вызове метода
        Примеры:
        >>> my_Cup = Cup(1, 10, 100)
        >>> my_Cup.pour_water()
        """
    ...
    def out_water(self):
        """"
        Функция выливает воду, если та была наполнена,
        в случае успеха выводится сообщение (кружка пуста).
        :raise ValueError: вызывает ошибку, если кружка была пустая при вызове метода
        Примеры:
        >>> my_Cup = Cup(0, 10, 100)
        >>> my_Cup.out_water()
        """
        ...
    def add_liquid(self, liquid_input):
        """"
        Функция добавляет жидкость в кружку, если кружка пустая
        :raise TypeErroe: вызывает ошибку при попытке налить не целое и не вещественное число жидкости
        :raise ValueError: вызывает ошибку при попытке переполнить бутылку или налить отрицательные значения
        :return: новое число занятого объёма бутылки
        примеры:
        >>> my_Cup = Cup(0, 10, 100)
        >>> my_Cup.add_liquid(50)
        """
        ...


class Glasses:
    def __init__(self, vision_status, material_type):
        """
        Создание объекта класса корабль:
        :param vision_status: рение
        :param cargo_type: материал
        Примеры:
        >>> eyes = Glasses(+2.5, "Metal")
        """
        if not isinstance(vision_status, (int,float)):
            raise TypeError("Water vision must be int or float")
        if not isinstance(material_type, str):
            raise TypeError("Name of material type must be string")


    def check_vision(self):
        """
        Метод смотрит зрение
        :return: возвращает значение зрения
        Примеры:
        >>> eyes = Glasses(+2.5, "Metal")
        >>> eyes.check_vision()
        """
    ...

    def check_is_material_type(self, type_):
        """
        Метод проверяет соответствие материала очков с предложенным пользователем типом
        :param type_: материал, с которым сравнивается значение
        :raise ErrorType: вызывает ошибку, если type_ не строковая переменная
        :return: возвращает значение True, если тип материала очков совпал с type_, False - если не совпал
        Примеры:
        >>> eyes = Glasses(+2.5, "Metal")
        >>> eyes.check_is_material_type("Plastic")
        """
        ...

class Car:
    def __init__(self, mileage, price):
        """
        Инициализация объекта город:
        :param mileage: пробег автомобиля
        :param price: цена автомобиля (в тыс. рублей)
        Примеры:
        >>> BMW = Car(50617, 2400) # PEP8 здесь противоречит тому, что города пишутся с большой буквы
        """
        if not isinstance(mileage, int):
            raise TypeError("Mileage must be int!")
        if mileage <= 0:
            raise ValueError("Mileage must be graiter than 0")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be float or int!")
        if price <= 0:
            raise ValueError("Price must be graiter than 0")

    def last_price(self):
        """
        Метод обновляет
        :return: возвращает новую цену
        Примеры:
        >>> BMW = Car(50617, 2400)
        >>> BMW.last_price()
        """
        ...

    def mileage_up(self, additional_mileage):
        """
        Метод увеличивает пробег автомобиля на additional_area
        :param additional_area: новый пробег автомобиля
        :raise TypeError: вызывает ошибку, если тип additional_area не int и не float
        :return: возвращает новый пробег
        Примеры:
        >>> BMW = Car(50617, 2400)
        >>> BMW.mileage_up(10)
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()