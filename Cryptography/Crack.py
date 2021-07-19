import Cryptography.VigenereCipher as VigenereCipher
import Cryptography.AffineCipher as AffineCipher

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


def Decrypt_affine(file, a, b):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        plaintext = AffineCipher.Decrypt(line, a, b)
        print(plaintext)


def Decrypt_vigenere(file, key):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        plaintext = VigenereCipher.VigenereCipher(line, key, encrypt=False)
        print(plaintext)


def find_a_b(r, s):
    d_minus = 19
    p = 4
    q = 19
    a = (d_minus * (r - s)) % 26
    b = (d_minus * ((p * s) - (q * r))) % 26

    return a, b


def solutions():
    # Datagram 1
    # Decrypt_vigenere("Datagrams/datagram1.txt", k)

    # Datagram 2
    a, b = find_a_b(alf_num["A"], alf_num["J"])
    Decrypt_affine("Datagrams/datagram2.txt", a, b)

    # Datagram 3
    # Decrypt_vigenere("Datagrams/datagram3.txt", k)
