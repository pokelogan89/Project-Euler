from time import time

def collatz(max_limit):
    t0 = time()
    l_max = (0,0)
    for i in range(2,max_limit):
        i_mut = i
        l = 1
        while i_mut > 1:
            if i_mut%2 == 0:
                i_mut /= 2
                l += 1
            else:
                i_mut = 3*i_mut + 1
                l += 1
        if l > l_max[1]:
            l_max = (int(i),l)
    print(l_max)
    p_time = (time() - t0)*1000
    print("Processing time is %d ms" %p_time)

collatz(1000000)