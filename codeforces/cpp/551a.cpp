#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n; cin >> n;
    vector<int> v;
    for (int i = 0; i < n; i++) {
        int t; cin >> t;
        v.push_back(t);
    }
    for (int i = 0; i < v.size(); i++) {
        int elem = v[i];
        int score = 1;
        for (int j = 0; j < v.size(); j++) {
            if (v[j] > elem)
                score++;
        }
        cout << score << " ";
    }
    cout << endl;
}