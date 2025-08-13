# Write a program to analyse two different word files/paragraphs where you need to do following tasd
# 1. Find all unique words used in each paragraph
# 2. Identify the common words between both paragraphs
# 3. Display total count of unique word found in both paragraphs


para1 = input("Enter 1st para:\n")
para2 = input("Enter 2nd para:\n")

words1 = set(para1.lower().split())
words2 = set(para2.lower().split())

print("Unique words in paragraph 1:", words1)
print("Unique words in paragraph 2:", words2)
print("Common words:", words1.intersection(words2))
print("Total count of unique words in both paragraphs:", len(words1.union(words2)))
