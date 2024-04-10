import random

def generate_omophones(alphabet):
    omophones = {}
    numbers = list(range(100, 1000))  # Создаем список трехзначных чисел для использования в качестве омофонов
    random.shuffle(numbers)  # Перемешиваем числа

    for letter in alphabet:
        omophones[letter] = []  # Создаем пустой список омофонов для каждой буквы

    for letter in alphabet:
        while len(omophones[letter]) < 3:  # Добавляем по 3 омофона для каждой буквы
            number = numbers.pop()  # Берем очередное число из списка
            omophones[letter].append(number)  # Добавляем число в список омофонов для данной буквы

    return omophones

def main():
    # Создаем список кириллического алфавита
    alphabet = [chr(code) for code in range(ord('а'), ord('я')+1)] + ['ё']
    omophones = generate_omophones(alphabet)

    # Выводим полученные омофоны для каждой буквы
    for letter, values in omophones.items():
        print(f'{letter}: {", ".join(map(str, values))}')

if __name__ == "__main__":
    main()
