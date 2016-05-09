import java.util.Scanner;
class hangover {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		double cardLen = s.nextDouble();
		double i = 2.0;
		int count = 0;
		double currentLen = 0.0;
		while (cardLen != 0.00) {
			while (currentLen < cardLen) {
				currentLen+=(1/i++);
				count++;
			}
			System.out.println(count+" card(s)");
			cardLen = s.nextDouble();
			currentLen = 0.0;
			i = 2.0;
			count = 0;
		}
	}
}