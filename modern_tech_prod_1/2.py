# Импортируем необходимые функции из пакета figures
from figures import circle_area, circle_perimeter
from figures import triangle_area, triangle_perimeter
from figures import square_area, square_perimeter

# Пример использования функций для окружности
print("Окружность:")
print(f"Площадь окружности с радиусом по умолчанию (5): {circle_area()}")
print(f"Длина окружности с радиусом по умолчанию (5): {circle_perimeter()}")
print(f"Площадь окружности с радиусом 10: {circle_area(10)}")
print(f"Длина окружности с радиусом 10: {circle_perimeter(10)}")
print()

# Пример использования функций для треугольника
print("Треугольник:")
print(f"Периметр треугольника со сторонами по умолчанию (7, 2, 8): {triangle_perimeter()}")
print(f"Площадь треугольника со сторонами по умолчанию (7, 2, 8): {triangle_area()}")
print(f"Периметр треугольника со сторонами 3, 4, 5: {triangle_perimeter(3, 4, 5)}")
print(f"Площадь треугольника со сторонами 3, 4, 5: {triangle_area(3, 4, 5)}")
print()

# Пример использования функций для квадрата
print("Квадрат:")
print(f"Периметр квадрата со стороной по умолчанию (15): {square_perimeter()}")
print(f"Площадь квадрата со стороной по умолчанию (15): {square_area()}")
print(f"Периметр квадрата со стороной 20: {square_perimeter(20)}")
print(f"Площадь квадрата со стороной 20: {square_area(20)}")