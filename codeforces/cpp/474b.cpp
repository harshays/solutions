#include <iostream>
using namespace std;
#include <algorithm>
#include <vector>

int main() {
    int n; cin >> n;
    vector<int> piles; 
    int tmp, m, sm = 0;
    while (n--) {
        cin >> tmp;
        sm += tmp;
        piles.push_back(sm);
    }
    cin >> m;
    vector<int> wms; 
    while (m--) {
        cin >> tmp;
        wms.push_back(tmp);
    }

    for (int wm : wms) {
        int pos = lower_bound(piles.begin(), piles.end(), wm) - piles.begin();
        cout << pos+1 << endl;
    }

}