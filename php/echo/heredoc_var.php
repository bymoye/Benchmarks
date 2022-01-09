<?php
$temp = 'Hello World';
for ($i = 0; $i < 10;$i++){
    $startTime = hrtime(true);
    for ($j = 0; $j < 10000;$j++){
        echo <<<EOF
        <p style="display:none">$temp</p>
EOF;
    }
    $endTime = hrtime(true);
    $count = $i+1;
    echo "第{$count}次：".($endTime - $startTime)/1e+6 . " ms<br>";
}