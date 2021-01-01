age = {}
count = 1

for n in [5,2,8,16,18,0,1]:
    age[n] = (count, count)
    last = n
    count += 1

while count <= 30000000:
    if last in age:
        last = age[last][1] - age[last][0]
    else:
        last = 0
        
    if last in age:
        age[last] = (age[last][1], count)
    else:
        age[last] = (count, count)
    if (count in [2020, 30000000]):
        print(last)
    count += 1
