t1 = (30, 54, 6.6, "Python", 'java', 30, 3, 30, 6.6)
print("Tuple: ", t1)
print(t1[3:7])
print(t1[-2:])
print(t1[:-3])

#count
print(t1.count(30))
print(t1.count(6.6))

#index
print(t1.index("Python"))
print(t1.index(6.6))
print(t1.index(30))         #counts only first iteration

