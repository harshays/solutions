import java.util.*;

public class chat58a {

    public static boolean isMatch(String h,String s) {
        int pos = 0;
        for (int i = 0; i < s.length(); i++) {
            if (h.charAt(pos) == s.charAt(i)) ++pos;
            if (pos == h.length()) return true;
            else if (pos >= h.length()) return false;
        }
        return false;
    }



    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String s1 = s.next();
        s1.toLowerCase();
        if (isMatch("hello",s1)) System.out.println("YES");
        else System.out.println("NO");
    }
}