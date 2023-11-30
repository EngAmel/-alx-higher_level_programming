#include <stdio.h>
#include <lists.h>

/**
 * check_cycle - function check cycle
 * @list:node
 *
 * Return: 1 if there cycle 0 if not.
 **/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *first = list;

		while (slow != NULL && first != NULL)
		{
			slow = slow->next;
			first = first->next->next;
			if (slow == first)
				return (1);
		}
		return (0);
}
