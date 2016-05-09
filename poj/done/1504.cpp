#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int reverse(int n) {
    vector<int> v;
    while (n) {
        v.push_back(n%10);
        n/=10;
    }

    int r = 0;
    for (int i = 0; i < v.size(); i++) {
        r += v[i]*pow(10.0, static_cast<int>(v.size()-1-i));
    }
    return r;
}

int main() {
    int t, a, b; cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> a >> b;
        cout << reverse(reverse(a) + reverse(b)) << endl;
    }
}
