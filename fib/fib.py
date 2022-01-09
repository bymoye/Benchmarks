import timeit
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)
time = timeit.Timer(stmt="fib(30)",setup="from __main__ import fib").timeit(number=1)
print(time*1000,'ms')