from functools import partial

instructions = [l.split() for l in open('input', 'r')]

def acc(pc, accumulator, offset): return pc + 1,      accumulator + offset
def jmp(pc, accumulator, offset): return pc + offset, accumulator
def nop(pc, accumulator, offset): return pc + 1,      accumulator

def swap(instructions, i):
    s = instructions[i][0]
    swaps = { 'jmp':'nop', 'nop':'jmp'}
    if s in swaps:
        instructions[i][0] = swaps[s]
        pc, accumulator = run(instructions, set([len(instructions)]))
        instructions[i][0] = s
        if pc == len(instructions):
            return accumulator
    return 0

def run(instructions, executed = set()):
    pc, accumulator = 0, 0
    while pc not in executed:
        executed.add(pc)
        i = instructions[pc]
        pc, accumulator = eval(i[0])(pc, accumulator, int(i[1]))
    return pc, accumulator

print(run(instructions)[1],
      sum(map(partial(swap, instructions), range(len(instructions)))))
    
