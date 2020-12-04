#include<stdio.h>
#include<stdlib.h>

int main() {
    // Variable declaration
    int a, b, c, d;
    float e, f;
    char g;
    char name[25];
    a = 10; 

    // Input statement
    printf("Welcome to hell!!\n");
    scanf("%d%d", &a, &b);
    printf("Hemlo hoomans! These are the numbers you sent us: %d, %d", a, b);

    int num1, num2;  
    int sum, sub, mult, mod;  
    float div;  
  
    /* 
     * Read two numbers from user separated by comma 
     */  
    printf("Input any two numbers separated by comma : ");  
    scanf("%d,%d", &num1, &num2);  
  
    /* 
     * Performs all arithmetic operations 
     */   
    sum = num1 + num2;  
    sub = num1 - num2;  
    mult = num1 * num2;  
    div = (float)num1 / num2;  
    mod = num1 % num2;  
  
    /* 
     * Prints the result of all arithmetic operations 
     */  
    printf("The sum of the given numbers : %d\n", sum);  
    printf("The difference of the given numbers : %d\n", sub);  
    printf("The product of the given numbers : %d\n", mult);  
    printf("The quotient of the given numbers : %f\n", div);  
    printf("MODULUS = %d\n", mod);  
    
    if (a%2==0 && b%2==0) {
        printf("Both numbers are even.\n");
    }
    else {
        if (a%2==0) {
            printf("Only a is even");
        }
        else if (b%2==0) {
            printf("Only b is even");
        }
        else {
            printf("Both numbers are odd.");
        }
    }

    return 0;
}
