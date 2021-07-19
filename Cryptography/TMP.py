def find_graphs(file):
    f = open(file, "r")
    line = f.readline()
    f.close()

    print(len(line))

    trigraph = f"{line[0]}{line[1]}{line[2]}"
    for i in range(3, len(line)):
        for j in range(i, len(line)):
            if j + 2 >= len(line):
                break
            if f"{line[j]}{line[j + 1]}{line[j + 2]}" == trigraph:
                print(f"{trigraph}: {j + 2 - i + 1}")
        trigraph = f"{line[i - 2]}{line[i - 1]}{line[i]}"


def count_max_chars(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    dict = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "J": 0,
        "K": 0,
        "L": 0,
        "M": 0,
        "N": 0,
        "O": 0,
        "P": 0,
        "Q": 0,
        "R": 0,
        "S": 0,
        "T": 0,
        "U": 0,
        "V": 0,
        "W": 0,
        "X": 0,
        "Y": 0,
        "Z": 0
    }

    for line in lines:
        for char in line:
            if char in dict.keys():
                dict[char] = dict[char] + 1

    print(dict)

    max_value = max(dict.values())
    for k, v in dict.items():
        if v == max_value:
            print(f"'{k}': {v}")


def get_all_combinations():
    arr = ["X", "G", "H", "U", "I", "V"]

    for i in arr:
        for j in arr:
            if i != j:
                print(f"# a, b = find_a_b(alf_num[\"{i}\"], alf_num[\"{j}\"])")


get_all_combinations()