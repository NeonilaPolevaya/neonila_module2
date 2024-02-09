if __name__ == "__main__":
    # Write your solution here

    class Meal:
        """ Базовый класс блюдо """

        def __init__(self, name: str, gluten_free: bool, vegetarian: bool, price: int):
            """
            Создание и подготовка к работе объекта "Блюдо"
            :param name: Название блюда
            :param gluten_free: Наличие глютена в блюде
            :param vegetarian: Является ли блюдо вегетерианским
            :param price: Цена
            Примеры:
            >>> my_pancakes = Meal('Pancakes', False, True, 250)  # инициализация экземпляра класса
            """
            if not isinstance(name, str):
                raise TypeError("Название блюда должно быть типа str")
            self.name = name

            if not isinstance(gluten_free, bool):
                raise TypeError("Наличие глютена в блюде должно быть типа bool")
            self.gluten_free = gluten_free

            if not isinstance(vegetarian, bool):
                raise TypeError("Является ли блюдо вегетерианским должно быть типа bool")
            self.vegetarian = vegetarian

            if not isinstance(price, int):
                raise TypeError("Цена блюда должна быть типа int")
            if price <= 0:
                raise ValueError("Цена блюда должна быть положительным числом")
            self.price = price


        def __str__(self):
            return f"Блюдо {self.name}. Глютен-фри {self.gluten_free}. " \
                   f"Вегетерианское {self.vegetarian}. Цена {self.price}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, gluten_free={self.gluten_free!r}, " \
                   f"vegetarian={self.vegetarian!r}, price={self.price!r})"

        def check_meal(self) -> str:
            """
            Функция которая проверяет блюдо на наличие глютена или мяса
            :return: Сообщение о том, что блюдо является вегетерианским и/или глютен-фри
            Примеры:
            >>> my_pancakes = Meal('Pancakes', False, True, 250)
            >>> my_pancakes.check_meal()
            """
            ...

        def make_order(self, money_reserve: int) -> str:
            """
            Функция для заказа блюда
            :param money_reserve: Запас денег для заказа
            :raise ValueError: Если цена блюда превышает запас денег для заказа, то возвращается ошибка.
            :return: Сообщение о том, что заказ был сделан
            Примеры:
            >>> my_pancakes = Meal('Pancakes', False, True, 250)
            >>> my_pancakes.make_order(800)
            """
            if not isinstance(money_reserve, int):
                raise TypeError("Запас денег должен быть типа int")
            if money_reserve <= 0:
                raise ValueError("Запас денег должен быть положительным числом")
            ...


    class Pizza(Meal):
        """ Дочерний класс пицца """

        def __init__(self, name: str, gluten_free: bool, vegetarian: bool, price: int, size: int):
            """
            Создание и подготовка к работе объекта "Пицца"
            :param size: Размер пиццы
            :param name: Название блюда
            :param gluten_free: Наличие глютена в блюде
            :param vegetarian: Является ли блюдо вегетерианским
            :param price: Цена
            Примеры:
            >>> my_peperoni = Pizza('Peperoni', False, False, 450, 25)  # инициализация экземпляра класса
            """
            super().__init__(name, gluten_free, vegetarian, price)
            if not isinstance(size, int):
                raise TypeError("Размер пиццы должен быть типа int")
            if size < 0:
                raise ValueError("Размер пиццы должен быть положительным числом")
            self.size = size

        def __str__(self) -> str:
            return f"{super().__str__()}. Размер пиццы {self.size}"

        def __repr__(self) -> str:
            return f"{super().__repr__().replace(')', '')}. size={self.size!r})"

        def make_order(self, money_reserve: int) -> str:
            """
            Метод для заказа пиццы make_order перегружен, так как необходимо учесть новый атрибут "Размер пиццы"
            :param money_reserve: Запас денег для заказа
            :raise ValueError: Если цена пиццы превышает запас денег для заказа, то возвращается ошибка.
            :return: Сообщение о том, что заказ был сделан
            Примеры:
            >>> my_peperoni = Pizza('Peperoni', False, False, 450, 25)
            >>> my_peperoni.make_order(800)
            """
            ...

    pass
