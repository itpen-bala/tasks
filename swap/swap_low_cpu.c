#include <stdio.h>

void swap(int *px, int *py)
{
    int tmp = *px;
    *px = *py;
    *py = tmp;
}

int main()
{
    int a = 2;
    int b = 4;
    printf("a = %d, b = %d\n", a, b);

    swap(&a, &b);
    printf("a = %d, b = %d\n", a, b);

    return 0;
}
