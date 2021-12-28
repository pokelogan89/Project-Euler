def main(max):
    min = 1
    min_check = []

    for i in range(2,max + 1):
        if min%i != 0:
            min = min*i
            min_check.append(i)
            for x in min_check:
                if (i%x == 0 and i != x):
                    min_check.remove(x)
                    min = min/x

    print(int(min))  
    return None

main(20)