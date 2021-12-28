import time

def pow_finder(max_p):
    t0 = time.time()
    nums = []
    for places in range(1,2*max_p):
        if places*9**max_p < 10**(places - 1):
            max_search = places*9**max_p
            break
    t1 = time.time()
    for i in range(2,max_search + 1):
        l_st = map(lambda l: int(l)**max_p,str(i))
        if sum(l_st) == i:
            nums.append(i)
    p_time = int((time.time() - t0)*1000)
    s_time = int((t1 - t0)*1000)
    print("The numbers whose digits to the power of {} is equal to the number itself are {}, the sum of which is {}, out of a maximum of {}".format(max_p,nums,sum(nums),max_search))
    print("Took %d ms to find solution and %d ms to find bounds" %(p_time,s_time))

    return None

pow_finder(5)
