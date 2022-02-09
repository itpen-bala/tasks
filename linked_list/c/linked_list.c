#include <stdio.h>
#include <stdlib.h>

#define NODE_QTY 3

typedef struct list
{
    unsigned int id;
    struct list *next;
} list;

void insert_node(list **node, unsigned int id)
{
    list *p;
    p = malloc(sizeof(list));
    p->id = id;
    p->next = *node;
    *node = p;
}

list *search_node(list *node, unsigned int id)
{
    if(node == NULL)
        return NULL;
    if(node->id == id)
        return node;
    else
        return(search_node(node->next, id));
}

list *search_predecessor_node(list *node, unsigned int id)
{
    if((node == NULL) || (node->next == NULL))
        return NULL;
    if((node->next)->id == id)
        return node;
    else
        return (search_predecessor_node(node->next, id));
}

int delete_node(list **node, unsigned int id)
{
    list *p;
    list *prev;

    p = search_node(*node, id);
    if(p != NULL)
    {
        prev = search_predecessor_node(*node, id);
        if(prev == NULL)
            *node = p->next;
        else
            prev->next = p->next;
        free(p);
        return 1;
    }
    return 0;
}

void traversal_tree(list *node)
{
    if(node != NULL)
    {
        printf("id: %d\n", node->id);
        traversal_tree(node->next);
    }
}

int main()
{
   list *node = NULL;

   for(int i = 0; i < NODE_QTY; i++)
   {
       insert_node(&node, i);
       printf("id: %d\n", node->id);
   }

   traversal_tree(node);

   unsigned int id = 1;
   if (delete_node(&node, id) == 1)
       printf("Node with id %d successfully deleted\n", id);
   else
       printf("Node with id %d is not found\n", id);
   
   traversal_tree(node);

   return 0;
}
