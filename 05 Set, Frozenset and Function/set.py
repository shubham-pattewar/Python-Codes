month1 = {"Jan", "feb", "Mar", "Apr", "May", "Oct", "Nov", "Jul"}
month2 = set(["Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Jan", "feb", "Mar", "Apr", "May"])

#Adding Items
month1.add("Oct")
print(month1)

month2.remove("Jun")
print(month2)

month1.update(["Jun", "Jul"])

# month2.remove("May")          # It will show error
month2.discard("May")            # This will not show any error
print(month2)


month1 = {"Jan", "feb", "Mar", "Apr", "May", "Oct", "Nov", "Jul"}
month2 = set(["Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Jan", "feb", "Mar", "Apr", "May"])

print(month1 | month2)
print(month1.union(month2))

print(month2.issubset(month1))

print(month1.issubset(month2))

print(month1.issuperset(month2))

print(month1.issuperset(month2))

print(month1.intersection(month2))


