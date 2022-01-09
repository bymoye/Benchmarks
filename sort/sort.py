import timeit
import random
test_array = [random.randint(0, 1000) for i in range(10000)]
def bubleSort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
time = timeit.Timer(stmt="bubleSort(test_array)",setup="from __main__ import bubleSort,test_array").timeit(number=1)
print(time*1000,'ms')