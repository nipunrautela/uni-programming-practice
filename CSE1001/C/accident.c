#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, accidents[5];
    scanf("%d", &n);
    int total = 0;
    for (int i=0; i<n; i++) {
        scanf("%d", &accidents[i]);
        total += accidents[i];
    }
    int average = total/n;
    printf("Average: %d\n", average);
    printf("Difference: ");
    for (int i=0; i<n; i++) {
        printf("%d ", abs(average-accidents[i]));
    }
    return 0;
}
