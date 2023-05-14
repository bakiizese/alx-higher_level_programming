#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - entry
 * @p: struct var
 */
void print_python_list_info(PyObject *p)
{
	int n;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (n = 0; n < Py_SIZE(p); n++)
		printf("Element %d: %s\n", n, Py_TYPE(PyList_GetItem(p, n))->tp_name);
}
