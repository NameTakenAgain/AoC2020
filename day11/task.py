import numpy as np
from functools import reduce

input = [list(map(ord, list(i.strip()))) for i in open("input","r")]
sx, sy = len(input), len(input[0])

def pad(a, f = np.zeros):
    res = f((sx+2, sy+2), dtype = np.int8)
    res[1:1+sx,1:1+sy] = a
    return res

is_seat = pad(np.where(np.array(input) == ord('L'), 1, 0), np.ones)

directions = ((-1,-1), (-1, 0), (-1, 1),
              ( 0,-1),          ( 0, 1),
              ( 1,-1), ( 1, 0), ( 1, 1))

def neighbors1(a):
    return reduce(np.add, [a[1+x:1+x+sx,1+y:1+y+sy] for x,y in directions])

def neighbors2(a):
    def los(a, pos, dir):
        while True:
            pos = tuple(np.add(pos, dir))
            if is_seat[pos]: return a[pos]
    return np.array([[sum([los(a, (x,y), dir)
                           for dir in directions])
                      for y in range(1,1+sy)]
                     for x in range(1,1+sx)])

def round(a, neighbors, crowded):
    ns = neighbors(a)
    birth = pad(np.where(ns == 0, 1, 0))
    not_death = pad(np.where(ns < crowded, 1, 0))
    return np.where(a * not_death + birth, 1, 0) * is_seat

def run(neighbors, crowded):
    a = np.zeros((sx+2, sy+2), dtype = np.int8)
    while True:
        b = a
        a = round(a, neighbors, crowded)
        if np.array_equal(a, b): return np.sum(a)

print(run(neighbors1, 4), run(neighbors2, 5))
