
import java.util.*;

public class button268b {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int b = s.nextInt();
        int i = 0, p = 0, n = b;
        while (true) {
            n--;i++;
            if (n == 0) break;
            p += n*i;
        }
        System.out.println(p+b);
    }
}