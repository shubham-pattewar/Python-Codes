# Write a program to build simple text analysis tool. Tool should perform following task for the input text
# 1. Count total no. of words 
# 2. count total no. of spaces 
# 3. count the frequency of each word included in input
# 4. Identify and display top 3 mostly frequent word 
# 5. Count the number of vowels in the entire text 
# 6. Sort the string with conversion of original string into the reverse ascending order

str = "Hello How are you are How"

words = str.split()
counter = len(words)
print("Total Number of Words: ", counter)

print("Total Number of Count: ", str.count(' '))

