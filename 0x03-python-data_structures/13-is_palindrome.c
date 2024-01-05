#include "lists.h"

/**
 * reverse_list - reverses a linked list
 *
 * @head: head of the linked list
 */

void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;

	while (current)
	{
		*head = current->next;
		current->next = prev;
		prev = current;
		current = *head;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: head of the linked list
 *
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	if (head == NULL)
		return (0);

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (slow->next != NULL && fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	reverse_list(&slow);

	while (*head != NULL && slow != NULL)
	{
		if ((*head)->n != slow->n)
			return (0);

		*head = (*head)->next;
		slow = slow->next;
	}

	return (1);
}
