#include <iostream>
using namespace std;

struct vars {
    int n = 0,a = 1, b = 2;
};

int nextFibonacci(vars *&v) { // a reference pointer 
    if (v->n == 0) {
        v->n++;
        return v->a; 
    }
    else if (v->n == 1) {
        v->n++;
        return v->b;
    }
    else {
        v->n++;
        int temp = v->a + v->b;
        v->a = v->b;
        v->b = temp;
        return temp;
    }
}

void debugVars(vars *&v) {
    cout << v->n << endl;
    cout << v->a << endl;
    cout << v->b << endl;
}


int main() {
    int LIMIT = 4000000;
    vars v;
    vars *vp = &v; // pointer
    int sum = 0; 
    while (vp->b < LIMIT) {
        int val = nextFibonacci(vp);
        if (val % 2 == 0) sum += val;
    }
    cout << "answer: " << sum << endl;
}