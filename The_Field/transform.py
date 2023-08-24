def transform(a,b,L):
    return [a*i+b for i in L]
# a. Translate z one unit up and one unit to the right, then rotate ninety degrees clockwise, then scale by two
z = [3 + 4j,2+3j]
print(transform(2j,(1+1j)*2j,z))
# b. Scale the real part by two and the imaginary part by three, then rotate by forty-five 
# defrees counterclockwise, and then translate down two units and left three units
# No way, can not find a, b such that Scale the real part by two and the imaginary part by three.