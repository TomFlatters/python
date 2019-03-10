# flatten a 2D list into a 1D list

def flatten(xs):
    ls=[]
    for sublist in xs:
        for item in sublist:
            ls.append(item)
    return ls

def test(test_case, expected):
    actual = flatten(test_case)
    if actual == expected:
        print("Passed test for " + str(test_case))
    else:
        print("Didn't pass test for " + str(test_case))
        print("The result was " + str(actual) + " but it should have been " + str(expected))

test([], [])
test([[1, 2], [3, 4]], [1, 2, 3, 4])
test([[], [1, 2], [3, 4], []], [1, 2, 3, 4])