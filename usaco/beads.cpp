/*
ID: hrshah41
PROG: beads
LANG: C++         
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream fin("beads.in");
    ofstream fout("beads.out");
    int N; fin >> N;
    string beads; fin >> beads;
    int max = 0, curr = 0; char color; bool switched;

    for (int i = 0; i < beads.length(); i++) {
        curr = 0;
        color = 'w';
        switched = false;
        for (int j = 0; j < beads.length(); j++) {
            char currcol = beads[(i+j) % beads.length()];
            if (currcol != 'w') {
                if (color == 'w') {
                    color = currcol;
                } 
                else if (currcol != color) {
                    if (switched)
                        break;
                    else {
                        color = currcol;
                        switched = true;
                    }
                }
            }
            curr++;
        }
        if (curr > max) {
            max = curr;
        }
    }

    fout << max << endl;
    return 0;
}