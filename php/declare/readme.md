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

其实从JIT生成的汇编代码来看声明类型是要比不声明类型要少一些步骤的，但是开销更大 原因不明 后续php版本应该会改善