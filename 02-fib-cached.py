from typing import Dict
fib_cache: Dict[int, int] = {0: 0, 1: 1}

def fib3(n: int) -> int:
    if n not in fib_cache:
        fib_cache[n] = fib3(n-1) + fib3(n-2)
    return fib_cache[n]


if __name__ == '__main__':
    for i in range(100,2566):
        print(i, fib3(i))
