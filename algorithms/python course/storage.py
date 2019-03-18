#
# start manipulating flat text files
#
# first we need to open the file:

# fhand = open('namefile.txt', 'r' / 'w' for read/write)
# returns a file handle ( a way to get to the data (like a link) )

# "\n" is a newline character, when printed shows a newline, e.g:
# print('Hello\nWorld!')

# xfile = open('mbox.txt')
# for loop sees xfile as a sequence of lines:
# we can count how many lines there are
# count = 0
# for line in xfile:
#     count = count +1
#     print("Lines: ", count)

# we can read the file: (doesn't split with new line)
# inp = xfile.read()
# how many characters?
# print(len(inp))

# print every line that starts with from:
# for line in xfile:
#     if line.startswith("From:"):
#         line = line.rstrip() # strip away the white space (extra new line)
#         print(line)

# use a different approach: ( stylistic difference )
# for line in xfile:
#     line = line.rstrip()
#     if not line.startswith("From:"):
#         continue # skips to the next "line"
#     print(line)
# has the same effect

# get file name from user:
try:
    fname = input('Enter the file name: ')
    fhand = open(fname)
except: 
    print("Could not read from: ", fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count+1
print('There were ', count, ' subject lines in ', fname)