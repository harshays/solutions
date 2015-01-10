import java.util.*;

public class tram116a {

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int p = 0;
        int min = 0;
        for (int i = 0; i < n; i++) {
            int exit = s.nextInt();
            int enter = s.nextInt();
            p += (enter-exit);
            if (p > min) min = p;
        }
        System.out.println(min);
    }
}