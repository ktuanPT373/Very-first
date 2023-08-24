def myProduct(L):
    res = 1
    for n in L:
        res *= n
    return res
print(myProduct([2,3,4]))