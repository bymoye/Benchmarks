from randint import randint as cutrand
from Pyewacket import randint
from random import randint as randint1
from random import choice
from fastrand import pcg32bounded
from Fortuna import random_int
from numpy.random import randint as nrand
print('%',[pcg32bounded(101) for _ in range(10)])
print('@',[randint(0,100) for _ in range(10)])
print('#',[randint1(0,100) for _ in range(10)])
print('&',[random_int(0,100) for _ in range(10)])
print('^',[nrand(0,100) for _ in range(10)])
print('*',[cutrand(0,100) for _ in range(10)])
import timeit
time3 = timeit.Timer(stmt="pcg32bounded(101)",setup="from fastrand import pcg32bounded").timeit(1000000)
time1 = timeit.Timer(stmt="randint(0,100)",setup="from Pyewacket import randint").timeit(1000000)
time2 = timeit.Timer(stmt="randint(0,100)",setup="from random import randint").timeit(1000000)
time4 = timeit.Timer(stmt="random_int(0,100)",setup="from Fortuna import random_int").timeit(1000000)
time10 = timeit.Timer(stmt="randint(0,100)",setup="from numpy.random import randint").timeit(1000000)
time11 = timeit.Timer(stmt="randint(0,100)",setup="from randint import randint").timeit(1000000)
print('——————————randint：10000000——————————')
print('fastrand.pcg32bounded ：',time3*1000,' ms')
print('Pyewacket.randint ：',time1*1000,' ms')
print('random.randint ：',time2*1000,' ms')
print('Fortuna.random_int ：',time4*1000,' ms')
print('numpy.randint ：',time10*1000,' ms')
print('cutrand ：',time11*1000,' ms')
temp = ['a','b','c','d','e','f','g','h','j','k']
temp_len = len(temp)
len2 = temp_len-1
print('!',[temp[pcg32bounded(temp_len)] for _ in range(10)])
print('!!',[temp[randint(0,len2)] for _ in range(10)])
print('!!!',[temp[randint1(0,len2)] for _ in range(10)])
print('!!!!',[temp[random_int(0,len2)] for _ in range(10)])
print('!!!!!',[choice(temp) for _ in range(10)])
time5 = timeit.Timer(stmt="temp[pcg32bounded(temp_len)]",setup="from __main__ import pcg32bounded,temp,temp_len").timeit(1000)
time6 = timeit.Timer(stmt="temp[randint(0,len2)]",setup="from __main__ import randint,temp,len2").timeit(1000)
time7 = timeit.Timer(stmt="temp[randint1(0,len2)]",setup="from __main__ import randint1,temp,len2").timeit(1000)
time8 = timeit.Timer(stmt="temp[random_int(0,len2)]",setup="from __main__ import random_int,temp,len2").timeit(1000)
time9 = timeit.Timer(stmt="choice(temp)",setup="from __main__ import choice,temp,temp_len").timeit(1000)
print('——————————list：10000000——————————')
print('fastrand.pcg32bounded ：',time5*1000,' ms')
print('Pyewacket.randint ：',time6*1000,' ms')
print('random.randint ：',time7*1000,' ms')
print('Fortuna.random_int ：',time8*1000,' ms')
print('random.choice ：',time9*1000,' ms')