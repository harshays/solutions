import java.util.*;

public class q266b {

    public static void swap(char[] a, int i, int j) {
        char temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt(), swaps = s.nextInt();
        char[] qs = s.next().toCharArray();
        while (swaps != 0) {
            for (int i = 0; i < qs.length-1; i++) {
                if (qs[i] < qs[i+1]) {
                    swap(qs,i,i+1);
                    i++;
                }
            }
            swaps--;
        }
        String a = "";
        for (int i = 0; i < qs.length; i++) {
            a += (qs[i]+"");
        }
        System.out.println(a);

    }
}