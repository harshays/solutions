/*
ID: hrshah41
PROG: gift1
LANG: C++         
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream fout ("o.out");
    ifstream fin ("i.in");
    string a, b;
    fin >> a >> b;
    int ap = 1, bp = 1;
    for (int i = 0; i < a.length(); i++) {
        ap *= (static_cast<int>(a[i] - 64) % 47);
    }
    for (int i = 0; i < b.length(); i++) {
        bp *= (static_cast<int>(b[i] - 64) % 47);
    }
    if (ap % 47 == bp % 47) {
        fout << "GO" << endl;
    } else {
        fout << "STAY" << endl;
    }

    return 0;
}