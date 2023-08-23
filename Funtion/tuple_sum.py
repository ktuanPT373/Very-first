def tuple_sum(A, B):
    return [(a[0]+b[0],a[1]+b[1]) for a,b in zip(A,B)]
A = [(1,2),(10,20)]
B = [(3,4),(30,40)]
print(tuple_sum(A, B))

