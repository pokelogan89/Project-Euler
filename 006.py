def main(num):
    sum_sq = 0
    sum = 0
    for i in range(num + 1):
        sum += i
        sum_sq += i**2
    sol = abs(sum_sq - sum**2)

    return sol

print(main(100))