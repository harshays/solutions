#include <vector>
#include <iostream>
#define all(x) x.begin(),x.end()

using namespace std;

int main() {
    unsigned int n;
    vector<unsigned int> v;
    while (cin >> n) {
        auto lb = lower_bound(all(v), n);
        v.insert(lb, n);
        int median = (v.size() % 2 == 1) ? v[v.size()/2] : (v[v.size()/2] + v[v.size()/2 - 1])/2;
        cout << median << endl;
    }
}
