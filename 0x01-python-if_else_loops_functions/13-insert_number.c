#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * *insert_node - function add node
 * @head:header
 * @number:value
 *
 * Return: pointer.
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	*temp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (temp == NULL || new->n < temp->n)
	{
		new->next = temp;
		*head = new;
		free(new);
		return (*head);
	}
	while (temp != NULL)
	{
		if (temp->next != NULL || new->n < temp->next->n)
		{
			new->next = temp->next;
			temp->next = new;
			free(new);
			return (temp);
		}
		temp = temp->next;
	}
	free(new);
	return (NULL);


}
