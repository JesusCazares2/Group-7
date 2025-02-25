# Bubble sort algo
def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr [j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Merge sort algo
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively apply merge sort on both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two sorted halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Add remaining elements from left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Add remaining elements from right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2] # chose the middle element as a pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# needed for radix sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # count occurences of each digit at the 'exp' place value
    for i in range(n):
        index = (arr[i] // exp) % 10
        count [index] += 1

    # convert count[i] to be the actual position index in our output[]
    for i in range(1,10):
        count[i] += count[i - 1]

    # build array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # copy stored values from output[] into original array
    for i in range(n):
        arr[i] = output[i]

# radix sort
def lsd_radix_sort(arr):
    max_num = max(arr)
    exp = 1 # we are starting with 1's place

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr # return sorted arr

# linear search
def linear_search(arr, search):
    for i in range(len(arr)):
        if arr[i] == search:
            print(f"{arr[i]} was found")
            return i
    return -1