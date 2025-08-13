fs = frozenset([1,2, 3, 4, 5])
fs2 = frozenset([4, 5, 6, 7, 8])

print(type(fs))

for i in fs:
    print(i)

print(5 in fs)
print(7 in fs)

fs3 = fs.copy()
print(fs3)

#union
print(fs.union(fs2))

#intersection
print(fs.intersection(fs2))

#difference
print(fs.difference(fs2))

#symmetric difference
print(fs.symmetric_difference(fs2))