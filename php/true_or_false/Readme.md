# 结论
不管是否开启JIT
if else的格式都是最快的

三目运算符在JIT下仅次于if else
但是，没有开启JIT的情况下是三种方法中最慢的

JIT： if_else > ?: > !!
!JIT: if_else > !! > ?: