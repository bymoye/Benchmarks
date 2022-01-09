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

|        | Max(ms) | Min(ms) | Avg(ms) |
| ------ | ------- | ------- | ------- |
| Python | 7713.81 | 7449.63 | 7542.58 |
| Go     | 113.63  | 101.21  | 106.62  |
| Nodejs | 199.50  | 169.04  | 185.55  |
| java   | 179.00  | 163.29  | 166.57  |
| cython | 120.95  | 100.50  | 111.49  |
| php    | 2788.79 | 2645.78 | 2716.64 |

![sort](https://github.com/bymoye/Benchmarks/blob/master/sort/sort.png)