def closestTriangular(T):
    # The sequence starts with 1, 3, 6, 10, 15...
    current_triangular = 0
    x = 1

    # Keep calculating the next triangular number
    while True:
        next_triangular = (x * (x + 1)) // 2

        # If the next number exceeds T, the current one is the closest
        if next_triangular > T:
            break

        current_triangular = next_triangular
        x += 1

    return current_triangular


print(closestTriangular(T=5))