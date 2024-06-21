def quickSort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quickSort(left) + middle + quickSort(right)





array = [98, 3, 2, -43, 34, 3]
sorted_list = quickSort(array)
print(sorted_list)
