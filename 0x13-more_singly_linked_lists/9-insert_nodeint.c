#include "lists.h"
#include <stdio.h>

/**
 * insert_nodeint_at_index - inserts a new node at a given position.
 * @head: head of a linked list
 * @idx: index of the list
 * @n: integer of the inserted node
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)

{
	listint_t *node, *new, *prev;
	unsigned int i;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = NULL;
	node = *head;
	prev = *head;
	i = 0;
	if (idx == 0)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node != NULL)
	{
		if (i == idx)

		{
			new->next = node;
			prev->next = new;
			return (new);
		}
		prev = node;
	//	node->node = next;
		i++;
	}
	if (idx == i)
	{
		prev->next = new;
		return (new);
	}
	free(new);
	return (NULL);
}
