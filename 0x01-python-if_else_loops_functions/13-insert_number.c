#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *i = *h, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number
	if (i = NULL || i->n >= number)
	{
		new->next = i;
		*h = new;
		return (new);
	}
	while ((i && i->next) && i->next->n < number)
		i = i->next;
	new->next = i->next;
	i->next = new;
	return (new);
}
