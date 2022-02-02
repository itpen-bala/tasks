#include <stdio.h>

void swap(int *px, int *py)
{
    *px = *px + *py;
    *py = *px - *py;
    *px = *px - *py;
}

int main()
{
    int a = -2;
    int b = 111;
    printf("a = %d, b = %d\n", a, b);

    swap(&a, &b);
    printf("a = %d, b = %d\n", a, b);

    return 0;
}
