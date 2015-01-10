import java.util.Scanner;
class numberSteps {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int sum,x,y,t = s.nextInt();
		for (int tt = 0; tt < t; tt++) {
			x = s.nextInt();
			y = s.nextInt();
			sum = x + y;
			boolean isEven = (sum/2) % 2 == 0;
			if (x == y) {
				if (isEven) System.out.println(sum);
				else System.out.println(sum-1);
			}
			else if (x - 2 == y) {
				if (isEven) System.out.println(sum-1);
				else System.out.println(sum);
			}
			else {
				System.out.println("No Number");
			}
		}
	}
}