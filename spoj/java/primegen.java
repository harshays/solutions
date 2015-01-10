import java.util.Scanner;
class primegen {
	public static boolean checkPrime(int n) {
		int limit = (int) Math.sqrt(n) + 1;
		for (int i = 2; i <= limit; i++) {
			if (n % i == 0) return false;
		}
		return true;
		
	}
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int t = s.nextInt();
		for (int j = 0; j < t; j++) {
			int a = s.nextInt();
			int b = s.nextInt();
			for (int i = a; i <= b; i++) {
				if (checkPrime(i)) System.out.println(i);
			}

	}
}
}