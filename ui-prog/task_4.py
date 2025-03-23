# Построить график функции на интервале [a, b] f(x)=(x**2 - 5) / x

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**2 - 5) / x

# Запрашиваем у пользователя ввод интервала [a, b]
try:
    a = float(input("Введите начальное значение интервала a: "))
    b = float(input("Введите конечное значение интервала b: "))
    
    if a >= b:
        raise ValueError("Начальное значение интервала должно быть меньше конечного.")
except ValueError as e:
    print(f"Ошибка ввода: {e}")
    exit()

# Создаем массив значений x с небольшим шагом, исключая ноль
x = np.linspace(a, b, 400)
x = x[x != 0]  # Исключаем ноль, чтобы избежать деления на ноль

# Вычисляем значения функции
y = f(x)

# Строим график
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$f(x)=\frac{x^2 - 5}{x}$')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x) = (x^2 - 5) / x')
plt.legend()
plt.grid(True)
plt.show()
