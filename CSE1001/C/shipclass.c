#include <stdio.h>

int main() {

    char id[10];
    printf("Enter the ship ID: ");
    scanf("%s", id);
    if (id[0] == 'B' || id[0] == 'b') {
        printf("Battleship");
    }
    else if (id[0] == 'C' || id[0] == 'c') {
        printf("Cruiser");
    }
    else if (id[0] == 'D' || id[0] == 'd') {
        printf("Destroyer");
    }
    else if (id[0] == 'F' || id[0] == 'f') {
        printf("Frigate");
    }

    return 0;
}
