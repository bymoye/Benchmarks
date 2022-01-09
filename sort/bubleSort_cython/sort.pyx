import cython
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef bubleSort(int[:] arr):
    cdef int length = len(arr)
    cdef int i = 0
    cdef int j = 0
    with nogil:
        for i in range(length - 1):
            for j in range(length - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr