# Write a program to analyse two different word files/paragraphs where you need to do following tasd
# 1. Find all unique words used in each paragraph
# 2. Identify the common words between both paragraphs
# 3. Display total count of unique word found in both paragraphs


para1 = input("Enter first paragraph:\n")
para2 = input("Enter second paragraph:\n")

words1 = set(para1.lower().split())
words2 = set(para2.lower().split())

unique_para1 = words1
unique_para2 = words2

common_words = words1.intersection(words2)

total_unique_words = words1.union(words2)

print("\nUnique words in paragraph 1:", unique_para1)
print("Unique words in paragraph 2:", unique_para2)
print("Common words:", common_words)
print("Total count of unique words in both paragraphs:", len(total_unique_words))
