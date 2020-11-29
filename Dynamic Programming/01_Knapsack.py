def knapSack(bagWeight, wt, val, n):
    if n == 0 or bagWeight == 0:
        return 0
    if(wt[n-1] > bagWeight):
        return knapSack(bagWeight, wt, val, n-1)
    else:
        return max(val[n-1]+knapSack(bagWeight-wt[n-1], wt, val, n-1), knapSack(bagWeight, wt, val, n-1))


val = list(map(int, input("Enter Values:").split()))
wt = list(map(int, input("Enter Weights:").split()))
n = len(val)
bagWeight = int(input("Enter Bag Weight:"))
print(knapSack(bagWeight, wt, val, n))
