#include "lists.h"
/**
  * check_cycle - Checiks if linked list is a cycly linked
  *
  * @list: Linked list
  * Return: 1 if there is a cycle, otherwise 0
  */
int check_cycle(listint_t *list)
{
	listint_t *this_node = list, *next_node = list;

	if (list == NULL)
		return (0);

	while (this_node && next_node && next_node->next)
	{
		this_node = this_node->next;
		next_node = next_node->next->next;
		if (this_node == next_node)
			return (1);
	}
	if (this_node != next_node)
		return (0);
	return (1);
}
