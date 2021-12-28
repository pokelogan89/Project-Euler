def main():
    i = 0
    nums = 0
    while i < 100:
        inp = int(input("Type all of the numbers\n").strip())
        nums += inp
        i += 1
    sol = str(nums)

    return sol[:10]

print(main())