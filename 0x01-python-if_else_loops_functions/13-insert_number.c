#include "lists.h"

/**
 * insert_node - This func will only insert a number
 * into a sorted singly linked list.
 *
 * @head: This is the list head(pointer)
 *
 * @number: This is the0 number to store in the new node
 *
 * Return: Just a pointer
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *dog;
	listint_t *new;

	dog = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (dog->next != NULL)
	{
		if ((dog->next)->n >= number)
		{
			new->next = dog->next;
			dog->next = new;
			return (new);
		}
		dog = dog->next;
	}

	new->next = NULL;
	dog->next = new;
	return (new);
}
