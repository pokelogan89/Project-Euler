from math import factorial
import numpy as np
import time

mod_nums = []
def fact_finder(max_limit):
    t0 = time.time()
    nums = np.arange(3,max_limit + 1)
    for i in nums:
        n_mod = 0
        n_st = str(i)
        for x in range(len(n_st)):
            n_mod += factorial(int(n_st[x]))
        if n_mod == i:
            mod_nums.append(n_mod)
    
    s_time = (time.time() - t0)*1000
    print(sum(mod_nums))
    print("Processing time was %d ms" %s_time)
    
    return None

fact_finder(100000)
