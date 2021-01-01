import re

def Xbits(x, i):
    if i >= 36:
        yield 0
        return
    bit = (1 << i)
    for y in Xbits(x, i + 1):
        yield y
        if x & bit:
            yield bit + y

def mask(m, mem1, mem2, mask1, mask0, maskX):
    return (mem1, mem2,
            int(m[4].replace('X', '0'), 2),
            int(m[4].replace('X', '1'), 2),
            int(m[4].replace('1', '0').replace('X', '1'), 2))
    
def mem(m, mem1, mem2, mask1, mask0, maskX):
    mem1[int(m[3])] = int(m[4]) & mask0 | mask1
    for x in Xbits(maskX, 0):
        mem2[int(m[3]) & ~maskX | mask1 + x] = int(m[4])
    return mem1, mem2, mask1, mask0, maskX
    
mem1, mem2 = {}, {}
mask1 = mask0 = maskX = 0
for line in open("input"):
    m = re.search('(mask|mem)(\[(\d+)\])? = ([01X]{36}|(\d+))', line)
    mem1, mem2, mask1, mask0, maskX = eval(m[1])(m, mem1, mem2,
                                                 mask1, mask0, maskX)
print(sum(mem1.values()), sum(mem2.values()))
