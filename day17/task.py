import numpy as np

a = np.array([[1 if x == '#' else 0 for x in line.strip()]
              for line in open("input")])[np.newaxis,:,:]
for i in range(6):
    a = np.pad(a, 1, mode='constant', constant_values=(0,0))
    a2 = np.pad(a, 1, mode='constant', constant_values=(0,0))
    xs, ys, zs = a.shape
    ns = np.array([[[np.sum(a2[x:x+3, y:y+3, z:z+3]) - a[x,y,z]
                     for z in range(zs)]
                    for y in range(ys)]
                   for x in range(xs)])
    n3 = np.where(ns == 3,1,0)
    n2 = np.where(ns == 2,1,0)
    a = a * (n2 + n3) + (1 - a) * n3
print(np.sum(a))

a = np.array([[1 if x == '#' else 0 for x in line.strip()]
              for line in open("input")])[np.newaxis,np.newaxis,:,:]
for i in range(6):
    a = np.pad(a, 1, mode='constant', constant_values=(0,0))
    a2 = np.pad(a, 1, mode='constant', constant_values=(0,0))
    xs, ys, zs, ws = a.shape
    ns = np.array([[[[np.sum(a2[x:x+3, y:y+3, z:z+3, w:w+3])
                      - a[x,y,z,w]
                      for w in range(ws)]
                     for z in range(zs)]
                    for y in range(ys)]
                   for x in range(xs)])
    n3 = np.where(ns == 3,1,0)
    n2 = np.where(ns == 2,1,0)
    a = a * (n2 + n3) + (1 - a) * n3
print(np.sum(a))
