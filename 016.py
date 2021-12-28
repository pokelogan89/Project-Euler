from numpy.linalg.linalg import solve


def main(num,deg):
    ex = str(num**deg)
    sol = 0
    for i in range(len(ex)):
        sol += int(ex[i])
    return sol

print(main(2,1000))