import timeit
time = timeit.Timer(stmt="fib(30)",setup="from fibonacci import fibonacci as fib").timeit(number=1)
print(time*1000,'ms')