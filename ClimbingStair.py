from telnetlib import theNULL


def climbStairs(n):
        
    if n == 1 or n == 2:
        return n
    
    before = 1
    then = 2
    now = 0
    
    for step in range(3, n+1):
        now = before + then
        before = then
        then = now

    return now
print(climbStairs(7))