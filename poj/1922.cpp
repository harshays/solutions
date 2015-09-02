#include<iostream>
#include<math.h>

using namespace std;

int main() {
    int N;
    int sp, tm;
    double min, time;

    while (1) {
        cin >> N;
        if (N == 0) {
            break;
        }
        min = 3600 * 4.5;

        while (N--) {
            cin >> sp >> tm;
            if (tm < 0) {
                continue;
            }
            time = 4.5 / sp * 3600 + tm;

            if (time < min)
                min = time;
        }
        int t = (int)ceil(min);
        cout << t << endl;
    }
}
