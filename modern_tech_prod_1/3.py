from nikolay import Nikola  # Импортируем класс Nikola из пакета nikolay

# Создаем экземпляры класса Nikola
person1 = Nikola("Николай", 30)
person2 = Nikola("Максим", 25)
person3 = Nikola("Анна", 20)

# Выводим информацию о созданных объектах
print(person1.name, person1.age)  # Николай 30
print(person2.name, person2.age)  # Я не Максим, а Николай 25
print(person3.name, person3.age)  # Я не Анна, а Николай 20

# Попытка добавить новый атрибут
try:
    person1.отчество = "Иванович"
except AttributeError as e:
    print(e)  # Невозможно добавить атрибут 'отчество' к экземпляру класса Nikola

# Попытка добавить новый метод
try:
    person1.приветствие = lambda: print("Привет!")
except AttributeError as e:
    print(e)  # Невозможно добавить атрибут 'приветствие' к экземпляру класса Nikola