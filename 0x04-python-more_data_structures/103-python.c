#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <bytesobject.h>
/**
 * print+python_bytes - entry
 * @p
 */
void print_python_bytes(PyObject *p)
{
	int i;
	long int s;
	char *try = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &try, &s);
	printf("  s: %li\n", s);
	printf("  try string: %s\n", try);
	if (s < 10)
		printf("  first %li bytes:", s + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= s && i < 10; i++)
		printf(" %02hhx", try[i]);
	printf("\n");
}
/**
 * print_python_list - entry
 * @p: var
 */
void print_python_list(PyObject *p)
{
	int i;
        long int s = PyList_Size(p);
        PyListObject *list = (PyListObject *)p;
        const char *t;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", s);
        printf("[*] Allocated = %li\n", list->allocated);
        for (i = 0; i < s; i++)
        {
                t = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, t);
                if (!strcmp(t, "bytes"))
                        print_python_bytes(list->ob_item[i]);
        }
}
