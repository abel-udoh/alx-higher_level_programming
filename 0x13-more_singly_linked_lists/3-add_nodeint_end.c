#include "lists.h"
#include <stdio.h>

/**
 * add_nodeint_end - add a new node at the end of linked list
 * @head: head of a linked list
 * @n: integer
 * Return: address of the new element or NULL If it fails
 */

listint_t *add_nodeint_end(listint_t **head, const int n)

{
	listint_t *new;
	listint_t *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	 new->n = n;
	 new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	temp = *head;
	while (temp->next != NULL)
	{
		temp = temp->next;
	}
	temp->next = new;
	return (new);
}


