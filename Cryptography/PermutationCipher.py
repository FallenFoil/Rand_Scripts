# Memory efficient implementation of a simple Permutation cipher. The key is a list of the order of the columns.


def organize_key(key):
    new_key = [0] * len(key)
    i = 0

    for val in key:
        new_key[val - 1] = i
        i += 1

    return new_key


def column_length(input_length, key_length, column_index):
    res = int(input_length / key_length)
    mod = input_length % key_length

    if mod == 0:
        return res

    if column_index < mod:
        res += 1

    return res


def Encrypt(plain_text, key):
    cipher_text = ""
    key = organize_key(key)

    for i in key:
        while True:
            cipher_text += plain_text[i]
            i += len(key)
            if i >= len(plain_text):
                break

    return cipher_text


def Decrypt(cipher_text, key):
    plain_text = ""
    key = organize_key(key)

    cipher_len = len(cipher_text)
    key_len = len(key)

    add = 0
    end = False

    while not end:
        for i in range(key_len):
            index = add
            for key_val in key:
                if key_val == i:
                    break

                index += column_length(cipher_len, key_len, key_val)

            plain_text += cipher_text[index]

            if len(plain_text) == cipher_len:
                end = True
                break

        add += 1

    return plain_text


if __name__ == "__main__":
    opt = 1

    while True:
        print("1. Encryption\n2. Decryption")
        opt = input("$ ")

        try:
            opt = int(opt)

            if opt == 1 or opt == 2:
                break
        except TypeError:
            print("An error has occurred")

    if opt == 1:
        plain_text = input("Plaintext: ")

        key = input("Key (use spaces to separate the numbers): ")
        key = key.split()
        key = [int(i) for i in key]

        cipher_text = Encrypt(plain_text, key)
        print(f"Ciphertext: {cipher_text}")
    else:
        cipher_text = input("Ciphertext: ")

        key = input("Key (use spaces to separate the numbers): ")
        key = key.split()
        key = [int(i) for i in key]

        plain_text = Decrypt(cipher_text, key)
        print(f"Plaintext: {plain_text}")
