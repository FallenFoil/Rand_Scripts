from base64 import b64encode, b64decode
import pandas as pd
import Crypto.Cipher.AES as AES


def str_xor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


def clean_csv(file):
    csv = pd.read_csv(file, ";")
    csv = csv.drop(['httpRealm', 'formActionOrigin', 'guid', 'timeCreated', 'timeLastUsed', 'timePasswordChanged'],
                   axis=1)
    csv.to_csv("contas.csv", index=False, sep=";")


def encrypt(key, file):
    if len(key) != 16:
        exit(0)

    csv = pd.read_csv(file, ";")

    for i in range(len(csv["password"])):
        cipher = AES.new(key, AES.MODE_EAX)
        cipher_text, tag = cipher.encrypt_and_digest(str.encode(csv["password"][i]))
        result = cipher_text + tag + cipher.nonce
        csv["password"][i] = b64encode(result).decode('utf-8')

    csv.to_csv("contas.csv", index=False, sep=";")


def decrypt(key, file):
    if len(key) != 16:
        exit(0)

    csv = pd.read_csv(file, ";")

    for i in range(len(csv["password"])):
        data = b64decode(csv["password"][i])
        nonce = data[len(data) - 16:len(data)]
        tag = data[len(data) - 32:len(data) - 16]
        cipher_text = data[:len(data) - 32]

        cipher = AES.new(key, AES.MODE_EAX, nonce)
        print(cipher.decrypt_and_verify(cipher_text, tag).decode('utf-8'))

if __name__ == "__main__":
    opt = 1

    while True:
        print("1. Clean csv\n2. Encryption\n3. Decryption")
        opt = input("$ ")

        try:
            opt = int(opt)

            if opt == 1 or opt == 2 or opt == 3:
                break
        except:
            print("An error has occurred")

    if opt == 1:
        file = input("Csv File: ")
        file = "contas.csv"
        clean_csv(file)
    elif opt == 2:
        # k1 = input("Key 1 (size = 16): ")
        k1 = "abcdefghijklmnop"
        # k2 = input("Key 2 (size = 16): ")
        # k3 = str_xor(k1, k2)
        encrypt(str.encode(k1), "contas.csv")
        # encrypt(str.encode(k2), "contas.csv")
        # encrypt(str.encode(k3), "contas.csv")
    elif opt == 3:
        k1 = "abcdefghijklmnop"
        decrypt(str.encode(k1), "contas.csv")
    else:
        k1 = input("Key 1 (size = 16): ")
        k2 = input("Key 2 (size = 16): ")
