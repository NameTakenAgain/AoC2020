rdirs = [complex(1,0),complex(0, 1),complex(-1,0),complex(0,-1)]
ldirs = [complex(1,0),complex(0,-1),complex(-1,0),complex(0, 1)]

def eswn(dir, p, sp, wp, d, x):
    offset = rdirs['ESWN'.find(d)] * x
    return (dir, p + offset, sp, wp + offset)
    
def f(dir, p, sp, wp, d, x):
    return dir, p + rdirs[dir] * x, sp + wp * x, wp

def r(dir, p, sp, wp, d, x):
    return ((dir + x // 90) % 4, p, sp, wp * rdirs[x // 90])
    
def l(dir, p, sp, wp, d, x):
    return ((dir - x // 90) % 4, p, sp, wp * ldirs[x // 90])
    
func = {'E' : eswn, 'S' : eswn, 'W' : eswn, 'N' : eswn,
        'R' : r, 'L' : l, 'F' : f}

dir, p, sp, wp = 0, complex(0,0), complex(0,0), complex(10,-1)
for line in open('input', 'r'):
    dir, p, sp, wp = func[line[0]](dir, p, sp, wp, line[0], int(line[1:]))

print(int(abs(p.real) + abs(p.imag)), int(abs(sp.real) + abs(sp.imag)))

