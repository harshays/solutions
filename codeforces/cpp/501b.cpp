#include <iostream>
#include <map>
#include <algorithm>
#include <string>
using namespace std;

typedef map<string, string> mss;

map<string,string> makeMap() {
    mss m;
    int n;
    cin >> n;
    string k, v; 
    for (int i = 0; i < n; i++) {
        cin >> k >> v;
        m[k] = v;
    }
    return m;
}

bool keyExists(mss& m, string key) {
    return m.count(key) >= 1;
}

void shorten(mss& m, string init) {
    string value = m[init];
    while (keyExists(m, value)) {
        string old = value;
        value = m[value];
        m.erase(m.find(old));
    }
    m[init] = value;
}

int main() {
    mss m = makeMap();
    mss::iterator it;
    for (it = m.begin(); it != m.end(); it++) { shorten(m, it->first); }
    cout << m.size() << endl;
    for (it = m.begin(); it != m.end(); it++) {
        cout << it->first << " " << it->second << endl;
    }
    
}