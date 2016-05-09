/*
ID: hrshah41
PROG: milk2
LANG: C++         
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

struct interval {
    int start, end;
    interval(int s, int e) {
        start = s;
        end = e;
    }
    bool operator<(const interval& i) const {
        return start < i.start;
    }
};

int main() {
    ifstream fin("milk2.in");
    ofstream fout("milk2.out");
    int n; fin >> n;
    vector<interval> milk;
    while (n--) {
        int s,e; fin >> s >> e;
        milk.push_back(interval(s,e));
    }
    sort(milk.begin(), milk.end());
    int start = milk[0].start;
    int end = milk[0].end;
    int diff = 0;
    int maxcont = end - start;
    for (vector<interval>::iterator it = milk.begin() + 1; it != milk.end(); it++) {
        int low = it->start;
        int high = it->end;
        if (low <= end) {
            start = min(start, low);
            end = max(end, high);
            maxcont = max(maxcont, end - start);
        } else {
            diff = max(diff, low - end);
            start = low;
            end = high;
        }
    }
    fout << maxcont << " " << diff << endl;
}