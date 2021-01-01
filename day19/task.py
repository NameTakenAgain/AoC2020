import string

rules, strings = {}, []
for line in open("input"):
    parts = line.strip().split(': ')
    if len(parts)== 1:
        strings.append(parts[0])
        continue
    rules[int(parts[0])] = [[int(i) if i[0] in string.digits
                             else i.replace('"', '')
                             for i in part.split()]
                            for part in parts[1].split(' | ')]

def match_sequence(s, seq):
    if not seq: return [0]
    return [p + p2
            for p in matches(s, seq[0])
            for p2 in match_sequence(s[p:], seq[1:])]
    
def matches(s, rule):
    if not s: return []
    if isinstance(rule, str): return [ 1 ] if s[0] == rule else []
    return [p for part in rules[rule] for p in match_sequence(s, part)]

print(sum([l  == len(s) for s in strings for l in matches(s, 0)]))
