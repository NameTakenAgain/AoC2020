from collections import defaultdict

tiles = defaultdict(bool)
dirs = (('nw',  0, +1), ('sw', -1,-1), ('w', -1, 0),
        ('ne', +1, +1), ('se',  0,-1), ('e', +1, 0))

def walk(s, x = 0, y = 0):
    if not s: return x, y
    for d in dirs:
        if s.startswith(d[0]):
            return walk(s[len(d[0]):], x + d[1], y + d[2])

for l in open('input'):
    x, y = walk(l.strip())
    tiles[(x,y)] = not tiles[(x,y)]

print(sum(tiles.values()))
for i in range(100):
    flip = set()
    for k in list(tiles):
        if tiles[k]:
            neighbors = sum([tiles[(k[0] + d[1], k[1] + d[2])] for d in dirs])
            if neighbors == 0 or neighbors > 2:
                flip.add(k)
    for k in list(tiles):
        if not tiles[k]:
            neighbors = sum([tiles[(k[0] + d[1], k[1] + d[2])] for d in dirs])
            if neighbors == 2:
                flip.add(k)
    for f in flip:
        tiles[f] = not tiles[f]
print(sum(tiles.values()))
