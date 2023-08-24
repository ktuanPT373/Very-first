def my_func_composition(f,g):
    return {g[f[a]]:a for a in f}
f = {0:'a',1:'b'}
g = {'a':'apple','b':'banana'}
print(my_func_composition(f,g))
