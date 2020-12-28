#include <stdio.h>

int main()
{
    int n, c, m;
    float noc;
    
    printf("Enter the amount in hand:");
    scanf("%d",&n);
    printf("Enter price of one chocolate:");
    scanf("%d",&c);
    printf("Enter the number of wrappers our dear little bob had:");
    scanf("%d",&m);
    noc= (n/c)+m;
    printf("%f",noc);
    
    return 0;
}
