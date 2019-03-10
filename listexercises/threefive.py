def threes_or_fives(n):

    # calculate maximum multiple of 3 and 5 less than 'n':
    threes = int(((n-1) - ((n-1) % 3))/3) + 1
    fives = int(((n-1) - ((n-1) % 5))/5) + 1

    # create an array of multiples of 3 and 5 based on "threes" and "fives" values:
    threes_and_fives = []
    for i in range(threes):
        threes_and_fives.append(3*i)
    for j in range(fives):
        threes_and_fives.append(5*j)

    # sort the array by order and remove a zero if needed:
    threes_and_fives.sort()
    if threes_and_fives:
        if threes_and_fives[0] == threes_and_fives[1]:
            return threes_and_fives[1:]
    return threes_and_fives

def test(test_case, expected):
    actual = threes_or_fives(test_case)
    if actual == expected:
        print("Passed test for " + str(test_case))
    else:
        print("Didn't pass test for " + str(test_case))
        print("The result was " + str(actual) + " but it should have been " + str(expected))

test(0, [])
test(3, [0])
test(5, [0, 3])
test(6, [0, 3, 5])
test(10, [0, 3, 5, 6, 9])