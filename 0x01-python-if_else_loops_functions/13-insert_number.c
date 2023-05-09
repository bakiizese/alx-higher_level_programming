#include "lists.h"
/**
 * insert_node - entry
 * @head: struct head
 * @number: int
 * Return: new
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *i = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (i == NULL || i->n >= number)
	{
		new->next = i;
		*head = new;
		return (new);
	}
	while ((i && i->next) && i->next->n < number)
		i = i->next;
	new->next = i->next;
	i->next = new;
	return (new);
}
