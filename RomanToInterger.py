def romanToInt(s):
    base = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    i =0
    integer = 0
    while i < len(s):
        if i + 1 < len(s) and s[ i: i + 2 ] in base:
            integer += base[s[i:i+2]]
            i += 2
        elif i < len(s):
            integer += base[s[i]]
            i += 1
    return integer

print(romanToInt('XIV'))
