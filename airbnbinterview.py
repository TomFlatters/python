# taken from an airbnb interview question:

# find-missing(
# [4, 12, 9, 5, 6]
# [4, 9, 12, 6]
# )

def find_missing(completeArr, missingArr):
    completeArr.sort()
    missingArr.sort()

    i = 0
    while i < len(completeArr):
        if completeArr[i] != missingArr[i]:
            print(completeArr[i])
            return completeArr[i]
        i+=1

find_missing([4, 12, 9, 5, 6],[4, 9, 12, 6])