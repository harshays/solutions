import java.util.Scanner;
public class water4a {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int w = s.nextInt();
        String a = (w % 2 == 0 && w > 2) ? "YES" : "NO";
        System.out.print(a);
    }
}