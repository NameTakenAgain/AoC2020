from numpy import sum
from re import match

      # 5) Sum up all the pairs
          # 4) Build a list with a pair of true/false for both conditions
print(sum([(c in range(lo, hi + 1), (s[lo] == l) + (s[hi] == l) == 1)
           # Compute lo and hi limit, the letter, occureances of the letter, and padded string
           for lo,hi,l,c,s in [(int(m[1]), int(m[2]), m[3], m[4].count(m[3]), ' ' + m[4])
                         # Extract different parts of the line
                         for m in [match(r'(\d+)-(\d+) (\w): (\w+)', l)
                                   # 1) For all lines in input
                                   for l in open("input")]]], axis=0))


