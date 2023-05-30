#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - entry
 * @p: pointer
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s, ac, i;
	const char *te;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	s = var->ob_size;
	ac = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", ac);

	for (i = 0; i < s; i++)
	{
		te = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, te);
		if (strcmp(te, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(te, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}
/**
 * print_python_bytes - entry
 * @p: pointer
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t s, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		s = 10;
	else
		s = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", s);
	for (i = 0; i < s; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (s - 1))
			printf("\n");
		else
			printf(" ");
	}
}
/**
 * print_python_float - entry
 * @p: pointer
 */
void print_python_float(PyObject *p)
{
	char *buf = NULL;

	PyFloatObject *f_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buf = PyOS_double_to_string(f_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buf);
	PyMem_Free(buf);
}
