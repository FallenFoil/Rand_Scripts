# Memory efficient implementation of Vigenere cipher

LOWER_ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
UPPER_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']


def VigenereCipher(input_text, key, encrypt=True):
    output_text = ""
    i = 0

    for char in input_text:
        if char.isalpha():
            if char.islower():
                minus = 97
                alphabet = LOWER_ALPHABET
            else:
                minus = 65
                alphabet = UPPER_ALPHABET

            pi = ord(char) - minus
            ki = ord(key[i % len(key)]) - minus
            if encrypt:
                index = (pi + ki) % 26
            else:
                index = (pi - ki) % 26

            output_text = output_text + alphabet[index]
            i += 1
        else:
            output_text = output_text + char

    return output_text


if __name__ == "__main__":
    opt = 1

    while True:
        print("1. Encryption\n2. Decryption")
        opt = input("$ ")

        try:
            opt = int(opt)

            if opt == 1 or opt == 2:
                break
        except:
            print("An error has occurred")

    if opt == 1:
        plain_text = input("Plaintext: ")
        key = input("Key: ")
        cipher_text = VigenereCipher(plain_text, key)
        print(f"Ciphertext: {cipher_text}")
    else:
        cipher_text = input("Ciphertext: ")
        key = input("Key: ")
        plain_text = VigenereCipher(cipher_text, key, False)
        print(f"Plaintext: {plain_text}")
