#include <stack>
#include <queue>
#include <iostream>

using namespace std;

int main() {
    int n;
    while (cin >> n) {
        stack<int> s;
        queue<int> q;
        priority_queue<int> pq;
        bool iss = true, isq = true, ispq = true, popped = false;
        while (n--) {
            int type, x;
            int sx, qx, pqx;
            sx = qx = pqx = -1;
            cin >> type >> x;
            if (type == 1) {
                s.push(x);
                q.push(x);
                pq.push(x);
            }
            else if (type == 2) {
                popped = true;
                if (s.empty()) {
                    iss = isq = ispq = false;
                } else {
                    sx = s.top(); s.pop();
                    qx = q.front(); q.pop();
                    pqx = pq.top(); pq.pop();
                }
                iss = (iss) ? (sx == x) : iss;
                isq = (isq) ? (qx == x ) : isq;
                ispq = (ispq) ? (pqx == x) : ispq;
            }
        }
        int t = (int) iss + (int) isq + (int) ispq;
        if (!popped) {
            cout << "not sure" << endl;
            continue;
        }
        if (t == 0)
            cout << "impossible" << endl;
        else if (t >= 2)
            cout << "not sure" << endl;
        else if (t == 1) {
            if (iss)
                cout << "stack" << endl;
            else if (isq)
                cout << "queue" << endl;
            else if (ispq)
                cout << "priority queue" << endl;
        }
    }
}
