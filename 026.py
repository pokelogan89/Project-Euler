import numpy as np

def main(num):
    max_val = (0,0)
    for i in range(2,num):
        path = np.zeros(num)
        value = 1
        pos = 0

        while path[value] == 0 and value != 0:
            if max_val[1] > i:
                break

            path[value] = pos
            value *= 10
            value %= i
            pos += 1
        if path[value] == 1 and pos > max_val[1] + 1:
            max_val = (i,pos - 1)

    print(max_val)
    return None

main(20)
