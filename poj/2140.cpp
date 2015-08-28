#include <iostream>

using namespace std;

int main() {
    int n; cin >> n;
    int count = 1; // n itself

    for (int i = 1; i < n/2 + 1; i++) {
        int total = i;
        int j = i+1;
        while (total <= n) {
            total += j;
            j++;
            if (total == n) {
                count++;
                break;
            }
        }
    }

    cout << count << endl;

}
