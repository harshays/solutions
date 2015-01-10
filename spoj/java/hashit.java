import java.util.Arrays;
import java.util.Scanner;
class hashit {
	// find index of the element defined by the key
	// insert new key into table
	// deelete key from table

	String[] keys = new String[101]; // keys[hash value] stores name
	int total_keys = 0;
	
	int Hash(String key) {
		int val = 0,j = 0;

		for (int i = 0; i < key.length(); i++) val+=(((int)key.charAt(i))*(i+1));
		val = (val*19)%101;

		while (keys[val] != null && !keys[val].equals(key)) { //collision
			j++;
			val = (val + j*j + 23*j) % 101;
		}

		return val;
	}

	void add(String key) {
		int val = Hash(key);
		if (keys[val].equals(key)) return;
		keys[val] = key;
		total_keys++;
	}

	void del(String key) {
		int val = Hash(key);
		if (keys[val] != null && keys[val].equals(key)) {
			keys[val] = null;
		}
		total_keys--;
	}

	public static void main(String[] args) {
		hashit test = new hashit();
		Scanner s = new Scanner(System.in);
		int t = s.

	}
}