#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int getInversions(string &s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i+1; j < s.length(); j++) {
            if (s[i] > s[j]) {
                count++;
            }
        }
    }
    return count;
}

bool cmpInversion(string &s1, string &s2) {
    int i1 = getInversions(s1), i2 = getInversions(s2);
    return i1 < i2;
}

int main() {
    int len, num; cin >> len >> num;
    vector<string> v;
    string temp;
    for (int i = 0; i < num; i++) {
        cin >> temp;
        v.push_back(temp);
        getInversions(temp);
    }
    sort(v.begin(), v.end(), cmpInversion);

    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << endl;
    }
}
