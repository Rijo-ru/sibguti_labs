x = int(input("Input x: "))
y = int(input("Input y: "))

res = (abs(x) - abs(y)) / (1 + abs(x*y))
print("Результат ", res)