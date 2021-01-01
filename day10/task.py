from numpy import prod
from collections import Counter

def combinations(j, l):
    if j == l[-1]:
        yield 1
    else:
        for a in filter(lambda v: j+1 <= v <= j+3, l):
            yield from combinations(a, l)

def split_on_3s(l):
    start = 0
    for i in range(len(l) - 1):
        if l[i] + 3 == l[i+1]:
            yield l[start:i + 1]
            start = i + 1
    yield l[start:]
    

print(
      prod([sum([x for x in combinations(l[0], l)])
            for l in filter(lambda x:len(x) > 2, split_on_3s(s))]))

input = set(map(int, open("input","r")))
s = [0] + sorted(input) + [max(input) + 3]
l = [s[i+1] - s[i] for i in range(len(s) - 1)]
print(l.count(1) * l.count(3),
      prod([prod([[1,1,2,4,7][k]] * v)
            for k,v in Counter(map(len,"".join(map(chr, l)).split(chr(3)))).items()]))

