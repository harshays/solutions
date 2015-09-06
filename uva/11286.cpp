#include <map>
#include <set>
#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    while (n != 0) {
        map<set<int>, int> m;
        while (n--) {
            int tmp;
            set<int> s;
            for (int i = 0; i < 5; i++) {
                cin >> tmp;
                s.insert(tmp);
            }
            m[s]++;
        }
        int maxval = -1;
        for (auto it = m.begin(); it != m.end(); it++)
            maxval = (it->second > maxval) ? it->second : maxval;
        int count = 0;
        for (auto it = m.begin(); it != m.end(); it++) {
            if (it->second == maxval)
                count += it->second;
        }
        cout << count << endl;
        cin >> n;
    }
}
