import math

def f(x, y, c):
    try:
        # Первая часть: ln|cos(x^2 + 2)|
        cos_part = math.cos(x**2 + 2)
        if cos_part == 0:
            raise ValueError("Значение cos(x^2 + 2) равно 0, логарифм не определен.")
        result = math.log(abs(cos_part))
        
        # Вторая часть: 3.5 * (x / y)^2 + e^c
        if y == 0:
            raise ValueError("Деление на ноль: y = 0.")
        result += (3.5 * (x / y)**2 + math.exp(c)) / (math.sin(y**2 * x**3)**2)
        
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None
    except ZeroDivisionError:
        print("Деление на ноль.")
        return None
    except OverflowError:
        print("Переполнение.")
        return None
    
    return result

# Используем функцию с заданными координатами
x1, y1, c1 = math.pi / math.sqrt(2), -3.41, 1.6
x2, y2, c2 = 1, 0, -10

print(f"f(x1, y1, c1) = {f(x1, y1, c1)}")
print(f"f(x2, y2, c2) = {f(x2, y2, c2)}")

