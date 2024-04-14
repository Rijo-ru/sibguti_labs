def generate_magic_square():
    n = 4
    magic_square = [[0] * n for _ in range(n)]

    # Start position for 1 is middle of first row
    i = 0
    j = n // 2

    # One by one put all values in the magic square
    num = 1
    while num <= n*n:
        magic_square[i][j] = num
        num += 1

        # Move up and to the right
        new_i = (i - 1) % n
        new_j = (j + 1) % n

        # If the cell is already filled
        if magic_square[new_i][new_j]:
            # Move down one cell
            i = (i + 1) % n
        else:
            i = new_i
            j = new_j

    return magic_square

def print_magic_square(magic_square):
    for row in magic_square:
        print(' '.join(map(str, row)))

def encrypt_message(message, magic_square):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            index = ord(char.upper()) - ord('A') + 1
            encrypted_message += str(magic_square[(index-1) // 4][(index-1) % 4]) + " "
        else:
            encrypted_message += char
    return encrypted_message.strip()

def decrypt_message(encrypted_message, magic_square):
    decrypted_message = ""
    for token in encrypted_message.split():
        if token.isdigit():
            index = int(token)
            decrypted_message += chr(ord('A') + (magic_square[(index-1) // 4][(index-1) % 4]) - 1)
        else:
            decrypted_message += token
    return decrypted_message

def main():
    # Generate magic square
    magic_square = generate_magic_square()
    print("Magic Square:")
    print_magic_square(magic_square)

    # Encrypt a message
    message = input("Enter a message to encrypt: ")
    encrypted_message = encrypt_message(message, magic_square)
    print("Encrypted Message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, magic_square)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
