def row(p, n):
    return [p+i for i in range(n)]
# no row(p, n):
ans = [[i+j for j in range(20)] for i in range(15)]
# row(p, n):
res = [row(i,20) for i in range(15)]
print(ans == res)