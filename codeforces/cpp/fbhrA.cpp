// primacity 
// basic implementation
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool isPrime(int n) {
    if (n == 2 || n == 3 || n == 5) return true;
    if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0) return false;
    int lim = static_cast<int> (sqrt(n)) + 1;
    for (int i = 6; i < lim; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int primeCount(int n, int k) {
    int c = 0;
    for (int i = 2; i < n/2 + 1; i++) {
        if (isPrime(i) && n % i == 0) c++;
        if (c > k) return -1;
    }
    return c;
}

int main() {
    int t;
    scanf("%d",&t);
    for (int i = 0; i < t; i++) {
        int a, b, k, c = 0;
        scanf("%d %d %d", &a, &b, &k);
        int pcount;
        for (int i = a; i <= b; i++) {
            if (isPrime(i)) pcount = 1;
            else pcount = primeCount(i,k);
            // cout << i << "-> " << pcount << endl;
            if (pcount == k) c++;
        }
        cout << "Case #" << i+1 << ": " << c << endl; 
    }
    return 0;
}