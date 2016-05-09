#include <iostream>
#include <string>
#include <cmath>
#include <iomanip>
using namespace std;

int factorial(int n) {
    if (n == 0)
        return 1;
    if (n == 1)
        return 1;
    return n*factorial(n-1);
}

int main() {
    string a; cin >> a;
    string b; cin >> b;
    int aval = 0, bval = 0, unk = 0;
    for (auto v : a) {
        aval += (v == '+') ? 1 : -1;
    }
    for (auto v : b) {
        unk += (v == '?') ? 1 : 0;
        bval += (v == '?') ? 0 : (v == '+') ? 1 : -1;
    }
    int t = abs(aval - bval);
    if (unk == 0) {
        if (t == 0) {
            cout << double(1) << endl;
        } else {
            cout << double(0) << endl;
        }
        return 0;
    }
    if (unk < t) {
        cout << double(0);
        return 0;
    }
    if (unk % 2 != t % 2) {
        cout << double(0);
        return 0;
    }
    // cout << unk << " " << t << endl;
    int total = pow(2, unk);
    int plus = (unk + t)/2;
    int minus = abs(unk - plus);
    // cout << plus << " " << minus << endl;
    double pnr = factorial(unk)/double(factorial(abs(plus))*factorial(abs(minus)));
    // cout << pnr << endl;
    double ans = pnr/double(total);
    cout << setprecision(16) << ans << endl;
}