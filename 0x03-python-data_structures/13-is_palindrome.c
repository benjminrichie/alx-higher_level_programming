#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *reverse_listint(listint_t **head);

/**
 * is_palindrome - This func will write a function in C that
 * checks if a singly linked list is a palindrome.
 *
 * @head: Represents the input single linked list
 *
 * Return: Return: 0 if it is not a palindrome, 1 if it is a palindrome
 *
 */

int is_palindrome(listint_t **head)
{
	listint_t *aux = *head, *current = *head;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	while (current != NULL && aux != NULL && aux->next != NULL)
	{
		current = current->next;
		aux = aux->next->next;
	}
	current = reverse_listint(&current);
	aux = *head;
	while (aux != NULL && current != NULL)
	{
		if (aux->n != current->n)
			return (0);
		aux = aux->next;
		current = current->next;
	}
	return (1);
}
/**
 * reverse_listint - This func reverses a listint_t linked list
 *
 * @head: This is the pointer to the first node
 *
 * Return: Pointer to the first node
 *
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *next = *head, *current = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = current;
		current = *head;
		*head = next;
	}
	*head = current;
	return (*head);
}
