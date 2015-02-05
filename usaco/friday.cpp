/*
ID: hrshah41
PROG: friday
LANG: C++         
*/
#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream fin("friday.in");
    ofstream fout("friday.out");
    int N; fin >> N;
    int months[] = {31,28,31,30,31,30,31,31,30,31,30,31};
    int week[] = {0,0,0,0,0,0,0}; // count 13th
    int Y = 1900;
    int Y2 = Y + N - 1;
    int m = 0,  d = 0, y = 0;
    int countDays = 0, wk = 0; // days since jan 1 1900
    for (y = Y; y <= Y2; y++) {
        if ((y % 4 == 0 && y % 100 != 0) || (y % 400 == 0)) {
            months[1] = 29;
        } 
        else {
            months[1] = 28; 
        }

        for (m = 0; m < 12; m++) {
            for (d = 0; d < months[m]; d++) {
                wk = countDays++ % 7 ;
                if (d == 12) week[wk]++;
            }
        }
    }

    
    for (int i = 5; i < 12; i++) {
        fout << week[i%7];
        if (i != 11) fout << " "; 
        else fout << endl;
    }
    return 0;
}