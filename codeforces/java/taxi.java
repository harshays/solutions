import java.util.*;

public class taxi {
    public static int s1c(int s1) {
        if (s1 <= 0) return 0;
        int x = (s1 % 4 == 0) ? 0 : 1;
        return s1/4+x;
    }

    public static void main(String[] args) {
        int s1 = 0, s2 = 0, s3 = 0, s4 = 0;
        Scanner s = new Scanner(System.in);
        int g = s.nextInt();
        int[] grp = new int[g];
        for (int i = 0; i < g; i++) {
            grp[i] = s.nextInt();
        }
        for (int i = 0; i < g; i++) {
            if (grp[i] == 1) s1++;
            else if (grp[i] == 2) s2++;
            else if (grp[i] == 3) s3++;
            else s4++;
        }
        int s13 = Math.min(s1,s3);
        int total = (s4+s2/2+s13);
        s1 -= s13; 
        s3 -= s13;
        s2 = s2%2; // can be 1 2 or 0 2
        if (s2 == 0) {
            if (s1 > 0) {
                total += s1c(s1);
            }
            else if (s3 > 0) {
                total += s3;
            }
        }
        else if (s2 == 1) {
            if (s3 > 0) {
                total += s3+1;
            }
            else if (s1 > 0) {
                total += 1+s1c(s1-2);
            }
            else if (s1 == s3) {
                total += 1;
            }
        }
        System.out.println(total);


    }
}