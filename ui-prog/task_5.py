# Нарисовать произвольный рисунок и нарисовать его средствами модуля matploblib.patches

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def hexagon(x_center, y_center, size):
    """Функция для создания шестиугольника с заданным центром и размером."""
    angle = np.linspace(0, 2 * np.pi, 6, endpoint=False)
    x_hex = x_center + size * np.cos(angle)
    y_hex = y_center + size * np.sin(angle)
    return x_hex, y_hex

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(6, 8))

# Рисуем улей из шестиугольников
num_layers = 5
size = 0.1
for i in range(num_layers):
    for j in range(num_layers - i):
        x_center = 0.5 + (j - (num_layers - i - 1) / 2) * size * 1.5
        y_center = 0.2 + i * size * np.sqrt(3)
        x_hex, y_hex = hexagon(x_center, y_center, size)
        hex_patch = patches.Polygon(xy=list(zip(x_hex, y_hex)), closed=True, edgecolor='black', facecolor='gold')
        ax.add_patch(hex_patch)

# Настройки осей
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')  # Отключаем оси

plt.title("Улей")
plt.show()
