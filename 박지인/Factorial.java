package 박지인;

public class Factorial {

    //반복적으로 구현한 팩토리얼
    public static int factorial_iterative(int n) {
        int result = 1;
        for (int i = 1; i < n + 1; i++) {
            result *= i;
        }
        return result;
    }

    public static int factorial_recursive(int n) {
        if (n <= 1) {//종료 조건
            return 1;
        }
        return n * factorial_recursive(n - 1);
    }

    
    public static void main(String[] args) {
        System.out.println("반복적으로 구현: "+factorial_iterative(5));
        System.out.println("재귀적으로 구현: "+factorial_recursive(5));


    }
    
}
