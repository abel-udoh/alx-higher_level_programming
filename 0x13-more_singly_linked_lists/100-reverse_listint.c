#include "lists.h"
#include <stdio.h>

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: head of a linked list
 * Return: pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)

{
	listint_t *next, *prev;

	prev = NULL;
	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}
