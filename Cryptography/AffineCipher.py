alf_num = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25
}

num_alf = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z"
}


def Encrypt(input_text, a, b):
    output_text = ""

    for char in input_text:
        if char.isalpha():
            char = char.upper()
            int_char = alf_num[char]
            calc = ((a * int_char) + b) % 26
            output_text = output_text + num_alf[calc]
        else:
            output_text = output_text + char

    return output_text


def Decrypt(input_text, a, b):
    output_text = ""
    a_minus = 0
    found = False
    for i in range(1, 26):
        if ((i * a) % 26) == 1:
            a_minus = i
            found = True
            break

    if not found:
        return ""

    for char in input_text:
        if char.isalpha():
            char = char.upper()
            int_char = alf_num[char]
            calc = ((int_char - b) * a_minus) % 26
            output_text = output_text + num_alf[calc]
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
        a = input("a: ")
        b = input("b: ")
        cipher_text = Encrypt(plain_text, a, b)
        print(f"Ciphertext: {cipher_text}")
    else:
        cipher_text = input("Ciphertext: ")
        a = input("a: ")
        b = input("b: ")
        plain_text = Decrypt(cipher_text, a, b)
        print(f"Plaintext: {plain_text}")
