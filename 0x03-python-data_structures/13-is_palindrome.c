#include "lists.h"
/**
 * is_palindrome - entry
 * @head: struct var
 * Return: df
 */
int is_palindrome(listint_t **head)
{
	listint_t *w = *head, *f = *head, *node, *pr;
	int df = 0;

	while (f->next != NULL && f != NULL)
	{
		f = f->next->next;
		w = w->next;
	}
	node = w;
	pr = NULL;
	while (node)
	{
		f = node->next;
		node->next = pr;
		pr = node;
		node = f;
	}
	node = pr;
	f = *head;

	while (pr != NULL)
	{
		if (pr->n != f->n)
		{
			df = 1;
			break;
		}
		pr = pr->next;
		f = f->next;
	}

	pr = NULL;
	while (node != NULL)
	{
		f = node->next;
		node->next = pr;
		pr = node;
		node = f;
	}
	return (!df);
}
