from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib4(n-2) + fib4(n-1)

if __name__ == '__main__':
    for i in range(200,600):
        print(i, fib4(i))
