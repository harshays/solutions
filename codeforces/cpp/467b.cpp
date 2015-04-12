#include <iostream>
#include <bitset>
#include <vector>
using namespace std;

int count(bitset<21>& b) {
    int c = 0;
    for (int i = 0; i < b.size(); i++) {
        if (b[i] == 1) {
            c++;
        }
    }
    return c;
}

int main() {
    int n, m, k, x; cin >> n >> m >> k; 
    vector<int> xi; 
    while (m--) {
        cin >> x;
        xi.push_back(x);
    }
    int fed; cin >> fed;
    int cnt = 0;
    for (int op : xi) {
        bitset<21> b(fed^op);
        int diff = count(b);
        if (diff <= k)
            cnt++;
    } 
    cout << cnt << endl;
}