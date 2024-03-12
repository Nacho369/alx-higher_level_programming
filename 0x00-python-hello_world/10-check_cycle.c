#include "lists.h"


/*
 * check_cycle - A function in C that checks if a singly linked list has a cycle in it.
 * @list: Pointer to the linked list
 * Return: 0 if there is no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *current = list;

	if (list == NULL)
		return (0);

	while (temp != NULL && temp->next != NULL)
	{
		current = current->next;
		temp = temp->next->next;

		if (current == temp)
			return (1);
	}

	return (0);
}
