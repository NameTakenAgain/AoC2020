from re import sub

sub1 = [0,9,1,2,3,4,5,6,7,8] + [0]*38 + [0,9,1,2,3,4,5,6,7,8]
add1 = [0,2,3,4,5,6,7,8,9,1] + [0]*38 + [0,2,3,4,5,6,7,8,9,1]

def move(cups, current):
    cc = cups + cups
    pickup = cc[current:current + 3]
    newcups = sub("[%s]" % pickup, "", cups)
    dest = sub1[ord(cc[current - 1])]
    while chr(dest + 48) in pickup:
        dest = sub1[dest]
    pos = newcups.find(chr(dest + 48))
    cups = newcups[:pos + 1] + pickup + newcups[pos + 1:]
    if current > pos:
        steps = min(9 - current, 3)
        cups = cups[steps:] + cups[:steps]
    return cups, add1[current]
    
cups, curr = "872495136", 1
for i in range(100):
    cups, curr = move(cups, curr)
print(cups)
pos = cups.find('1')
print(cups[pos+1:] + cups[:pos])

s = "872495136"
n = [i + 1 for i in range(1000001)]

prev = m = curr = int(s[0])
for c in s[1:]:
    n[prev] = int(c)
    prev = int(c)
    m = max(prev, m)
n[prev] = 10
n[-1] = curr

for i in range(10000000):
    p1 = n[curr]
    p2 = n[p1]
    p3 = n[p2]
    dest = curr
    while True:
        dest = dest - 1 if dest > 1 else 1000000
        if not dest in [p1, p2, p3]: break
    n[curr] = n[p3]
    n[p3] = n[dest]
    n[dest] = p1
    curr = n[curr]
print(n[1], n[n[1]], n[1] * n[n[1]])
