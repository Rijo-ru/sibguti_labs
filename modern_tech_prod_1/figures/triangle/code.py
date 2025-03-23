a, b, c = 7, 2, 8  # Скрытые переменные

def triangle_perimeter(a=a, b=b, c=c):
    return a + b + c

def triangle_area(a=a, b=b, c=c):
    # Используем формулу Герона
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5