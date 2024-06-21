# def bubbleSort(array):
#     swaped =False
#     for i in range(len(array)):
#         for j in range(0, len(array) -i -1):
#             if array[j] > array[j+1]:
#                 array[j],array[j+1] = array[j+1], array[j]
#                 swaped = True
#             if not swaped:
#                 return array 

#     return array




# i =0
# while i < len(arr):
#     min_value = i
#     j=i+1
#     while j < len(arr):
#         if arr[j] <arr[min_value]:
#             min_value=j
#         j+=1
#     if min_value !=i:
#         arr[i],arr[min_value]=arr[min_value],arr[i]
#     i+=1
# print(arr,end=" ")


def bubbleSort(array):
    swapped = False
    # this loop for iteration
    for i in range(len(arr)):
        # this loop for comparesion(adjecent elements)
        for j in range(0, len(arr) -i -1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        if not swapped:
            return array



    return array



arr = [28, 1, 1, 3, -5 , 8]

res= bubbleSort(arr)
print(res)



