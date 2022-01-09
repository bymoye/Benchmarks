## 环境
> 系统：Fedora 34

> CPU： AMD EPYC 7K62 (2) @ 2.595GHz 

> PHP： 8.1.0  JIT (1205)

## 测试
> 测试方法： 通过php-fpm,取最优的一组数据进行.

### 不带变量
|                | Max(ms) | Min(ms) | Avg(ms) |
| -------------- | ------- | ------- | ------- |
| 单引号         | 0.48    | 0.39    | 0.42    |
| 双引号         | 0.60    | 0.39    | 0.45    |
| html直出(混合) | 0.58    | 0.47    | 0.51    |
| nowdoc         | 0.63    | 0.38    | 0.45    |
| heredoc        | 0.61    | 0.45    | 0.50    |

![echo](https://raw.githubusercontent.com/bymoye/Benchmarks/main/php/echo/echo.png)

### 带变量
|                | Max(ms) | Min(ms) | Avg(ms) |
| -------------- | ------- | ------- | ------- |
| 单引号         | 0.93    | 0.81    | 0.87    |
| 双引号         | 0.96    | 0.83    | 0.87    |
| html直出(混合) | 1.12    | 0.93    | 0.98    |
| heredoc        | 1.63    | 0.87    | 1.02    |

![echo_var](https://raw.githubusercontent.com/bymoye/Benchmarks/main/php/echo/echo_var.png)