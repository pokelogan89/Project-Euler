def main(digits):
    fib = [1,1]
    i = 0
    while len(str(fib[-1])) < digits:
        fib.append(fib[i] + fib[i + 1])
        i += 1
    return len(fib), fib[-1]

print(main(1000))
