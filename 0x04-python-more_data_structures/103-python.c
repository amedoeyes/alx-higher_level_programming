#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints bytes information
 *
 * @p: python Object
 */

void print_python_bytes(PyObject *p)
{
	char *buf;
	long size;
	long i;
	long bytes;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	buf = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", buf);

	if (size >= 10)
		bytes = 10;
	else
		bytes = size + 1;

	printf("  first %ld bytes:", bytes);

	for (i = 0; i < bytes; i++)
	{
		if (buf[i] >= 0)
			printf(" %02x", buf[i]);
		else
			printf(" %02x", 256 + buf[i]);
	}

	printf("\n");
}

/**
 * print_python_list - prints list information
 *
 * @p: python Object
 */

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyObject *object;
	long size = ((PyVarObject *)(p))->ob_size;
	long i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		object = ((PyListObject *)p)->ob_item[i];

		printf("Element %ld: %s\n", i, ((object)->ob_type)->tp_name);

		if (PyBytes_Check(object))
			print_python_bytes(object);
	}
}
