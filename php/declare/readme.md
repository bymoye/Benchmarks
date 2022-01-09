## 环境
> 系统：Fedora 34

> CPU： AMD EPYC 7K62 (2) @ 2.595GHz 

> PHP： 8.1.0  JIT (1205)

## 测试
> 测试方法： 通过cil,取最优的一组数据进行.

|            | Max(ms) | Min(ms) | Avg(ms) |
| ---------- | ------- | ------- | ------- |
| 声明类型   | 0.17    | 0.06    | 0.08    |
| 不声明类型 | 0.12    | 0.01    | 0.03    |

![declare](https://raw.githubusercontent.com/bymoye/Benchmarks/main/php/declare/declare.png)