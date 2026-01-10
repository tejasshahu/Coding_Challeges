def fibonacci_series(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_series(n-1) + fibonacci_series(n-2)

if __name__ == '__main__':
    n = 6
    print(fibonacci_series(n))