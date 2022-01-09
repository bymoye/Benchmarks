public class test{
    public static int fib(int n){
        if (n == 1 || n == 2)return 1;
        return fib(n-1)+fib(n-2);
    }
    public static void main(String[] args) {
        long startTime = System.nanoTime();
        fib(30);
        long endTime = System.nanoTime();
        System.out.println("time: " + (endTime - startTime)/1e+6 + " ms");
    }
}
