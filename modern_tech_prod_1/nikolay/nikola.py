class Nikola:
    __slots__ = ('name', 'age')  # Запрещаем добавление новых атрибутов

    def __init__(self, name, age):
        # Проверяем имя и преобразуем его, если это не "Николай"
        if name != "Николай":
            self.name = f"Я не {name}, а Николай"
        else:
            self.name = name
        self.age = age

    def __setattr__(self, key, value):
        # Запрещаем добавление новых атрибутов
        if key not in self.__slots__:
            raise AttributeError(f"Невозможно добавить атрибут '{key}' к экземпляру класса Nikola")
        super().__setattr__(key, value)