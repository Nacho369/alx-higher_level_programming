#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	if (curr->n > number)
	{
		*head = new;
		new->next = curr;
		return (new);
	}

	while (curr->next != NULL)
	{
		if (curr->next->n > number)
		{
			new->next = curr->next;
			curr->next = new;
			return (new);
		}
		curr = curr->next;
	}

	curr->next = new;
	return (new);
}
