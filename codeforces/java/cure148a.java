import java.util.*;

public class cure148a {

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        int k = s.nextInt(), l = s.nextInt(), m = s.nextInt(), n = s.nextInt(), d = s.nextInt();
        boolean[] tal = new boolean[d];
        int[] no = new int[d];
        for (int i = 0; i < tal.length; i++) {
            tal[i] = true;
            no[i] = i+1;
        }
        for (int i = 0; i < tal.length; i++) {
            if (no[i] % k == 0 || no[i] % l == 0 || no[i] % m == 0 || no[i] % n == 0) tal[i] = false;
        }
        int c = 0;
        for (int i = 0; i < tal.length; i++) {
            if (tal[i] == false) c++;
        }
        System.out.println(c);

    }
}