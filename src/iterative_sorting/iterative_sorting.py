# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            # commented tmp var code is equivalent
            # use comma notation instead
            # tmp = arr[j]
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                # arr[j] = arr[i]
                # arr[i] = tmp
    # code below was first attempt. prompt for the assignment came with cur_index and smallest_index defined
        # cur_index = i
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # for j in range(i + 1, len(arr)):
        #     tmp = arr[j]
        #     # if tmp < arr[smallest_index]:
        #     if tmp < arr[i]:
        #         # arr[j] = arr[cur_index]
        #         # arr[cur_index] = tmp
        #         arr[j] = arr[i]
        #         arr[i] = tmp
        #     j += 1

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap = True
    count = 0
    while swap:
        swap = False
        count += 1
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                print(f"{count} swapping: {i}")
                print(arr)
                swap = True
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                print(arr)
                print("----")

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
