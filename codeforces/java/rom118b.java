import java.util.*;

public class rom118b {
    public static String line(int n) {
        if (n == 0) return "0";
        return n+" "+line(n-1);
    }
    public static String bline(int n, int l) {
        if (l == 0) return "";
        if (n == l) return "";
        return n+" "+bline(n+1,l);
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        for (int i = 0; i < n+1; i++) {
            String sp = "";
            for (int j = 0; j < 2*n-2*i; j++) {
                sp += " ";
            }
            System.out.print(sp);
            System.out.println(bline(0,i)+line(i));
        }

        for (int i = n-1; i >= 0; i--) {
            String sp = "";
            for (int j = 0; j < 2*n-2*i; j++) {
                sp += " ";
            }
            System.out.print(sp);
            System.out.println(bline(0,i)+line(i));
        }

    }
}