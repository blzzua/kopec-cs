from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        return self == other

    def __lt__(self, other: Any) -> bool:
        return (self < other) and self != other

    def __gt__(self, other: Any) -> bool:
        return (not self < other) and self != other

    def __le__(self, other: Any) -> bool:
        return (not self < other) or self == other

    def __ge_(self, other: Any) -> bool:
        return not self < other
        pass

def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
            print(f"not found at high={high} mid={mid} low={low}. go up")
        elif sequence[mid] > key:
            print(f"not found at high={high} mid={mid} low={low}. go down")
            high = mid - 1
        else:
            print(f"found at high={high} mid={mid} low={low}")
            return True

    return False



if __name__ == "__main__":
    sorted_list = [x for x in range(512)]
    print(binary_contains(sorted_list, 341))
    print(binary_contains(sorted_list, 516))


