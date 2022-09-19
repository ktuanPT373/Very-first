 

def isPowerOfTwo(n):
    if n == 1:
        return True
    else:
        if n % 2 == 0:
            return isPowerOfTwo(n/2)
        else:
            return False
print(isPowerOfTwo(2))