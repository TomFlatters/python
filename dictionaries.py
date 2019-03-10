# dictionaries:
# dictionaries are a fundamental data structure which contains "key-value" pairs - each value is represented by a key
# this is the data structure used in JSON

d = {} # creates a dictionary
d["some key"] = "some_value" # assigns the key "some_key" to the value "some-value"
# note: the key can be a number or string

fav_nums = {"good": 3, "better": 7, "best": 37} # a dictionary doesn't need to be initalised to empty

# example: phone book
phone_book = {"075": "T. Flatters"}
num = input("Enter a phone number: ")
print("The number belongs to " + phone_book[num])

# map through a dictionary:
for rating in fav_nums: # see how the "for __ in ___" can still be used with keys
    print(fav_nums[rating])

# dictionaries represent graphs
# note: a python "dictionary" is referred to as a "map" elsewhere
