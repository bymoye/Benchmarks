<?php
function bubleSort($arr){
    $length = count($arr);
    for ($i = 0; $i < $length; $i++){
        for ($j = 0; $j < $length - $i - 1; $j++){
            if ($arr[$j] > $arr[$j + 1]){
                $tmp = $arr[$j];
                $arr[$j] = $arr[$j + 1];
                $arr[$j + 1] = $tmp;
            }
        }
    }
}
$arr = array();
for ($i = 0; $i < 10000; $i++){
    $arr[] = rand(1, 1000);
}
$start_time = hrtime(true);
bubleSort($arr);
$endtime = hrtime(true);
echo ($endtime - $start_time)/1e+6," ms\n";