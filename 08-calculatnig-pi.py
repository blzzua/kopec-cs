
def caclulate_pi(n_terms: int ) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for i in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi

if __name__ == '__main__':
    print(caclulate_pi(100_000))
    print(caclulate_pi(1000_000))
    print(caclulate_pi(10_000_000))
    print(caclulate_pi(100_000_000))
    print(caclulate_pi(1000_000_000))
    """
    3.1415826535897198
    3.1415916535897743
    3.1415925535897915
    3.141592643589326
    3.1415926525880504
 pi=3,14159265358979323846
    """