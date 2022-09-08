def powerSum(x, n):
    if n == 0:
        return 1
    else:
        partial = powerSum(x, n//2)
        result = partial * partial
        if n%2 == 1:
            result *= x
        return result
print(powerSum(2,1000))