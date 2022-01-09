function bubleSort(arr){
    length = arr.length
    for (let i = 0; i < length; i++) {
        for (let j = 0; j < length - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            }
        }
    }
    return arr
}
var test_arr = [];
for (let i = 0; i < 10000; i++) {
    test_arr[i] = Math.floor(Math.random() * 10000)
}
console.time('bubbleSort')
bubleSort(test_arr)
console.timeEnd('bubbleSort')