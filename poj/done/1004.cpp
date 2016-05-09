#include <iostream>
using namespace std;

int main() {
    double total = 0, temp;

    for (int i = 0; i < 12; i++) {
        scanf("%lf", &temp);
        total += temp;
    }

    printf("$%.2f\n", total/12.0);
}
