from numpy import mul
slope = ["".join([line.strip()]*100) for line in open("input")]

for xstep, ystep in [(xs, ys)
                     for ys, xl in enumerate([[], [1,3,5,7], [1]])
                     for xs in xl]:
    print(sum([slope[y][x * xstep]  == '#' for x,y in enumerate(range(0, len(slope), ystep))]))

for xstep, ystep in [(xs, ys)
                     for ys, xl in enumerate([[], [1,3,5,7], [1]])
                     for xs in xl]:
    print(mul(sum([slope[y][x * xstep]  == '#' for x,y in enumerate(range(0, len(slope), ystep))])))

