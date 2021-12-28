import operator as op

def main(max):
    num = []
    max = range(max)
    for x in max:
        if (op.mod(x,3) == 0 or op.mod(x,5) == 0):
            num.append(x)
    sol = sum(num)
    print(sol)
    return None

main(1000)