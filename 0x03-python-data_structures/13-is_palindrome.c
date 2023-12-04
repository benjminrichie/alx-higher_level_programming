#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
*add_nodeint - This func adds a new node
*at the beginning of a listint_t list
*
*@head: This is the pointer or head of listint_t
*
*@n: This is an int to add in listint_t list
*
*Return: address (SUCCESS) else NULL (FAILED)
*
*/

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
*is_palindrome - This will identify if a
*linked list(singly) is palindrome
*
*@head: This is a pointer or head of listint_t
*
*Return: 1 (SUCCESS) else 0 (FAIL)
*
*/

int is_palindrome(listint_t **head)
{
	listint_t *head2 = *head;
	listint_t *aux = NULL, *aux2 = NULL;

	if (*head == NULL || head2->next == NULL)
		return (1);
	while (head2 != NULL)
	{
		add_nodeint(&aux, head2->n);
		head2 = head2->next;
	}
	aux2 = aux;
	while (*head != NULL)
	{
		if ((*head)->n != aux2->n)
		{
			free_listint(aux);
			return (0);
		}
		*head = (*head)->next;
		aux2 = aux2->next;
	}
	free_listint(aux);
	return (1);
}
