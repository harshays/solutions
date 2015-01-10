
import java.util.*;

public class valr485b {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        long max_x = s.nextInt(),min_x = max_x, min_y = s.nextInt(), max_y = min_y;
        for (int i = 0; i < n-1; i++) {
            long x = s.nextInt(), y = s.nextInt();
            min_x = Math.min(x,min_x);
            max_x = Math.max(x,max_x);
            min_y = Math.min(y,min_y);
            max_y = Math.max(y,max_y);
        }
        long m = Math.max(Math.abs(max_x-min_x),Math.abs(max_y-min_y));
        System.out.println(m*m);
    }
}