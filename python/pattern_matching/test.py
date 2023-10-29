import timeit
from if_early_return import if_early_return
from dict_lookup import dict_lookup
from match_case import match_case

# data = "Hello World"
# data = b"hi"
data = list()


print("if_early_return:", timeit.timeit(lambda: if_early_return(data), number=10000000))
print("dict_lookup:", timeit.timeit(lambda: dict_lookup(data), number=10000000))
print("match_case:", timeit.timeit(lambda: match_case(data), number=10000000))
