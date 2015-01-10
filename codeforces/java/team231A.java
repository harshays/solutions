import java.util.*;

public class team231A {

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int p = 0;

        for (int i = 0; i < n; i++ ) {
            int a = s.nextInt(), b = s.nextInt(), c = s.nextInt();
            int sum = a + b + c;
            if (sum >= 2) p++;
        }

        System.out.println(p);
    }
}