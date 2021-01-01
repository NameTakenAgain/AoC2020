import re
print([sum([all([k in d for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]) and
            all([{'byr' : lambda v : int(v) in range(1920, 2003),
                  'iyr' : lambda v : int(v) in range(2010, 2021),
                  'eyr' : lambda v : int(v) in range(2020, 2031),
                  'hgt' : lambda v : ((v[-2:] == 'in' and int(v[:-2]) in range(59, 77)) or
                                      (v[-2:] == 'cm' and int(v[:-2]) in range(150, 194))),
                  'hcl' : lambda v : re.match('#[0-9a-fA-F]{6}',v),
                  'ecl' : lambda v : v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                  'pid' : lambda v : re.match('^\d{9}$', v)}[k](d[k])
                 for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]) if v else True
            for d in [dict([x.split(':') for i in [p.replace('\n', ' ').split()] for x in i])
                      for p in open("input", "r").read().split('\n\n')]])
       for v in [False, True]])
