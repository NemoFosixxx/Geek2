def print_numbers(m, n):
    if m > n:
        return
    print(m)
    print_numbers(m + 1, n)

m = 5
n = 10

print_numbers(m, n)
