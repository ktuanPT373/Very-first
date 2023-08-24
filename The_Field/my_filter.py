def my_filter(L,num):
    return [n for n in L if n%num != 0]
print(my_filter([1,2,4,5,7],2))