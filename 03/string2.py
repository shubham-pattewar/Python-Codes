# Write a program to build simple text analysis tool. Tool should perform following task for the input text
# 1. Count total no. of words 
# 2. count total no. of spaces 
# 3. count the frequency of each word included in input
# 4. Identify and display top 3 mostly frequent word 
# 5. Count the number of vowels in the entire text 
# 6. Sort the string with conversion of original string into the reverse ascending order

from collections import Counter

text = input("Enter your text:\n")

words = text.split()
word_count = len(words)
space_count = text.count(' ')
word_freq = Counter(words)
top_3 = word_freq.most_common(3)
vowel_count = sum(1 for c in text.lower() if c in 'aeiou')
sorted_text = ''.join(sorted(text, reverse=True))

print("Total words:", word_count)
print("Total spaces:", space_count)
print("Word frequencies:", dict(word_freq))
print("Top 3 frequent words:", top_3)
print("Total vowels:", vowel_count)
print("Reversed sorted string:", sorted_text)


