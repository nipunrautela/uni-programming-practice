#include <stdio.h>

int n, cust_no[10], balance[10];
char names[10][20];

void withdraw(int c_no, int amount) {
    int index;
    for (int i=0; i<n; i++) {
        if (c_no == cust_no[i]) {
            index = i;
            break;
        }
    }
    balance[index] -= amount;
    if(balance[index] >= 500) {
        printf("%d\n%s\n%d", cust_no[index], names[index], balance[index]);
    }
    else {
        printf("Insufficient Balance");
    }
}

int main() {
    int number, amount;
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        scanf("%d%s%d", &cust_no[i], &names[i], &balance[i]);
    }
    scanf("%d%d", &number, &amount);
    withdraw(number, amount);
    return 0;
}