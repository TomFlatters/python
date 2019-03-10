# my first attempt at a binary search:

print("Think of a number from 1-1000.")

low = 0
high = 1000


for n in range(1,10):
    guess = int((low + high) / 2)
    x = input("Is your number " + str(guess) + "?")
    if x == "Y" or x == "y":
        print("I win!")
        break
    else:
        y = input("Is it higher than " + str(guess) + "?")
        if  y == "Y" or y == "y":
            low = guess
        else:
            high = guess


# This example uses a while loop instead:

# print("Please think of a number that is >= 0 and < 1000")

# numberIsGeqTo = 0
# numberIsLtThan = 1000

# while numberIsGeqTo + 1 != numberIsLtThan:
#     # We need to write // instead of / for integer division
#     guess = (numberIsGeqTo + numberIsLtThan) // 2
#     response = input("Is your number less than " + str(guess) + "? ")
#     if response == "yes":
#         numberIsLtThan = guess
#     elif response == "no":
#         numberIsGeqTo = guess

# print("Your number is " + str(numberIsGeqTo))