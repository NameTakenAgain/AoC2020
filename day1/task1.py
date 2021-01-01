from itertools import combinations
from numpy import prod

with open("input1") as f:
    values = [int(v) for v in f]
    print([prod(vs) for l in [2, 3]
           for vs in combinations(values, l)
           if sum(vs) == 2020])
            
                
