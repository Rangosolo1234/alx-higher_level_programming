#include <stdlib.h>
#include "lists.h"
/**
  * insert_node - inserts a number into a sorted singly linked list.
  * @head: pointer to the pointer of the list.
  * @number: number to be inserted.
  *
  * Return: address f the new node or NULL if it failed.
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev_node, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node != NULL)
	{
		new_node->n = number;
		if (*head == NULL || (*head)->n >= new_node->n)
		{
			new_node->next = *head;
			*head = new_node;
			return (new_node);
		}
		else
		{
			prev_node = *head;
			while (prev_node->next != NULL && prev_node->next->n < new_node->n)
				prev_node = prev_node->next;
			new_node->next = prev_node->next;
			prev_node->next = new_node;
			return (new_node);
		}
	}
	return (NULL);
}
