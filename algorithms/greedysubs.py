# return the lengths of 'greedy' subsequences for a given array length, subsqequence length and array:

def greedysubsequence(lengthList, lengthSubsequence, list):
    numberSubsequences = lengthList - lengthSubsequence + 1
    working = [[0]*i]
    result = [[0]*i for i in range(0,numberSubsequences)]
    print(result)

    for i in range(0,numberSubsequences-1):
        for k in range(1,lengthSubsequence-1):   
            working[i] = [list[i+k]]
            for j in range(1,lengthSubsequence-k):
                    if (list[k+j+i] > working[i][-1]):
                        working[i][k].append(list[j+i])    
                    print(result)

    print(result)
    return result


greedysubsequence(6, 4, [1, 5, 2, 5, 3, 6])