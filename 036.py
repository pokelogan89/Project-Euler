from numpy import arange
import time

def palin_baser(max_limit):
    t0 = time.time()
    b10 = arange(1,max_limit + 1)
    b10_rev = list(map(lambda x: int(str(x)[::-1]),b10))
    b10_pal = []
    
    for i,num in enumerate(b10):
        if num == b10_rev[i]:
            b10_pal.append(num)
    
    b2 = list(map(lambda x: int(bin(x)[2:]),b10_pal))
    b2_rev = list(map(lambda x: int(str(x)[::-1]),b2))
    b2_pal = []
    
    for i,bi in enumerate(b2):
        if bi == b2_rev[i]:
            b2_pal.append(bi)

    b210_pal = list(map(lambda x: int('0b'+ str(x),2),b2_pal))
            
    print(sum(b210_pal))
    p_time = (time.time() - t0)*1000
    print("Processing time was %d ms" %p_time)

    return None

palin_baser(10**6)