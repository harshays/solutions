import java.util.Scanner;
class addingReverse {

	public static int reverse(int number) {
		String string_number = number + "";
		int l = string_number.length();
		String reversed = "";
		for (int i = l-1; i >= 0; i--) {
			reversed+=(string_number.charAt(i)+"");
		}
		int reversed_int = Integer.parseInt(reversed);
		return reversed_int;
	}

	public static void main(String[] args) {
		int a,b,sum;
		Scanner s = new Scanner(System.in);
		int t = s.nextInt();
		for (int i = 0; i < t; i++) {
			a = s.nextInt();
			b = s.nextInt();
			a = reverse(a);
			b = reverse(b);
			sum = a + b;
			sum = reverse(sum);
			System.out.println(sum);
		}
	}
}