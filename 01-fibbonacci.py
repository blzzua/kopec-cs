def fib1(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

if __name__ == '__main__':
    for i in range(40):
        print(i, fib1(i))
