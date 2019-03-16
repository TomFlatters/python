# "try" and "except" can be used to deal
# with invalid inputs:

x = input("Enter a number:")

try:
    print("Double your number is:")
    print(int(x) * 2)
except:
    print("Please enter a NUMBER!")