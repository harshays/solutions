#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a,b,s; cin >> a >> b >> s;
    a = abs(a); b = abs(b);
    
    if (s < a + b) {
        cout << "NO";
    } else {
        if ((s - a - b) % 2 == 0) {
            cout << "YES";
        } else {
            cout << "NO";
        }
    }
}