import java.util.*;

public class domino50a {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int m = s.nextInt();
        int n = s.nextInt();
        int maxi = Math.max(m,n);
        int mini = Math.min(m,n);
        int res = maxi*(mini/2) + maxi/2*(mini%2);
        System.out.println(res);
    }
}