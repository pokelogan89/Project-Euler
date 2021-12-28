from numpy import arange
from time import time

def P5_generator(infun):
    for onum in infun:
        for inum in infun:
            yield onum,inum

def main(max_limit):
    t0 = time()
    nums = []
    s_set = []
    d_set = []
    P5 = list(map(lambda x: x*(3*x - 1)/2,arange(1,max_limit + 1)))
    
    for i in range(2):
        for onum,inum in P5_generator(P5):
            D = abs(onum - inum)
            if D == 0:
                continue
            S = onum + inum
            if D in P5:
                d_set.append(D)
            else:
                continue
            if S in P5 and S not in nums:
                nums.append(D)

    print(nums.sort())
    print(P5[:20])
    p_time = (time() - t0)*1000
    print("Processing time was %d ms" %p_time)

    return None

main(2200)