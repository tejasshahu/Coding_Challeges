# Fibonacci series for given number = 5
# 0, 1, 1, 2, 3
# test case1: 0 -> 0
# test case2: 1 -> 1
# test case3: 5 -> 0, 1, 1, 2, 3

def get_fibonacci_series_n_element(n):
    if n <= 1:
        return n
    else:
        return get_fibonacci_series_n_element(n-1) + get_fibonacci_series_n_element(n-2)

def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    return sequence[:n]

def fibonacci_series(n):
    a, b = 0, 1
    print(f"First {n} Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


if __name__ == '__main__':
    n = 5
    print(f"Fibonacci series's {n}th element:", get_fibonacci_series_n_element(n-1))
    print(f"First {n} Fibonacci Series:", fibonacci_sequence(n))
    print(fibonacci_series(n))
