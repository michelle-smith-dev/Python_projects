def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)


i = j = k = 0

while i < len(left) and j < len(right):
    if left[i] < right[j]:
        arr[k] = left[i]
        i += 1


else:
    arr[k] = right[j]
    j += 1
k += 1

while i < len(left):
    arr[k] = left[i]
    i += 1
    k += 1

while j < len(right):
    arr[k] = right[j]
    j += 1
    k += 1


def print_array(arr):
    """Prints the elements of an array."""

    for element in arr:
        print(element, end=" ")
    print()


# Example usage
arr = [32, 45, 67, 2, 7]
print("Given array:")
print_array(arr)

merge_sort(arr)

print("\nSorted array:")
print_array(arr)