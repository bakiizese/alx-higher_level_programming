#include "lists.h"
/**
 * check_cycle - entry
 * list: struct
 * Return:: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *lw = list;
	listint_t *ft = list;

	if (!list)
		return (0);
	while (lw && ft && ft->next)
	{
		lw = lw->next;
		ft = ft->next->next;
		if (lw == ft)
			return (1);
	}
	return (0);
}

