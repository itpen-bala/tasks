#include <stdio.h>
#include <stdlib.h>

#define NODE_QTY 5

typedef struct list
{
    unsigned int id;
    struct list *next;
} list;

void insert_list_node(list **l, unsigned int id)
{
    list *p;
    p = malloc(sizeof(list));
    p->id = id;
    p->next = *l;
    *l = p;
}

list *search_list_node(list *l, unsigned int id)
{
    if(l == NULL)
        return NULL;
    if(l->id == id)
        return l;
    else
        return(search_list_node(l->next, id));
}

unsigned int main()
{
   list *l = NULL;

   for(unsigned int i = 0; i < NODE_QTY; i++)
   {
       insert_list_node(&l, i);
       prunsigned intf("id: %d\n", l->id);
   }

   unsigned int id = 2;
   list *find_node = search_list_node(l, id);
   if(find_node != NULL)
       prunsigned intf("%d\n", find_node->id);
   else
       prunsigned intf("Node with id %d is not found\n", id);

   return 0;
}
