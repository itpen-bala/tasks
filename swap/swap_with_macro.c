#include <stdio.h>

#define SWAP(type, x, y) type temp = y; y = x; x = temp

int main()
{
    int a = 10;
    int b = 11;
    printf("a = %d, b = %d\n", a, b);

    SWAP(int, a, b);
    printf("a = %d, b = %d\n", a, b);

    return 0;
}
