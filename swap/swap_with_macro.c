#include <stdio.h>

#define swap(type, x, y) type temp = y; y = x; x = temp

int main()
{
    int a = 10;
    int b = 11;
    printf("a = %d, b = %d\n", a, b);

    swap(int, a, b);
    printf("a = %d, b = %d\n", a, b);

    return 0;
}
