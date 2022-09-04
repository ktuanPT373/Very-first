
def findDuplicate(a):
    seen = {}
    for i in range(len(a)):
        if a[i] in seen:
            return a[i]
        else:
            seen[a[i]] = False 
print(findDuplicate([1,4,3,5,6,6,2]))
b = {}
b[5] = True
b[6] = True
print(b)