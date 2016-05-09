#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int n; cin >> n;
    string scur; cin >> scur;
    string slock; cin >> slock;
    int tot = 0;
    for (int i = 0; i < n; i++) {
        int cur = scur[i] - '0';
        int lock = slock[i] - '0';
        int diff = abs(cur - lock);
        tot += min(diff, 10 - diff);
    }

    cout << tot << endl;
    return 0;
}