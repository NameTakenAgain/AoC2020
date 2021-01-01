from copy import deepcopy

def plain1(deck, seen): return False
def plain2(deck, c0, c1, cond1, cond2): return c0 > c1

def recursive1(deck, seen):
    t = (tuple(deck[0]), tuple(deck[1]))
    if t in seen: return True
    seen.add(t)
    return False

def recursive2(deck, c0, c1, cond1, cond2):
    if c0 < len(deck[0]) and c1 < len(deck[1]):
        return len(Combat([deepcopy(deck[0][1:c0 + 1]),
                           deepcopy(deck[1][1:c1 + 1])],
                          cond1, cond2)[0])
    return c0 > c1


def Combat(deck, cond1, cond2):
    seen = set()
    while len(deck[0]) and len(deck[1]):
        if cond1(deck, seen): return [[1],[]]
        c0, c1 = deck[0][0], deck[1][0]
        cond = cond2(deck, c0, c1, cond1, cond2)
        deck = [deck[0][1:] + ([c0, c1] if cond else []),
                deck[1][1:] + ([c1, c0] if not cond else [])]
    return deck

deck = [[int(i) for i in l.strip().split('\n')[1:]]
        for l in open("input").read().split('\n\n')]

print([sum([sum([(i + 1) * v for i, v in enumerate(d[::-1])]) for d in ds])
       for ds in [Combat(deepcopy(deck), plain1, plain2),
                  Combat(deepcopy(deck), recursive1, recursive2)]])
