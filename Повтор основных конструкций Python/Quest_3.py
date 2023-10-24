from itertools import combinations
def inversions(sequence):
    return len(list(filter(lambda x: x[0] > x[1],  combinations(sequence, r=2))))

sequence = [3, 1, 4, 2]

print(inversions(sequence))


