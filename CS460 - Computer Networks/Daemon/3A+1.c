#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int a, n;
    int flag = 0;
    int count = 0;
    int mem[1000];
    printf("Enter a number: ");
    scanf("%d", &a);
    printf("The number you have entered is: %d\n", a);

    while (a != 1)
    {
        if (a % 2 == 0)
        {
            printf("%d, ", a);
            a = a/2;
            count++;
            
            while (mem[n] != '\0'){
                n++;
                flag = 1;
            }
            
            while (n + 1 != 1 && flag != 0){
                mem[n] = mem[n-1];
                n--;
            }

            mem[n] = a;
        }

        else
        {
            printf("%d, ", a);
            a = (3*a)+1;
            count++;

            while (mem[n] != '\0'){
                n++;    
                flag = 1;
            }

            while (n + 1 != 1 && flag != 0){
                mem[n] = mem[n-1];
                n--;
            }

            mem[n] = a;
        }
    }
    printf("\nThere were %d steps\n", count);
    
    return 0;
}
