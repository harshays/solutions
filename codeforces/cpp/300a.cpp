#include <iostream>
#include <vector>
using namespace std;

void vprint(vector<int>& v) {
    cout << v.size() << " ";
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;
}

int main() {
    int n; cin >> n;
    vector<int> arr, l, g, z;
    for (int i = 0; i < n; i++) {
        int t; cin >> t;
        if (t < 0)
            l.push_back(t);
        else if (t > 0)
            g.push_back(t);
        else
            z.push_back(t);
    }

    if (g.size() == 0) {
        for (int i = 0; i <= 1; i++) {
            g.push_back(l.back());
            l.pop_back();
        }
    }

    if (l.size() % 2 == 0) {
        z.push_back(l.back());
        l.pop_back();
    }

    vprint(l);
    vprint(g);
    vprint(z);
}