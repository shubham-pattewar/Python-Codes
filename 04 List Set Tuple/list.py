list1 = [1,2, "Java", "Python", 45.66, '#']
print(list1)
list2 = []      
print(list2)
list3 = list(["Shubham", "anuj", "Pratik", "Abhi"])
print(list3)
print(type(list1))


# Positive and Negative Indexing in list
l = [10, 20, 30, 40, 50]
print(l[-1])
print(l[-3: ])
print(l[2:8])


# Iterating in list
l1 = ['A', 'B', 'C', 'D', 'E']
for i in l1:
    print(i)


# Adding elements to the list
l2 = [3, 54, 76, 7, 43, 54]
l2.append(50)
print(l2)

l2.insert(2, 98)        #insert(index, element)
print(l2)


# List Functions
# count
print(l2.count(54))

#sort
print(l2.sort())        # returns None

l2.sort()
print(l2)               # sorted list

#clear
l2.clear()
print(l2)

# copy()
l3 = ["A", "B", 34, 65]
l4 = l3.copy()
print(l4)

#append
l3.extend(["Shu", "Aj"])
print(l3)

#index
print(l3.index(34))

#pop
l3.pop()        # deletes last Index
print(l3)
l3.pop(2)
print(l3)