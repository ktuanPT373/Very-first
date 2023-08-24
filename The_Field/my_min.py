def myMin(L):
    res = float('inf')
    for n in L:
        res = min(n,res)
    return res
print(myMin([3,4,5]))