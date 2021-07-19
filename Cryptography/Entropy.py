import math

# Calculates the entropy, in bits, where Pis are an array of the probabilities of the possible outcomes and m is the number of times
def entropy_non_uniform(Pis, m):
    res = 0

    for Pi in Pis:
        res += (Pi * math.log(1 / Pi, 2))

    return res * m

# Calculates the entropy, in bits, where N is the possible outcomes and m is the number of times
def entropy_uniform(N, m):
    return m * math.log(N, 2)

# Entropy of an uniform scenario with 6 possibilities, 1 time.
print(entropy_uniform(6, 1))

# Entropy of a non-uniform scenario with 3 possibilities, 1 time.
print(entropy_non_uniform([5/12, 3/12, 4/12], 1))
