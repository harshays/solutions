import java.util.*;

public class socks460a {

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int m = s.nextInt();
        int c = 0;
        while (n-- > 0) {
            c++;
            if (c % m == 0) n++;
        }
        System.out.println(c);
    }
}