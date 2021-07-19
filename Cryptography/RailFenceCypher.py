# Memory efficient implementation of Rail Fence cipher


def row_length(input_length, key_length, row_index):
    return 0

def Encrypt(plain_text, key):
    output_text = ""
    for row in range(key):
        i = row
        output_text = output_text + plain_text[i]
        offset_1 = (key * 2) - 2 - (2 * row)

        if offset_1 == 0:
            offset_1 = (key * 2) - 2

        double_offset = False
        if row != 0 and row != (key - 1) and row != (key - 1) / 2:
            double_offset = True
            offset_2 = (key * 2) - 2 - (2 * ((key - 1) - row))

        offset = offset_1

        while True:
            i = i + offset

            if i >= len(plain_text):
                break

            if double_offset:
                if offset == offset_1:
                    offset = offset_2
                else:
                    offset = offset_1

            output_text = output_text + plain_text[i]

    return output_text


def Decrypt(cipher_text, key):
    plain_text = ""

    add = 0

    first = True
    end = False

    while not end:
        if first:
            start = 0
            stop = key
            step = 1

            start_index = 0
        else:
            start = 1
            stop = key
            step = 1

            start_index = row_length(len(cipher_text), key, 0)

        up_diagonal = add % 2 != 0

        if up_diagonal:
            start = key - 2
            stop = -1
            step = -1

            start_index = len(cipher_text) - row_length(len(cipher_text), key, start) - row_length(len(cipher_text), key, start + 1)

        for row in range(start, stop, step):
            row_len = row_length(len(cipher_text), key, row)

            if row_len <= add:
                if up_diagonal:
                    start_index -= row_length(len(cipher_text), key, row - 1)
                else:
                    start_index += row_len

                continue

            plain_text += cipher_text[start_index + add]

            if len(plain_text) == len(cipher_text):
                end = True
                break

            if up_diagonal:
                start_index -= row_length(len(cipher_text), key, row - 1)
            else:
                start_index += row_len

        first = False
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
        except:
            print("An error has occurred")

    if opt == 1:
        plain_text = input("Plaintext: ")
        key = input("Key: ")
        cipher_text = Encrypt(plain_text, int(key))
        print(f"Ciphertext: {cipher_text}")
    else:
        cipher_text = input("Ciphertext: ")
        key = input("Key: ")
        plain_text = Decrypt(cipher_text, int(key))
        print(f"Plaintext: {plain_text}")