import java.util.*;

public class flip405a {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] v = new int[n];
        for (int i = 0; i < n; i++) {
            v[i] = s.nextInt();
        }
        Arrays.sort(v);
        for (int i = 0; i < v.length; i++) {
            System.out.print(v[i]+" ");
        }
    }
}