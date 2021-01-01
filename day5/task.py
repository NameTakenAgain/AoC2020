print()
seats = [int(line.translate({70:48,66:49,82:49,76:48}), 2)
         for line in open("input")]
print(max(seats), *[i + 1
                    for i in range(128 * 8)
                    if i in seats and i + 1 not in seats and i + 2 in seats])
        

