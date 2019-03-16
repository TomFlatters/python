test_data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:1 2008"

# a simple way
def findEmailHost(data):

    atpos = data.find("@") # "@" position
    sppos = data.find(' ',atpos) # space position after atpos position
    host = data[atpos+1 : sppos-1]

    return host

print(findEmailHost(test_data))