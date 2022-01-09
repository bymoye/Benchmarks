<?php
function fib($n){
    if($n == 1 || $n == 2) return 1;
    return fib($n - 1) + fib($n - 2);
}
$start_time = hrtime(true);
fib(30);
$endtime = hrtime(true);
echo ($endtime - $start_time)/1e+6," ms\n";