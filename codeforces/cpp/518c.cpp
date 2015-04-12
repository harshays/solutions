#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void print(vector<int>& s) {
    for (auto e : s) {
        cout << e << " ";
    }
    cout << endl;
}

int main() {
    int i = 0, n, m, k, app; cin >> n >> m >> k;
    int s = n/k + 1;
    vector<vector<int> > apps(s, vector<int>(k, -1));
    
    for (int i = 0; i < n; i++) {
        int v; cin >> v;
        apps[i/k][i%k] = v;
    }

    // for (int x = 0; x < s; x++) {
    //     print(apps[x]);
    // }

    int gest = 0;
    while (m--) {
        cin >> app;
        for (int i = 0; i < s; i++) {
            if (std::find(apps[i].begin(), apps[i].end(), app) != apps[i].end()) {
                gest += i + 1;
                int idx = std::find(apps[i].begin(), apps[i].end(), app) - apps[i].begin();
                if (idx > 0) {
                    int tmp = apps[i][idx];
                    apps[i][idx] = apps[i][idx-1];
                    apps[i][idx-1] = tmp;
                } else {
                    if (i > 0) {
                        int tmp = apps[i][idx];
                        apps[i][idx] = apps[i-1][apps[i-1].size()-1];
                        apps[i-1][apps[i-1].size()-1] = tmp;
                    }
                }
            } else {
                continue;
            }
        }
    }
    cout << gest << endl;


}