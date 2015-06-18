#include <iostream>
using namespace std;

int main() {
    long long a,b; cin >> a >> b;
    long long c = 0;
    while (true) {
        long long sq = a/b;
        c += sq;
        if (a % b == 0) {
            cout << c << endl;
            return 0;
        }
        long long d = a % (sq * b);
        a = max(b,d);
        b = min(b,d);
    }
}