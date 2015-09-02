#include <iostream>
#include <string>

using namespace std;

int main() {
    string alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z";
    string inp;
    char m[26];
    int maxf = 0;

    for (int i = 0; i < 26; i++) {
        m[i] = 0;
    }

    for (int i = 0; i < 4; i++) {
        getline(cin, inp);
        for (int j = 0; j < inp.length(); j++) {
            if (inp[j] >= 65 && inp[j] <= 90) {
                m[inp[j]-65]++;
            }
        }
    }

    for (int i = 0; i < 26; i++) {
        maxf = max(maxf, int(m[i]));
    }

    while (maxf) {
        string row = "";
        for (int i = 0; i < 26; i++) {
            if (m[i] >= maxf)
                row += '*';
            else
                row += ' ';
            if (i != 25)
                row += ' ';
        }
        int lidx = 0;
        for (int i = 0; i < row.length(); i++) {
            if (row[i] == '*')
                lidx = i;
        }
        cout << row.substr(0, lidx+1) << endl;
        maxf--;
    }

    cout << alphabet;
}
