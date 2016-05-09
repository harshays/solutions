#include <iostream>
#include <string>
using namespace std;

int main() {
    string n; cin >> n;
    for (int i = 0; i < n.length(); i++) {
        if (i == 0 && n[i] == '9')
            continue;
        int dig = n[i] - '0';
        if (dig >= 5)
            n[i] = '0'+9-dig;
    }
    cout << n << endl;
}