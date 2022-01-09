public class sort{
    public static int[] bubleSort(int[] arr){
        int length = arr.length;
        int temp = 0;
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        return arr;
    }
    public static void main(String[] args) {
        int[] arr = new int[10000];
        for (int i = 0; i < 10000; i++) {
            arr[i] = (int)(Math.random() * 1000);
        }
        long startTime = System.nanoTime();
        bubleSort(arr);
        long endTime = System.nanoTime();
        System.out.println("time: " + (endTime - startTime)/1e+6 + " ms");
    }
}
