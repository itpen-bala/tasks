#include <stdio.h>

struct node
{
    int data;
    struct node *next;
};

void addNode(struct node *new, struct node *old)
{
    new->next == NULL;
    if(old != NULL)
    {
        old->next = new;
    }
}

int main()
{
    struct node n1;
    n1.data = 1;
    printf("%d\n", n1.data);
    addNode(&n1, NULL);

    struct node n2;
    n2.data = 2;
    printf("%d\n", n2.data);

    addNode(&n2, &n1);
    printf("%d\n", n1.next->data);

    return 0;
}
