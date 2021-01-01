from itertools import combinations

input = list(map(int, open("input", "r")))

def valid(input, i):
    return input[i] in map(sum, combinations(input[i-25:i], 2))

invalid = [input[i] for i in range(26, len(input))
           if not valid(input, i)][0]

print(invalid, *[min(l) + max(l) for l in [input[i:j]
                                           for i in range(len(input))
                                           for j in range(i + 2, len(input))]
                 if sum(l) == invalid])
