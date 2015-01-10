import java.util.Scanner;
public class task118a {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String w = s.next().toLowerCase();
        String p = "";
        for (int i = 0; i < w.length(); i++) {
            if (w.charAt(i) == 'a' || w.charAt(i) == 'e' ||w.charAt(i) == 'i' ||w.charAt(i) == 'o' ||w.charAt(i) == 'u' || w.charAt(i) == 'y') p+="";
            else p+=("."+w.charAt(i));
        }
        System.out.println(p);
    }
}