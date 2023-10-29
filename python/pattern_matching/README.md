旨在确认在python3.12版本中对传入不同类型的属性做不同的操作时, 
if early return
match case
dict_lookup

三种方式的性能差异

结果是: dict_lookup > if early return > match case

match case 与 switch case不同, 特别是在执行方面, match case的优化空间很大.