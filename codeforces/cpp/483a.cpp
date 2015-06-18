#include <iostream>
using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int main() {
    long long l,r; cin >> l >> r;
    if (r - l < 2) {
        cout << -1 << endl;
        return 0;
    }
    bool found = false;
    long long a = l, b, c;
    while (a + 2 <= r && !found) {
        b = a + 1;
        c = b + 1;

        while (c <= r && !found) {
            if (gcd(c,b) == 1 && gcd(c,a) > 1) {
                cout << a << " " << b << " " << c << endl;
                return 0;
            }
            c++;
        }
        a++;
    }
    cout << -1 << endl;
}