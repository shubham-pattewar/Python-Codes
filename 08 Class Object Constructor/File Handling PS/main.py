from filehandling import read_file, write_file, update_file

# Read content from two files
lines1 = read_file('file1.txt')
lines2 = read_file('file2.txt')

# Write combined content to third file
write_file('file3.txt', lines1 + lines2)

# Read content from fourth file
lines4 = read_file('file4.txt')

# Insert content of fourth file into third file after first 10 lines
update_file('file3.txt', lines4, 10)