import math
import matplotlib.pyplot as plt

def calculate_arc_and_sector(radius, angle_degrees):
    # Переводим угол в радианы
    angle_radians = math.radians(angle_degrees)
    
    # Длина дуги: L = r * θ, где θ - угол в радианах
    arc_length = radius * angle_radians
    
    # Площадь сектора: S = 0.5 * r^2 * θ
    sector_area = 0.5 * radius**2 * angle_radians
    
    return arc_length, sector_area

def plot_sector(radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    
    # Создаем график
    fig, ax = plt.subplots()
    
    # Рисуем полный круг
    circle = plt.Circle((0, 0), radius, color='lightblue', fill=True, alpha=0.2)
    ax.add_artist(circle)
    
    # Рисуем сектор
    sector_x = [0] + [radius * math.cos(math.radians(deg)) for deg in range(int(angle_degrees) + 1)]
    sector_y = [0] + [radius * math.sin(math.radians(deg)) for deg in range(int(angle_degrees) + 1)]
    ax.fill(sector_x, sector_y, color='orange', alpha=0.6, label='Сектор')
    
    # Настройки графика
    ax.set_aspect('equal')
    ax.set_xlim(-radius-1, radius+1)
    ax.set_ylim(-radius-1, radius+1)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Сектор окружности радиусом {radius} и углом {angle_degrees}°")
    plt.legend()
    
    # Показываем график
    plt.show()


# Ввод данных
radius = float(input("Введите радиус окружности: "))
angle_degrees = float(input("Введите величину центрального угла (в градусах): "))

# Расчёт и вывод результатов
arc_length, sector_area = calculate_arc_and_sector(radius, angle_degrees)
print(f"Длина дуги: {arc_length}")
print(f"Площадь сектора: {sector_area}")

# Отрисовка сектора
plot_sector(radius, angle_degrees)
