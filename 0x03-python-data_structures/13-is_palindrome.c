#include "lists.h"

/**
 * is_palindrome - tests if linked lists is palindrome
 * @head: address of pointer to list
 * Return: 1 is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *w = *head;
	listint_t *f = *head, *node, *pr;
	int df = 0;

	while (f != NULL && f->next != NULL)
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
	f = *head;
	node = pr;
	while (pr)
	{
		if (f->n != pr->n)
		{
			df = 1;
			break;
		}
		f = f->next;
		pr = pr->next;
	}
	pr = NULL;
	while (node)
	{
		f = node->next;
		node->next = pr;
		pr = node;
		node = f;
	}
	return (!df);
}
