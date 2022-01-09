## 环境
> 系统：Fedora 34

> CPU： AMD EPYC 7K62 (2) @ 2.595GHz 

> PHP： 8.1.0  JIT (1205)

## 测试
> 测试方法： 通过cil,取最优的一组数据进行.

|                  | Max(ms) | Min(ms) | Avg(ms) |
| ---------------- | ------- | ------- | ------- |
| 匿名函数(不传参) | 0.19    | 0.08    | 0.10    |
| 普通函数(不传参) | 0.13    | 0.01    | 0.03    |
| 匿名函数(传参)   | 0.19    | 0.08    | 0.10    |
| 普通函数(传参)   | 0.11    | 0.01    | 0.03    |

![echo](https://raw.githubusercontent.com/bymoye/Benchmarks/main/php/function/function.png)