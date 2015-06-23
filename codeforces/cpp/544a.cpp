#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

int main() {
    int k; string q; cin >> k >> q;
    set<char> s; s.insert(q[0]);
    vector<string> v; string temp = "";
    for (auto c: q) {
        if (s.find(c) == s.end()) {
            s.insert(c);
            v.push_back(temp);
            temp = c;
        } else {
            temp += c;
        }
    }
    v.push_back(temp);
    
    // cout << v.size() << endl;
    if (v.size() < k) {
        cout << "NO" << endl;
    } 
    else {
        cout << "YES" << endl;
        for (int i = 0; i < k - 1; i++) {
            cout << v[i] << endl;
        }
        string acc = "";
        for (int i = k - 1; i < v.size(); i++) {
            acc += v[i];
        }
        cout << acc << endl;
    }
}