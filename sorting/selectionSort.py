def selectionSort(data):
    L = len(data)
    for sp in range(L):
        max_num = sp
        for up in range(sp+1 , L):
            if data[up] < data[max_num]:
                max_num = up
        data[sp], data[max_num] = data[max_num], data[sp]

    return data
    

data = [4, 64, 2 , 453, 1, 33., -45]

print(selectionSort(data))

            