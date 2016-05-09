import java.util.Scanner;
class feynman {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int squares;
		while (n != 0) {
			squares = (n*(n+1)*(2*n+1))/6;
			System.out.println(squares);
			n = s.nextInt();
		}
	}
}