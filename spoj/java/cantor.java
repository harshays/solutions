import java.util.Scanner;
class cantor {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int t = s.nextInt();
		int index = 0;
		int n;
		int[] x = new int[90000100];
		int[] y = new int[90000100];
		x[index] = 1;
		y[index] = 1;
		for (int i = 0; i < t; i++) {
			n = s.nextInt();

			while (index+1 < n) {
				x[++index] = x[index-1]+1;
				y[index] = y[index-1]; 
				System.out.println("INDEX IS "+index);
				while (x[index] != 1) {
					x[++index] = x[index-1]-1;
					y[index] = y[index-1]+1;
				}

				x[++index] = x[index-1];
				y[index] = y[index-1]+1;

				while (y[index] != 1) {
					x[++index] = x[index-1]+1;
					y[index] = y[index-1]-1;
				}
			}
			System.out.println("TERM "+n+" IS "+y[n-1]+"/"+x[n-1]);
		}
	}
}