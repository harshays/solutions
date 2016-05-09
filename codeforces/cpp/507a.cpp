#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <sstream>
using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;

int main() {
    int k, n, ai;
    cin >> n >> k;
    vi a;
    multimap <int, int> m;
    for (int i = 0; i < n; i++) {
        cin >> ai;
        m.insert(pair<int,int>(ai,i+1));
    }
        
    multimap<int,int>::iterator it = m.begin();
    int total = 0, count = 0;
    stringstream ss;

    for (; it != m.end(); it++) {
        total += it->first;
        if (total > k) break;
        count++;
        ss << it->second << " ";
    }

    cout << count << endl;
    cout << ss.str() << endl;
    
}