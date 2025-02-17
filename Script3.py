def reverse_print(arr, i=None):
    if i is None:
        i = len(arr) - 1
    if i < 0:
        return
    print(arr[i])
    reverse_print(arr, i - 1)

arr = [1, 2, 3, 4, 5]
reverse_print(arr)