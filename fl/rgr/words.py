import random

def load_words():
    """Загружает слова из файла и возвращает их список."""
    with open("words.txt", "r") as file:
        words = [line.strip() for line in file if 3 <= len(line.strip()) <= 12]
    return words

def choose_word(words):
    """Выбирает случайное слово из списка."""
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    """Возвращает слово с угаданными буквами и подчеркиваниями для неугаданных."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    words = load_words()
    word = choose_word(words)
    attempts = 6
    guessed_letters = set()

    print("Добро пожаловать в игру 'Угадай слово'!")
    print(f"Слово: {display_word(word, guessed_letters)}")

    while attempts > 0:
        guess = input("Введите букву: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже вводили эту букву. Попробуйте другую.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Отлично! Буква '{guess}' есть в слове.")
        else:
            attempts -= 1
            print(f"Буквы '{guess}' нет в слове. Осталось попыток: {attempts}")
        
        current_display = display_word(word, guessed_letters)
        print(f"Слово: {current_display}")
        
        if '_' not in current_display:
            print(f"Поздравляем! Вы угадали слово: {word}")
            break
    else:
        print(f"К сожалению, попытки закончились. Загаданное слово было: {word}")

if __name__ == "__main__":
    play_game()
