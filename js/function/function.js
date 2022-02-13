var b = 0;
var c = 0;
function a(a){
    if (a % 2 == 0) {
        b+=1;
    }else{
        c+=1;
    }
}
for (let n = 0;n<5;n++){
    let startTime = performance.now();
    for (let i = 0;i < 100000;i++){
        a(i);
    }
    console.log(performance.now() - startTime);
    console.log(b,c);
}