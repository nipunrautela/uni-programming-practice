#include <stdio.h>

int main() {
    int hours, mins;
    printf("Enter the number of hours browsed: ");
    scanf("%d", &hours);
    printf("Enter the number of minutes browsed: ");
    scanf("%d", &mins);
    if (hours >= 7) {
        printf("Invalid.");
    }
    else if (hours >= 5) {
        printf("Cost of browsing: %d", 200 + (hours-5)*50 + mins);
    }
    else {
        printf("Cost of browsing: %d", (hours)*50 + mins);
    }
    
    return 0;
}
