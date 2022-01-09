import timeit
import random
import numpy as np
from bubleSort import bubleSort
import cython
arr = [random.randint(0, 1000) for i in range(10000)]
arr = np.array(arr)
time = timeit.Timer(stmt = "bubleSort(arr)", setup = "from __main__ import bubleSort,arr").timeit(number=1)
print(time*1000,'ms')