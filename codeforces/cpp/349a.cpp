#include <iostream>
using namespace std;


int main() {
    int d25 = 0, d50 = 0;

    int N; cin >> N;
    bool ok = true;
    for (int i = 0; i < N && ok; i++) {
        int m; cin >> m;
        if (m == 25)
            d25++;
        else if (m == 50) {
            if (d25) {
                d50++; d25--;
            } else {
                ok = 0;
            }
        } else {
            if (d25 >= 1 && d50 >= 1) {
                d25--; d50--;
            } else if (d25 >= 3) {
                d25-=3;
            } else {
                ok = 0;
            }
        }
    }
    if (ok)
        cout << "YES";
    else
        cout << "NO";
}