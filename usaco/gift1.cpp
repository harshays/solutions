/*
ID: hrshah41
PROG: gift1
LANG: C++         
*/
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main() {
    ofstream fout ("gift1.out");
    ifstream fin ("gift1.in");
    map<string,int> np; 
    int n; fin >> n;
    for (int i = 0; i < n; i++) {
        string p; fin >> p;
        np[p] = 0;
    }
    while (!fin.eof()) {
        string inp; fin >> inp;
        int amt, f; fin >> amt >> f;
        if (f != 0) {
            np[inp] -= amt;
            np[inp] += amt - (amt/f)*f;
            for (int i = 0; i < f; i++) {
                string frnd; fin >> frnd;
                np[frnd] += amt/f;
            }
        } else {
            np[inp] += amt;
        }
    } 

    ifstream f2("gift1.in");
    int num; f2 >> num;
    while (num-- > 0) {
        string name; f2 >> name;
        fout << name << " " << np[name] << endl;
    }
    return 0;
}