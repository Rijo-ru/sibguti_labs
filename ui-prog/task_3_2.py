# б) Вывести таблицу значений функции состоящей из N=18 строк в точках, где i от 1 до 18 строк
from task_3_1 import f
import math

# x = (abs(math.sin(i*math.pi/4)))**(1/3)
# y = math.sin((i*(math.pi/6)**(1/2)))
# c = math.log2(i)/math.cos(i)

N = 18
print(f"{'i':<5} {'x':<15} {'y':<15} {'c':<15} {'f(x, y, c)':<15}")
for i in range(1, N + 1):
    x = (abs(math.sin(i * math.pi / 4)))**(1/3)
    y = math.sin(i * (math.pi / 6)**(1/2))
    try:
        c = math.log2(i) / math.cos(i)
    except ZeroDivisionError:
        c = float('inf')  # Обработка деления на ноль в случае cos(i) == 0
    
    result = f(x, y, c)
    
    # Печать строки таблицы
    print(f"{i:<5} {x:<15.10f} {y:<15.10f} {c:<15.10f} {result}")