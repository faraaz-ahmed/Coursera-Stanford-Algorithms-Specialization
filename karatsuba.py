# efficient way to multiply two numbers say x, y
# let x = 10^(n/2)a + b
# and y = 10^(n/2)c + d
# then the product x*y can be recursively computed as
# => xy = 10^(n)ac + 10^(n/2)(ad + bc) + bd
# but we know, (a + b)(c + d) = ac + bd + ad + bc
# using this we can reduce the number of calls from 4 to 3 
# => xy = 10^(n)ac + 10^(n/2)[(a + b)(c + d) - (ac + bd)] + bc
# let z0 = ac, z1 = bd, z2 = (a + b)(c + d)
# => xy = 10^(n)z0 + 10^(n/2)(z2 - z1 - z0) + z1 

def karatsuba(x, y):
    strx, stry = str(x), str(y)
    if x < 10 or y < 10:
        return x * y
    else:
        length = len(str(x))
        position = int(length / 2) if (length % 2 == 0) else int(length / 2 + 1)
        a, b, c, d = int(strx[:int(length / 2)]), int(strx[int(length / 2):]), int(stry[:int(length / 2)]), int(stry[int(length / 2):])
        z0, z1, z2 = karatsuba(a, c), karatsuba(b, d), karatsuba((a + b), (c + d)) 
        return 10 ** (2 * position) * z0 + 10 ** (position) * (z2 - z1 - z0) + z1 

# main script
print(karatsuba(122, 122))