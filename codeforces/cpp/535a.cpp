#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<int,string> single;
    map<int,string> tenth;
    single[0] = "zero";
    single[1] = "one";
    single[2] = "two";
    single[3] = "three";
    single[4] = "four";
    single[5] = "five";
    single[6] = "six";
    single[7] = "seven";
    single[8] = "eight";
    single[9] = "nine";
    single[10] = "ten";
    single[11] = "eleven";
    single[12] = "twelve";
    single[13] = "thirteen";
    single[14] = "fourteen";
    single[15] = "fifteen";
    single[16] = "sixteen";
    single[17] = "seventeen";
    single[18] = "eighteen";
    single[19] = "nineteen";
    tenth[2] = "twenty";
    tenth[3] = "thirty";
    tenth[4] = "forty";
    tenth[5] = "fifty";
    tenth[6] = "sixty";
    tenth[7] = "seventy";
    tenth[8] = "eighty";
    tenth[9] = "ninety";

    int n; cin >> n;
    if (n <= 19) {
        cout << single[n] << endl;
    } else {
        int ten = n/10;
        int sing = n%10;
        if (sing != 0) {
            cout << tenth[ten]+"-"+single[sing] << endl;
        } else {
            cout << tenth[ten] << endl;
        }
    }
}