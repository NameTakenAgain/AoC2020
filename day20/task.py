from collections import Counter, defaultdict
from numpy import prod
import re

def value(s):
    return int(s.translate({35:49,46:48}), 2)
    
def values(s):
    return [value(s),value(s[::-1])]
    
def readtile(s):
    lines = s.split('\n')
    nr = int(lines[0][5:9])
    lines = lines[1:11]
    ledge = "".join([l[0] for l in lines])
    hedge = "".join([l[9] for l in lines])
    return (nr, lines, (values(lines[0]) + values(lines[9])
                        + values(ledge) + values(hedge)))
    
tiles = [readtile(t) for t in open("input").read().split('\n\n')]

c = Counter(i for t in tiles for i in t[2])
corners = [t[0] for t in tiles if Counter([c[e] for e in t[2]])[1] == 4]
print(prod(corners))

def rotate(t):
    return ["".join([r[len(t) - i - 1] for r in t]) for i in range(len(t))]

trimmed_tiles = {}
north = defaultdict(list)
west = defaultdict(list)

def trim_tile(t, nr, index):
    trim = [l[1:-1] for l in t[1:-1]]
    n = value(t[0])
    w = value("".join([l[0] for l in t]))
    s = value(t[9])
    e = value("".join([l[9] for l in t]))
    north[n].append((nr, index))
    west[w].append((nr, index))
    return trim, (n,w,e,s)
    
def rotate_and_flip(tile):
    trimmed = []
    nr, t = tile[0], tile[1]
    for i in range(4):
        trimmed.append(trim_tile(t, nr, i))
        t = rotate(t)
    t = t[::-1]
    for i in range(4):
        trimmed.append(trim_tile(t, nr, i + 4))
        t = rotate(t)
    trimmed_tiles[nr] = trimmed

for t in tiles:
    rotate_and_flip(t)

def get_direction(prev, i, dir, dirdict):
    result = []
    while True:
        t = trimmed_tiles[prev]
        result.append((prev,i))
        next = t[i][1][dir]
        l = list(filter(lambda x: x[0] != prev, dirdict[next]))
        if not l:
            return result
        prev, i = l[0]
                        
def solve(corner):
    c = trimmed_tiles[corner]
    solutions =[]
    for rotation in range(8):
        edges = c[rotation][1]
        if len(north[edges[0]]) == 1 and len(west[edges[1]]) == 1:
            print()
            row = get_direction(corner, rotation, 3, north)
            solutions.append([get_direction(tile, index, 2, west)
                              for tile, index in row])
    return solutions

def get_image(solution):
    return ["".join(z)
           for l in solution
           for z in zip(*[trimmed_tiles[t][i][0] for t,i in l])]

def find_nessie(img, line, pos):
    m1 = re.search('#....##....##....###', img[line][pos:])
    if m1:
        pos += m1.start()
        m2 = re.search('.#..#..#..#..#..#', img[line + 1][pos:])
        m3 = re.search('..................#', img[line ][pos:])
        if m2 and m3 and m2.start() == 0 and m3.start() == 0:
            return 1 + find_nessie(img, line, pos + 1)
    return 0

for c in corners:
    solutions = solve(c)
    for s in solutions:
        img = get_image(s)
        monster = 0
        for i in range(len(img) - 1):
            monster += find_nessie(img, i + 1, 0)
        if monster:
            print(sum([l.count('#') for l in img]) - monster * 15)
