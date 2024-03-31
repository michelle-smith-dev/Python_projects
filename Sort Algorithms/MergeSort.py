debug = False

def mergesort(arr):
    # print(len(arr))
    if len(arr) < 2:
        return arr
    mid_p = len(arr) // 2  # You're getting the mid index point
    if debug: print("The mid point:", mid_p)
    left = arr[0:mid_p]  # mergesort(arr[0:mid_p])
    # Then splitting up the array into the first index up to but not including the mid point index
    if debug: print("The left array:", left)
    right = arr[mid_p:]  # mergesort(arr[mid_p:])

    mergesort(left)
    mergesort(right)
    # Taking the mid point index to the end of the index
    if debug: print("The right array:", right)
    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            print("left:", left)
            i += 1
        else:
            merged.append(right[j])
            j += 1
            print("right:", right)
    print("merged:", merged)
    remain = right[j:]
    if i < len(left):
        remain = left[i:]
        merged.extend(remain)

    return merged


arr1 = [90, 48, 1, 32, 67, 58, 77]
mergesort(arr1)
# print(arr1)