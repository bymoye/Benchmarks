from supportWebp import check_Version
import re
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'

version_list = {'Firefox':65,
                'Chrome':32,
                'Edge':18,
                'AppleWebKit':605,
                'OPR':19, # Safari 14
                'UCBrowser':12,
                'SamsungBrowser':4,
                'QQBrowser':10,
            }
regexp1 = re.compile(r'(Firefox|Chrome|Edge|AppleWebKit|OPR|UCBrowser|SamsungBrowser|QQBrowser)\/(\d+)')
regexp2 = re.compile(r'(\d+)')
def programme1(ua:str) -> bool:
    e = re.findall(regexp1, ua)
    for i,j in e:
        if version_list[i] < int(j):
            return True
    return False

def programme2(ua:str) -> bool:
    for i in version_list:
        n = ua.find(i)
        if n != -1:
            temp = re.match(regexp2, ua[n + len(i) + 1:]).group()
            if int(temp) >= version_list[i]:
                return True
    return False

num_list = [str(i) for i in range(10)]
def programme3(ua:str) -> bool:
    for i in version_list:
        n = ua.find(i)
        if n!= -1:
            sub = n + len(i) + 1
            temp = ''
            while(ua[sub] in num_list):
                temp += ua[sub]
                sub += 1
            if int(temp) >= version_list[i]:
                return True
    return False
from timeit import Timer
time1 = Timer(stmt="programme1(user_agent)", setup="from __main__ import programme1, user_agent").timeit(number=10000)
time2 = Timer(stmt="programme2(user_agent)", setup="from __main__ import programme2, user_agent").timeit(number=10000)
time3 = Timer(stmt="programme3(user_agent)", setup="from __main__ import programme3, user_agent").timeit(number=10000)
time4 = Timer(stmt="check_Version(bytes(user_agent, encoding = 'utf8'))", setup="from __main__ import check_Version, user_agent").timeit(number=10000)
print('''
      纯正则表达式结果：%s,
      混合索引结果：%s,
      纯python结果：%s,
      Cython结果：%s
      ''' % (programme1(user_agent), programme2(user_agent), programme3(user_agent), check_Version(bytes(user_agent, encoding = 'utf8'))))
print('''
      纯正则表达式执行1000次结果：%s ms,
      混合索引执行1000次结果：%s ms,
      纯python执行1000次结果：%s ms,
      Cython执行1000次结果：%s ms
      ''' % (time1 * 1000, time2 * 1000, time3 * 1000, time4 * 1000))