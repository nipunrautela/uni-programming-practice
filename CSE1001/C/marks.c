#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char name[25][10], prog[2][10];
    int regno[10], m1[10], m2[10], m3[10], m4[10], m5[10], grade[10];
    int n, i, s, mark_avg;
    const int class_avg = 50;
    scanf("%d", &n);
    for (i = 0; i < 10; i++)
    {
        scanf("%d%s%s%d%d%d%d%d", &regno[i], name[i], prog[i], &m1[i], &m2[i], &m3[i], &m4[i], &m5[i]);
        mark_avg = (m1[i] + m2[i] + m3[i] + m4[i] + m5[i]) / 5;
        if (strcmp(prog[i], "UG") == 0)
        {
            s = class_avg + (0.5 * mark_avg);
            if (mark_avg > s)
                grade[i] = 'A';
            else if (mark_avg > class_avg && mark_avg < s)
                grade[i] = 'B';
            else
                grade[i] = 'C';
        }
        else if (strcmp(prog[i], "PG") == 0)
        {
            s = class_avg + mark_avg / 4;
            if (mark_avg > s)
                grade[i] = 'A';
            else if (mark_avg > class_avg && mark_avg < s)
                grade[i] = 'B';
            else
                grade[i] = 'C';
        }
        else
            printf("No such programme");
        for (i = 0; i < 10; i++)
            printf("%d%s%c", regno[i], name[i], grade[i]);
    }
}