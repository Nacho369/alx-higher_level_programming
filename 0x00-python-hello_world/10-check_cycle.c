#include "lists.h"


/*
 * check_cycle - A function in C that checks if a singly linked list has a cycle in it.
 * @list: Pointer to the linked list
 * Return: 0 if there is no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp->next != NULL && temp->next->next != NULL)
	{
		temp = temp->next;

		if (temp->next == list)
			return (1);
	}

	return (0);
}
