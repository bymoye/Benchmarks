## 环境
> 系统：Windows 11

> CPU： Intel(R) Core(TM) i5-8400

> Java： 15

> Python： 3.10

> php： 8.1

> go： 1.17

> nodejs： 16.13.1

## 测试
> 测试方法： 进行十次测试，取最高值和最低值。越低越好。

|          | Max(ms) | Min(ms) | Avg(ms) |
| -------- | ------- | ------- | ------- |
| Python   | 205.94  | 194.80  | 201.04  |
| Go       | 3.29    | 2.24    | 2.79    |
| Nodejs   | 9.58    | 8.52    | 8.95    |
| java     | 3.32    | 2.58    | 3.06    |
| cython   | 10.36   | 8.21    | 9.04    |
| cython_c | 3.58    | 3.23    | 3.28    |
| php      | 101.27  | 87.03   | 91.62   |

![fib](https://github.com/bymoye/Benchmarks/blob/master/fib/fib.png)