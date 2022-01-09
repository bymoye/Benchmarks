function fib(n){
    if (n == 1 || n == 2){
        return 1
    }
    return fib(n-1) + fib(n-2)
}
console.time('fib')
fib(30)
console.timeEnd('fib')