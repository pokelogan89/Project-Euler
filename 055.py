from time import time
from numpy import arange

def lychrel(n):
    i = 0
    nm = n
    l = 0
    while i < 50:
        nm_rev = int(str(nm)[::-1])
        nm += nm_rev
        if nm == int(str(nm)[::-1]):
            break
        i += 1
        if i == 50:
            l = 1
    
    return l

def main(max_limit):
    t0 = time()
    num = 0
    lyc = list(arange(1,max_limit + 1)) 
    for i in lyc:
        num += lychrel(int(i))

    print(num)
    p_time = (time() - t0)*1000
    print("Processing time is %d ms" %p_time)

    return None

main(10000)