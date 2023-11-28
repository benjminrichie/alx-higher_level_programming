#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * print_listint - This func will simply print
 * all elements of a listint_t list
 *
 * @h: This is a pointer to head of list
 *
 * Return: The number of nodes
 */

size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int k; /* number of nodes */

	current = h;
        k = 0;

	while (current != NULL)
	{
		printf("%i\n", current->k);
		current = current->next;
		k++;
	}

	return (k);
}

/**
 * add_nodeint_end - This func only adds
 * a new node at the end of a listint_t list
 *
 * @head: This is a pointer to the first node of listint_t list
 *
 * @n: This is the int to be included in new node
 * 
 * Return: address of the new element(SUCCESS) else NULL(FAIL)
 *
 */

listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}

	return (new);
}

/**
 * free_listint - This func will free a listint_t list
 *
 * @head: This is a pointer to the list to be freed
 *
 * Return: Nothing
 *
 */

void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
