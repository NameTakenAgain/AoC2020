contains = {}
for l in [l.strip() for l in open('input', 'r')]:
    m = l.split(' bags contain ')
    contains[m[0]] = dict(map(lambda v: (v[1],v[0]),
                              re.findall(r' ?(\d+) (.+?) bags?\.?,?', m[1])))
def can_hold(color1, wanted):
    return (wanted in contains[color1]
            or any([can_hold(color2, wanted) for color2 in contains[color1]]))

def bags(color1):
    return 1 + sum([int(contains[color1][color2]) * bags(color2)
                    for color2 in contains[color1]])

print(sum([can_hold(bag, 'shiny gold') for bag in contains]), bags('shiny gold') - 1)

