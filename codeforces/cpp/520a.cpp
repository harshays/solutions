#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int n; cin >> n;
    string s; cin >> s;
    if (n < 26) {
        cout << "NO" << endl;
        return 0;
    }
    std::transform(s.begin(), s.end(), s.begin(), ::tolower);
    int count[26] = {0};
    for (auto c : s) {
        count[c-'a']++;
    }
    for (int i = 0; i < 26; i++) {
        if (count[i] < 1) {
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;
}