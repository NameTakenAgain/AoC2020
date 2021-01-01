import re
from numpy import prod

def readinput():
    f = open("input")

    rules = []
    while True:
        line = f.readline().strip()
        m = re.search(r'(.+): (\d+)\-(\d+) or (\d+)\-(\d+)', line)
        if not m: break
        rules.append((m[1], ((int(m[2]), int(m[3])), (int(m[4]), int(m[5])))))
    
    f.readline()
    line = f.readline().strip()
    ticket = [int(i) for i in line.split(',')]
    f.readline()
    line = f.readline()
    others = [[int(i) for i in line.split(',')] for line in f.readlines()]
    return rules, ticket, others
    
def valid(x):
    return any([lo <= x <= hi for r in rules for lo, hi in r[1]])

rules, ticket, others = readinput()

v = [t for t in others if (all([valid(i) for i in t]))]

matches = [(c, set([i for i,rule in enumerate(rules)
             if all([any([lo <= v <= hi for lo, hi in rule[1]])
                     for v in [t[c] for t in v]])]))
           for c in range(len(ticket))]

uniques = []
while len(uniques) < len(matches):
    unique = [x for x in matches if len(x[1]) == 1][0]
    u = list(unique[1])[0]
    uniques.append((unique[0], u))
    for m in matches:
        if u in m[1]:
            m[1].remove(u)
    
print(sum([i
           for t in others
           for i in t
           if not(valid(i))]),
      prod([ticket[c]
            for c,r in uniques
            if rules[r][0].startswith('departure')]))
    
