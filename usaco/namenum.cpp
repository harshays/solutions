/*
ID: hrshah41
PROG: namenum
LANG: C++         
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;

string serialize(string& name) {
    string serial = "";
    for (int i = 0; i < name.length(); i++) {
        if (name[i] == 'Z' || name[i] == 'Q')
            serial += "0";
        else if (name[i] < 'Q')
            serial += (name[i] - 'A')/3 + '2';
        else if (name[i] >= 'Q')
            serial += (name[i] - 'Q')/3 + '7';
    }
    return serial;
}

int main() {
    ifstream fin("namenum.in");
    ofstream fout("namenum.out");
    ifstream dicttxt("dict.txt");
    string n; fin >> n;
    int c = 0;
    if (dicttxt.is_open()) {
        while (!dicttxt.eof()) {
            string word; dicttxt >> word;
            if (n.length() == word.length() && n == serialize(word)) {
                fout << word << endl;
                c++;
            }
        }
    }

    if (c == 0) {
        fout << "NONE" << endl;
    }
}
