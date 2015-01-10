import java.util.Scanner;

public class NextRound158A {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int k = s.nextInt();
        int count = 0;
        int[] scores = new int[n];
        for (int i = 0; i < n; i++) {
            scores[i] = s.nextInt();
        }
        k = scores[k-1];
        for (int i = 0; i < n; i++) {
            if (scores[i] > 0 && scores[i] >= k) count++;
        }
        System.out.print(count);
    }
}