import java.util.Scanner;
public class long71a {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = s.next();
            if (words[i].length() > 10) {
                int l = words[i].length() - 2;
                String w = words[i].charAt(0)+""+l+""+words[i].charAt(words[i].length()-1);
                words[i] = w;
            }
        }
        for (int i = 0; i < n; i++) {
            System.out.println(words[i]);
        }

    }
}