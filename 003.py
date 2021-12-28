from math import sqrt

def filter(inp):
    pot = []

    for i in range(inp + 1):
        pot.append(i)
    
    p = 2
    while (p*p <= inp):
        if pot[p] > 0:
            for i in range(p**2, inp + 1, p):
                pot[i] = 0
        p += 1
    
    prime = [x for x in pot if x > 0]
    print(prime)
    
    return None

def main(num):
    filter(num)

    return None

main(600851475143)