import java.util.*;

public class matrix263a {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int[][] m = new int[5][5];
        int tx = 0, ty = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                m[i][j] = s.nextInt();
                if (m[i][j] == 1) {
                    tx = i;
                    ty = j;
                }
            }
        }
        int r = Math.abs(2-tx)+Math.abs(2-ty);
        System.out.println(r);
    }
}