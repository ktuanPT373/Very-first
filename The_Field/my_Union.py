def myUnion(L):
    res = L[0]
    for n in L:
        res = res & n
    return res
test = [{1,3,2},{1},{3,4,1,5}]
print(myUnion(test))