#include <stdio.h>

int main() {
    int num1, num2;
    printf("Enter first number: ");
    scanf("%d", &num1);
    printf("Enter the second number: ");
    scanf("%d", &num2);
    int smol = 0;
    if (num1<num2) smol = num1; else smol = num2;
    printf("The GCF is: ");
    for (int i=smol; i>1; i--) {
        if (num1%i == 0 && num2%i == 0){
            printf("%d", i);
            break;
        }
    }

    return 0;
}
