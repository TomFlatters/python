# basic usage of Python lists:

beatles = [ "John", "Paul", "George", "Ringo" ]

number_of_beatles = len(beatles) # number_of_beatles = 4

beatle = beatles[0] # beatle is now "John", Python lists start numbering at 0
beatle = beatles[1] # beatle is now "Paul"

beatles[3] = "Ringo Starr" # The list is now [ "John", "Paul", "George", "Ringo Starr" ]

# Pete Best was the original drummer before Ringo
beatles.append("Pete") # beatles is now [ "John", "Paul", "George", "Ringo Starr", "Pete"]
del beatles[4] # beatles is now [ "John", "Paul", "George", "Ringo Starr" ]
# beatles.remove("Pete") # is another option for removing by value instead!

#concatenate lists
one_direction = ["Niall", "Liam", "Harry", "Louis"]
names = beatles + one_direction

#print a list of names...
for name in names:
    print(name)

#or index them as well!
for i in range(0, len(names)):
    print(str(i) + ": " + names[i])