#include <unordered_map>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, m; cin >> n >> m;
    int a, b;
    unordered_map<int, vector<int> > wrs;

    while (m--) {
        cin >> a >> b;
        wrs[a].push_back(b);
        wrs[b].push_back(a);
    }

    unordered_map<int, vector<int> >::iterator it;
    int min = -1;
    for (it = wrs.begin(); it != wrs.end(); it++) {
        if (it->second.size() < 2)
            continue;
        vector<int>& ff = it->second;
        int wr = it->first;
        for (int i = 0; i < ff.size(); i++) {
            int wr2 = ff[i];
            vector<int>& ff2 = wrs[wr2];
            for (int j = 0; j < ff2.size(); j++) {
                int wr3 = ff2[j];
                vector<int>& ff3 = wrs[wr3];
                if (find(ff3.begin(), ff3.end(), wr) != ff3.end()) {
                    int sum = ff.size() + ff2.size() + ff3.size() - 6;
                    if (min < 0 || sum < min)
                        min = sum;
                }
            }
        }
    }
    cout << min << endl;
}
