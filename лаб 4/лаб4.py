class Pets:
    """
    Базовый класс питомцы.

    Атрибуты:
        name : Имя питомца
        age : Возраст питомца
        breed : Порода питомца

    """

    def __init__(self, name: str, age: int, breed: str) :
        """Инициализация базового питомца."""
        self.name = name
        self.age = age
        self.breed = breed

    def name(self):
        return self.name

    def author(self):
         return self.author

    def __str__(self):
        """Возвращает строковое представление."""
        return f"Питомец {self.name}. Возраст: {self.age} лет. Порода: {self.breed}."

    def __repr__(self):
        """Возвращает формальное представление."""
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}, breed={self.breed!r})"

    def get_info(self):
        """Базовый метод получения информации о питомце."""
        return f"'{self.name}' - {self.age} - {self.breed}"

    def get_name(self):
        """Геттер для имени (пример инкапсуляции)."""
        return self.name


class Cats(Pets):
    """Дочерний класс кошек."""

    def __init__(self, name: str, age: int, breed: str, climbing_skill: int):
        """Расширение конструктора: добавлен скилл лазанья."""
        super().__init__(name, age, breed)
        self.climbing_skill = climbing_skill

    def climbing_skill(self):
        return self.climbing_skill

    def climbing_skill(self, value):
        if value <0:
            raise ValueError("Показатель скилла варьируется от нуля")
        if value >10:
            raise ValueError("Показатель скилла варьируется до десяти")
        if not isinstance(value, int):
            raise TypeError ("Показатель скилла должен быть целым")
        self.climbing_skill=value

    def __str__(self):
        """Перегрузка: добавлена информация о скилле лазанья."""
        return f"Кот {self.name}. Возраст: {self.age} лет. Порода: {self.breed}. Скилл лазанья: {self.climbing_skill}."

    def __repr__(self):
        """Перегрузка: добавлена информация о скилле лазанья."""
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}, breed={self.breed!r}, climbing_skill={self.climbing_skill})"


    def get_info(self):
        """
        Перегрузка метода.

        Причина: для котов нужно добавить информацию о скилле лазанья.
        """
        return f"{super().get_info()}, {self.climbing_skill}."

    def climbing_skill(self) -> int:
        """Геттер для скилла лазанья."""
        return self.climbing_skill


class Dogs(Pets):
    """Дочерний класс собак."""

    def __init__(self, name: str, age: int, breed: str, training_skill: int):
        """Расширение конструктора: добавлен уровень дрессировки."""
        super().__init__(name, age, breed)
        self.training_skill = training_skill

    def training_skill(self):
        return self.training_skill

    def training_skill(self, value):
        if value <0:
            raise ValueError("Уровень дрессировки варьируется от нуля")
        if value >10:
            raise ValueError("Уровень дрессировки варьируется до десяти")
        if not isinstance(value, int):
            raise TypeError ("Уровень дрессировки должен быть целым")
        self.training_skill=value

    def __str__(self):
        """Перегрузка: добавлена информация об уровне дрессировки."""
        return f"Собака {self.name}. Возраст: {self.age} лет. Порода: {self.breed}. Уровень дрессировки: {self.training_skill}."

    def __repr__(self):
        """Перегрузка: добавлена информация об уровне дрессировки."""
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}, breed={self.breed!r}, training_skill={self.training_skill})"


    def get_info(self):
        """
        Перегрузка метода.

        Причина: для собак нужно добавить информацию об уровне дрессировки.
        """
        return f"{super().get_info()}, {self.training_skill}."

    def training_skill(self) -> int:
        """Геттер для уровня дрессировки."""
        return self.training_skill