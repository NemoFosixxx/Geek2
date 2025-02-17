def print_numbers(m, n):
    if m > n:
        return
    print(m)
    print_numbers(m + 1, n)

M = 5
N = 10

print_numbers(M, N)