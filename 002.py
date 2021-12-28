def main(max):
    fib = [1,2]
    sum = 0
    i = 1
    while fib[i] <= max:
        fib.append(fib[i] + fib[i - 1])
        if fib[i]%2 == 0:
            sum = sum + fib[i]
        i+=1
    print(sum)
    return None

main(4000000)