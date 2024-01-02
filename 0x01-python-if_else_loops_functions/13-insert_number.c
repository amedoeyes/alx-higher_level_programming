#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted linked list
 *
 * @head: pointer to head of list
 * @number: number to insert
 *
 * Return: pointer to new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return NULL;
	}

	while (*head != NULL && (*head)->n < number)
	{
		head = &(*head)->next;
	}

	new_node->n = number;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}
