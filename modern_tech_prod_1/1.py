from datetime import datetime
from time import sleep

# datetime.now() вызывается один раз при создании функции, и это значение будет использоваться при всех последующих вызовах функции, независимо от того, сколько времени прошло.

def time_now(msg, dt=None):
    if dt is None:
        dt = datetime.now()
    print(msg, dt)

# Тесты
time_now('Сейчас такое время: ')
sleep(1)
time_now('Прошла секунда: ')
sleep(1)