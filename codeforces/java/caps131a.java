import java.util.*;

public class caps131a {

    public static void main(String args[]) {
        Scanner w = new Scanner(System.in);
        String s = w.next();
        if (s.equals(s.toUpperCase())) {
            System.out.println(s.toLowerCase());
        } else if (s.charAt(0) > 95 && s.substring(1).equals(s.substring(1).toUpperCase())) {
            System.out.println((s.charAt(0)+"").toUpperCase()+s.substring(1).toLowerCase());
        }
        else System.out.println(s);
    }
}