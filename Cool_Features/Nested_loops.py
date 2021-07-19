for i in range(3):
    for j in range(4):
        for w in range(5):
            print(i + j + w)


from itertools import product

for i, j, w in product(range(3), range(4), range(5)):
    print(i + j + w)
