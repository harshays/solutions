#include <iostream>
#include <unordered_map>
#include <string>
#include <sstream>

using namespace std;

int main() {
	unordered_map<string, int> m;
	int n; cin >> n;
	while (n--) {
		string word; cin >> word;
		if (m.find(word) == m.end()) {
			m[word] = 0;
			cout << "OK" << endl;
		} else {
			m[word]++;
			cout << word << m[word] << endl;
		}
	}
}
