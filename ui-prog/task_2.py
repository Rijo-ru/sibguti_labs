a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))

# Проверяем, что a не равно 0, чтобы уравнение было решаемым
if a != 0:
    x = b / a
    print(f"Решение уравнения: x = {x}")
else:
    print("Уравнение не имеет решений, так как a равно 0.")
