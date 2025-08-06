s1 = {2, 3, 3, 3, "Python", "Java", 33.4}
print(s1)          # only prints unique elements
print(type(s1))

s2 = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"}
print(s2)

s2.add("Sep")
print(s2)

s2.remove("Apr")
print(s2)

s2.discard("Mar")
s2.discard("Dec")       # No Error unlike remove
print(s2)

s2.update(["Oct", "Nov"])
print(s2)


# Union Operation
Day1 = {"Mon", "Tues", "Wed", "Thu"}
Day2 = {"Fri", "Sat", "Sun"}
print(Day1 | Day2)
print(Day1.union(Day2))
