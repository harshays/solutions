import java.util.*;

public class learn472a {
    public static boolean isPrime(int n) {
        for (int i = 2; i < (int) Math.sqrt(n) + 1; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }


    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        for (int i = 4; i < n; i++) {
            if (!isPrime(i)) {
                if (!isPrime(n-i)) {
                    System.out.println(i+" "+(n-i));
                    break;
                }
            }
        }

    }
}