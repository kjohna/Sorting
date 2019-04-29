# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    while high > 1:
        mid = high // 2
        mid_val = arr[mid]
        if mid_val == target:
            # found
            return mid
        elif mid_val > target:
            # check LHS
            arr = arr[: mid + 1]
        elif mid_val < target:
            # check RHS
            arr = arr[mid + 1:]
        else:
            # ??
            return -1
        high = len(arr) - 1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    mid_val = arr[middle]
    print(f"mid_val: {mid_val}")
    print(f"target: {target}")
    if mid_val == target:
        # found
        print(f"found@{middle}")
        return middle
        print("here?")
    elif mid_val > target:
        # check LHS
        print("check LHS")
        high = middle
        result = binary_search_recursive(arr, target, low, high)
    elif mid_val < target:
        # check RHS
        print("check RHS")
        low = middle
        result = binary_search_recursive(arr, target, low, high)
    else:
        # ??
        return -1

    return result
