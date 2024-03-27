def add_polynomials(poly1, poly2):
    len1 = len(poly1)
    len2 = len(poly2)
    result = []

    # Определяем максимальную степень полинома
    max_len = max(len1, len2)

    # Складываем коэффициенты полиномов
    for i in range(max_len):
        coeff1 = poly1[i] if i < len1 else 0
        coeff2 = poly2[i] if i < len2 else 0
        result.append(coeff1 + coeff2)

    return result

# Пример использования
poly1 = [1, 2, 3]  # коэффициенты полинома 1
poly2 = [4, 5, 6, 7]  # коэффициенты полинома 2
print("Результат сложения полиномов:", add_polynomials(poly1, poly2))
