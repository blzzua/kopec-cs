from typing import  Generator
from typing import Dict

def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

if __name__ == '__main__':
    for i in fib6(10000):
        print(i)
