def equation_product(n):
    result = 1
    for i in range(1, n + 1):
        result *= (1 + 1 / (i ** 2))
    return result

n = int(input("Введите значение n: "))
print("Результат уравнения для n =", n, ":", equation_product(n))
