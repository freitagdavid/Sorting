# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        if len(arrA) == 0:
            merged_arr[i] = arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        elif arrB[0] < arrA[0]:
            merged_arr[i] = arrB.pop(0)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr)//2:])
        arr = merge(left, right)
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
def timsort( arr ):

    return arr


# num_list = [90,35,100,12,13,64,61,98,41,49,63,11,19,10,34,99,85,57,97,37,54,56,58,9,51,30,45,88,92,71,27,89,70,7,18,40,73,94,14,93,44,65,86,38,60,33,23,36,29,69,75,47,20,59,32,22,1,39,5,48,21,53,77,50,16,4,3,82,79,46,25,96,68,95,26,91,43,17,80,62,66,76,67,81,8,42,6,28,52,24,78,84,55,2,83,15,72,31,87,74]
# num_list = [90, 35, 100, 12, 13]
# print(merge_sort(num_list))
