from collections import Counter
c = list(map(Counter, open("test", "r").read().split('\n\n')))
print(c)

cls = [(Counter("".join(l)), len(l)) for l in [group.split('\n') for group in open("input", "r").read().split('\n\n')]]
print(sum(map(len, [c for c,_  in cls])), sum([1 for c, l in cls for k,v in c.items() if v == l]))

# The one-liner
print(*[sum(map(len,[operation(*sets)
                     for sets in [[set(list(line)) for line in group]
                                  for group in [group.split('\n')
                                                for group in open("input", "r").read().split('\n\n')]]]))
        for operation in [set.union, set.intersection]])

# The slightly less convoluted solution :)

# Read the whole file, split into one string per group
groups = [group.split('\n') for group in open("input", "r").read().split('\n\n')]

# Build a list, per group, with sets of letters per line in the group
letters_per_group = [[set(list(line)) for line in group]
                     for group in groups ]
# Use the set union operation to find the letters that are in *any* of the lines
any = [set.union(*sets) for sets in letters_per_group]
# Use the set intersection operation to find the letters that are in *all* of the lines
all = [set.intersection(*sets) for sets in letters_per_group]

# Add the number of members in the all/any sets
print(sum([len(a) for a in any]), sum([len(a) for a in all]))
