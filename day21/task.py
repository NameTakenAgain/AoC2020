from collections import defaultdict, Counter

allfoods = Counter()
allergens = defaultdict(list)

for line in open("input"):
    l = line.strip().split(' (contains ')
    allfoods.update(set(l[0].split()))
    for allergen in l[1][:-1].split(', '):
        allergens[allergen].append(set(l[0].split()))
        
for k,v in allergens.items():
    allergens[k] = set.intersection(*v)

possible = set([v for vs in allergens.values() for v in vs ])
print(sum([v for k, v in allfoods.items() if k not in possible]))


uniques = []
while len(allergens) < sum([len(v) for v in allergens.values()]):
    uniques = [list(v)[0] for v in allergens.values() if len(v) == 1]
    print()
    print('u:', uniques)
    for k,v in allergens.items():
        print(k,':', v)
        
    for k in allergens:
        if len(allergens[k]) > 1:
            allergens[k].difference_update(uniques)

            
print(",".join([list(allergens[k])[0] for k in sorted(allergens.keys())]))

