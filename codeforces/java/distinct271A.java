import java.util.*;

public class distinct271A {

    public static boolean distinct(String year) {
        for (int i = 0; i < year.length(); i++) {
            for (int j = i+1; j < year.length(); j++) {
                if (year.charAt(i) == year.charAt(j)) return false;
            }
        }
        return true;
    }

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        int y = s.nextInt();
        boolean d = false;
        while (!d) {
            d = distinct(++y+"");
        }
        System.out.println(y);

    }
}