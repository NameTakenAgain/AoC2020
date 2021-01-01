from operator import add, mul

oper = {'+': add, '*': mul}

def term(s, f, acc, op):
    if s[0] == '(':
        v, s = ev(s[1:], f)
        return op(acc,v), s
    return op(acc, int(s[0])), s[1:]

def factor(s, f, acc, op):
    v1, s = term(s, f, 0, add)
    while s[0] == '+':
        v1, s = term(s[1:], f, v1, add)
    return op(acc, v1), s

def ev(s, f):
    acc, s = f(s, f, 0, add)
    while s[0] != '\n': 
        if s[0] == ')': return acc, s[1:]
        acc, s = f(s[1:], f, acc, op[s[0]])
    return acc
            
print(sum([ev(line.replace(' ', ''), term) for line in open('input')]),
      sum([ev(line.replace(' ', ''), factor) for line in open('input')]))
