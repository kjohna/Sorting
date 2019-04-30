# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # loop for # of total elements
    for i in range(0, elements):
        # if arrA[0] < arrB[0], merged_arr[i] = arrA.pop(0)
        if arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
            # if arrA is now empty:
            if not len(arrA):
                arrA.append(float('Inf'))
        # else merged_arr[i] = arrB.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)
            # if arrB is now empty:
            if not len(arrB):
                arrB.append(float('Inf'))
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        arrA = merge_sort(arr[:len(arr) // 2])
        arrB = merge_sort(arr[len(arr) // 2:])
        merge(arrA, arrB)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
