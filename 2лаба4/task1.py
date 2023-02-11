class Plain:
    def __init__(self, fuel: int):
        self.fuel = fuel

    def __str__(self):
        return f'Для перелёта понадобится {self.fuel} тонн топлива'

    def __repr__(self):
        return f"{self.__class__.__name__}(fuel={self.fuel!r})"


class Passenger(Plain):
    def __init__(self, fuel: int, category: str):
        super().__init__(fuel)
        self.category = category
        if not isinstance(category, str):
            raise TypeError(f'{self.category} должен содержать в себе текст: "мнутренний", "международный", "трансатлантический"')

    def __str__(self):
        super_str = super().__str__()
        return f'{super_str}. Перелет {self.category}.'

    def __repr__(self):
        super_repr = super().__repr__()
        return f"{super_repr}, (category={self.category!r})"


class Charter(Passenger):
    def __init__(self, fuel: int, category: str):
        super().__init__(fuel, category)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()


class Regular(Passenger):
    def __init__(self, fuel: int, category: str, customers: int):
        super().__init__(fuel, category)
        if isinstance(customers, int):
            if customers > 0:
                self.customers = customers
            else:
                raise ValueError('Количество пассажиров должно быть выражено в числовом формате')
        else:
            raise ValueError("У самолета нет пассажиров")

    def __str__(self):
        super_puper = super().__str__()
        return f'Куплено {self.customers} билета. {super_puper}'

    def __repr__(self):
        repr_puper = super().__repr__()
        return f'{repr_puper}, (customers={self.customers!r})'


class Military(Plain):
    def __init__(self, fuel: int, paratroopers, weight: int):
        super().__init__(fuel)
        self.paratroopers = paratroopers
        if isinstance(weight, int):
            if weight >= 0:
                self.weight = weight
            else:
                raise ValueError('Количество ракет не может быть орицательным.')
        else:
            raise ValueError("Количество ракет должно быть в виде числа")

    def __str__(self):
        return f'Количество ракет: {self.weight}. Десант: {self.paratroopers} военных. Для перелёта понадобится {self.fuel} тонн топлива'

    def __repr__(self):
        return f'{self.__class__.__name__}(fuel={self.fuel!r}), (paratroopers={self.paratroopers!r}), (weight={self.weight!r})'


class Cargo(Plain):
    def __init__(self, fuel: int, weight: int):
        super().__init__(fuel)
        if isinstance(weight, int):
            if weight > 0:
                self.weight = weight
            else:
                raise ValueError('Груз не записан')
        else:
            raise ValueError('Количество груза должно быть записано числом')

    def __str__(self):
        str_super = super().__str__()
        return f'Груз: {self.weight} тонн. {str_super}'

    def __repr__(self):
        repr_super = super().__repr__()
        return f'{repr_super}, (weight={self.weight!r}).'


if __name__ == "__main__":
    Being_777 = Charter(15, "международный")
    print(Being_777)
    Airbus_A319 = Regular(7, "внутренний",136)
    print(Airbus_A319)
    Il_76 = Cargo(12, 65)
    print(Il_76)
    Cy_27 = Military(5,"нет",6)
    print(Cy_27)
    pass

