def Sum(freq, i, j):
    sum = 0
    for p in range(i, j+1):
        sum += freq[p]
    return sum


def optCost(freq, i, j):
    if j < i:
        return 0
    if j == i:
        return freq[i]
    freqSum = Sum(freq, i, j)
    min = 99999999
    for r in range(i, j+1):
        cost = (optCost(freq, i, r-1)+optCost(freq, r+1, j))
        if cost < min:
            min = cost
    return freqSum+min


def optimalSearchTree(keys, freq, n):
    return optCost(freq, 0, n-1)


keys = list(map(int, input("Enter key values:").split()))
freq = list(map(int, input("Enter key values:").split()))
n = len(keys)
print("Cost of Optimal Binary Search Tree is:",
      optimalSearchTree(keys, freq, n))
