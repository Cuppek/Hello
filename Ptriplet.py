# pythagorean triplet

for a in range(1,9998):
    for b in range(a,9999):
        c = 10000 - a - b
        if (a**2 + b**2 == c**2):
            print(a, b, c)